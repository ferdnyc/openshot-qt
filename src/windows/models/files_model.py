"""
 @file
 @brief This file contains the project file model, used by the project tree
 @author Noah Figg <eggmunkee@hotmail.com>
 @author Jonathan Thomas <jonathan@openshot.org>

 @section LICENSE

 Copyright (c) 2008-2018 OpenShot Studios, LLC
 (http://www.openshotstudios.com). This file is part of
 OpenShot Video Editor (http://www.openshot.org), an open-source project
 dedicated to delivering high quality video editing and animation solutions
 to the world.

 OpenShot Video Editor is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 OpenShot Video Editor is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with OpenShot Library.  If not, see <http://www.gnu.org/licenses/>.
 """

import os
import json
import re
import glob

from PyQt5.QtCore import (
    QMimeData, Qt, QObject, pyqtSlot,
    QSortFilterProxyModel, QItemSelectionModel,
    QModelIndex, QAbstractTableModel, QUrl, QSize,
    QByteArray,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from classes import updates
from classes import info
from classes.image_types import is_image
from classes.query import File
from classes.logger import log
from classes.app import get_app
from requests import get

import openshot


class FileRoles:
    Id = Qt.UserRole + 11
    Path = Qt.UserRole + 12
    MediaType = Qt.UserRole + 13
    DataKey = Qt.UserRole + 14


class FileRoleNames:
    custom = {
        FileRoles.Id: QByteArray(b"id"),
        FileRoles.Path: QByteArray(b"path"),
        FileRoles.MediaType: QByteArray(b"mediatype"),
        FileRoles.DataKey: QByteArray(b"datakey"),
    }


class FileModelColumns:
    Data = 0
    Id = 0
    Icon = 0
    Title = 0
    Tags = 2
    Path = 0
    MediaType = 0


class FileFilterProxyModel(QSortFilterProxyModel):
    """Proxy class used for sorting and filtering model data"""

    def filterAcceptsRow(self, sourceRow, sourceParent):
        """Apply filtering parameters to data for requested row"""
        if not self.filter_group and self.filterRegexp().isEmpty():
            # Just run built-in parent filter logic
            return super().filterAcceptsRow(sourceRow, sourceParent)

        # Retrieve primary information from data column
        index = self.sourceModel().index(sourceRow, FileModelColumns.Data, sourceParent)
        file_title = self.sourceModel().data(index, Qt.DisplayRole)
        media_type = self.sourceModel().data(index, FileRoles.MediaType)
        row_id = self.sourceModel().data(index, FileRoles.Id)

        # Filter by media type, if enabled
        if len(self.filter_group) > 0 and media_type not in self.filter_group:
            log.debug(
                "Rejecting %s row %s, not in %s",
                media_type, row_id, self.filter_group)
            return False

        # Retrieve tags list from tags column
        index = self.sourceModel().index(sourceRow, FileModelColumns.Data, sourceParent)
        tags = self.sourceModel().data(index, Qt.DisplayRole)

        # Match against regex pattern and/or media type grouping
        return any([
            self.filterRegExp().indexIn(file_title) >= 0,
            self.filterRegExp().indexIn(tags) >= 0
            ])

    @pyqtSlot(QAction)
    def update_filter_group(self, selected: QAction):
        """ Update the media type accepted by the filter """
        log.debug("Setting filter group to %s", selected.data() or "all")
        if selected.data():
            self.filter_group = {selected.data()}
        else:
            self.filter_group = {"audio", "image", "video"}
        self.invalidateFilter()

    def __init__(self, *args, **kwargs):
        # Call base class implementation
        super().__init__(*args, **kwargs)
        self.filter_group = {"audio", "image", "video"}


class FilesModel(QAbstractTableModel):
    """Adapter which uses the project "files" list as its data storage backend,
    and provides a standard Qt data model interface to the file data"""

    app = get_app()
    _ = app._tr

    data_labels = [
        ("", ""),
        (_("Name"), "name"),
        (_("Tags"), "tags"),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        app = get_app()
        self._data = []
        app.window.OpenProjectSignal.connect(self.reset_model)
        self.reset_model()

    def reset_model(self):
        app = get_app()
        self.beginResetModel()
        if hasattr(app, "project"):
            self._data = app.project._data.get("files")
        self._thumb_paths = {}
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        """ Standard Qt model method for retrieving model length """
        if parent and parent.isValid():
            # Our indexes don't have children
            return 0
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        """ Standard Qt model method for retrieving model width """
        return 6

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        """ Standard Qt model method providing metadata on model contents """
        _flags = (
            Qt.ItemIsSelectable | Qt.ItemIsEnabled
            | Qt.ItemNeverHasChildren
            )
        if not index.isValid():
            return Qt.NoItemFlags
        if index.column() == 0:
            # Add drag & drop for first column data
            _flags = _flags | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled
        if index.column() in [1, 2]:
            # Name and Tags can be edited directly in the list
            _flags = _flags | Qt.ItemIsEditable
        return _flags

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        """ Standard Qt method for 2-dimensional models """
        if orientation is Qt.Vertical:
            return f"Row {section}"
        if role == Qt.DisplayRole:
            if section < 3:
                # Columns 0-2 have header text, others are hidden
                return self.data_labels[section][0]
            return ""
        if role == Qt.TextAlignmentRole:
            return Qt.AlignLeft

    def data(self, index: QModelIndex, role: int):
        """ Standard Qt method for retrieving model data """
        text_roles = [Qt.DisplayRole, Qt.ToolTipRole, Qt.EditRole]
        if not index.isValid():
            return

        file_data = self._data[index.row()]
        file_id = file_data.get("id")
        file_path = file_data.get("path")
        file_title = file_data.get("title", os.path.basename(file_path))

        # Currently we support the old 6-column model as a legacy
        # comptibility feature. Eventually this will be phased out,
        # and only the visible 3-column model will be supported, with
        # additional data being stored at column 0 in custom UserRoles
        # enumerated by the FileRoles object.
        col = index.column()
        if col in [0, 1] and role in text_roles:
            return file_title
        if col == 2 and role in text_roles:
            return file_data.get("tags", None)
        if col == 3 and role in text_roles:
            return file_data.get("media_type", None)
        if col == 4 and role in text_roles:
            return file_path
        if col == 5 and role in text_roles:
            return file_id

        # Support lookup by custom role
        if role == FileRoles.Id:
            return file_id
        if role == FileRoles.Path:
            return file_path
        if role == FileRoles.MediaType:
            return file_data.get("media_type", None)

        # Retrieve the underlying dict key corresponding to a visible column
        # (which is labeled using a localized heading string)
        # XXX: Should this be in headerData()? (as well?)
        if role == FileRoles.DataKey:
            if col < 3:
                return self.data_labels[col][1]
            else:
                return ''

        # Support icon lookup on the first or second column
        if col in [0, 1] and role == Qt.DecorationRole:
            return self.lookup_thumb(file_data)

    def setData(self, index: QModelIndex, value, role: int) -> bool:
        # Skip calls that don't provide any changes we can store
        if not index.isValid() or value == self.data(index, role):
            return True

        # Update the backend data store
        file_id = index.data(FileRoles.Id)
        key = index.data(FileRoles.DataKey)

        if not file_id or not key:
            return False
        log.debug("%s: Setting %s=%s", file_id, key, value)

        # Get file object and update the data at the corresponding key
        f = File.get(id=file_id)
        f.type = "update"
        f.key = [File.object_name, {"id": file_id}]
        f.data = {key: value}
        f.save()

        # Notify views and others about updated row data
        if key == "tags":
            # Signal one model item (tag cell) updated
            l_top = r_bottom = index
        else:
            # Signal a refresh of the whole row
            l_top = index.sibling(index.row(), 0)
            r_bottom = index.sibling(index.row(), self.columnCount() - 1)
        self.dataChanged.emit(l_top, r_bottom)
        return True

    def lookup_thumb(self, file_data: dict):
        file_id = file_data.get("id")
        if file_id not in self._thumb_paths:
            thumb_frame = 1
            if 'start' in file_data:
                # We need to offset the frame being thumbnailed
                fps = file_data["fps"]
                fps_float = float(fps["num"]) / float(fps["den"])
                thumb_frame = round(float(file_data['start']) * fps_float) + 1
            # Get path from thumbnail service
            thumb_path = self.get_thumb_path(
                file_id, thumb_frame, clear_cache=True)
            self._thumb_paths.update({
                file_id: thumb_path,
                })
        return QIcon(self._thumb_paths.get(file_id, None))

    @staticmethod
    def get_thumb_path(
            file_id, thumbnail_frame, clear_cache=False):
        """Get thumbnail path by invoking HTTP thumbnail request"""

        # Clear thumb cache (if requested)
        thumb_cache = ""
        if clear_cache:
            thumb_cache = "no-cache/"

        # Connect to thumbnail server and get image
        thumb_server_details = get_app().window.http_server_thread.server_address
        thumb_address = "http://%s:%s/thumbnails/%s/%s/path/%s" % (
            thumb_server_details[0],
            thumb_server_details[1],
            file_id,
            thumbnail_frame,
            thumb_cache)
        r = get(thumb_address)
        if r.ok:
            # Update thumbnail path to real one
            return r.text
        else:
            return ''

    def roleNames(self):
        """Provide the names of all defined roles in the model"""
        names = super().roleNames()
        names.update(FileRoleNames.custom)
        return names

    def mimeData(self, indexes):
        """Return MIME representation of selected files"""
        mime_data = QMimeData()
        # Drop invalid indexes
        indexes = list([idx for idx in indexes if idx.isValid()])
        log.debug("Generating MIME data for %d model indexes", len(indexes))
        # Grab all of the unique file IDs involved
        ids = [idx.data(FileRoles.Id) for idx in indexes]
        # Deduplicate list (all indexes in a given row have the same ID)
        ids = list(set(ids))
        log.debug("IDs: %s", ids)
        # Format as openshot:// URIs (readable by properties model / timeline)
        uris = [QUrl(f"openshot://file/{i}") for i in ids]
        mime_data.setUrls(uris)
        log.debug("URIs: %s", str(list(uris)))
        # Set the MIME data icon to the first valid item icon we can find
        icons = [idx.data(Qt.DecorationRole) for idx in indexes]
        for icon in icons:
            if isinstance(icon, QIcon):
                mime_data.setImageData(icon.pixmap(QSize(48, 48)))
                break
        return mime_data


class FilesManager(updates.UpdateInterface, QObject):
    # This method is invoked by the UpdateManager each time a change happens (i.e UpdateInterface)
    def changed(self, action):

        # Something was changed in the 'files' list
        if (len(action.key) >= 1 and action.key[0].lower() == "files") or action.type == "load":
            # Refresh project files model
            if action.type == "insert":
                # Don't clear the existing items if only inserting new things
                self.update_model(clear=False)
            elif action.type == "delete" and action.key[0].lower() == "files":
                # Don't clear the existing items if only deleting things
                self.update_model(clear=False, delete_file_id=action.key[1].get('id', ''))
            elif action.type == "update" and action.key[0].lower() == "files":
                # Do nothing for file updates
                pass
            else:
                # Clear existing items
                self.update_model(clear=True)

    def update_model(self, clear=True, delete_file_id=None):
        log.debug("Updating files model.")
        if clear:
            self.base_model.reset_model()
        return True

    def add_files(self, files, image_seq_details=None, quiet=False):
        # Access translations
        app = get_app()
        _ = app._tr

        # Make sure we're working with a list of files
        if not isinstance(files, (list, tuple)):
            files = [files]

        start_count = len(files)

        # Signal that the model will be growing
        start_row = self.base_model.rowCount()
        end_row = start_row + start_count - 1
        self.base_model.beginInsertRows(QModelIndex(), start_row, end_row)

        for count, filepath in enumerate(files):
            (dir_path, filename) = os.path.split(filepath)

            # Check for this path in our existing project data
            new_file = File.get(path=filepath)

            # If this file is already found, skip
            if new_file:
                del new_file
                continue

            try:
                # Load filepath in libopenshot clip object (which will try multiple readers to open it)
                clip = openshot.Clip(filepath)

                # Get the JSON for the clip's internal reader
                reader = clip.Reader()
                file_data = json.loads(reader.Json())

                # Determine media type
                if file_data["has_video"] and not is_image(file_data):
                    file_data["media_type"] = "video"
                elif file_data["has_video"] and is_image(file_data):
                    file_data["media_type"] = "image"
                elif file_data["has_audio"] and not file_data["has_video"]:
                    file_data["media_type"] = "audio"
                else:
                    # If none set, just assume video
                    file_data["media_type"] = "video"

                # Save new file to the project data
                new_file = File()
                new_file.data = file_data

                # Is this an image sequence / animation?
                seq_info = image_seq_details or self.get_image_sequence_details(filepath)

                if seq_info:
                    # Update file with correct path
                    folder_path = seq_info["folder_path"]
                    base_name = seq_info["base_name"]
                    fixlen = seq_info["fixlen"]
                    digits = seq_info["digits"]
                    extension = seq_info["extension"]

                    if not fixlen:
                        zero_pattern = "%d"
                    else:
                        zero_pattern = "%%0%sd" % digits

                    # Generate the regex pattern for this image sequence
                    pattern = "%s%s.%s" % (base_name, zero_pattern, extension)

                    # Split folder name
                    folderName = os.path.basename(folder_path)
                    if not base_name:
                        # Give alternate name
                        new_file.data["name"] = "%s (%s)" % (folderName, pattern)

                    # Load image sequence (to determine duration and video_length)
                    image_seq = openshot.Clip(os.path.join(folder_path, pattern))

                    # Update file details
                    new_file.data["path"] = os.path.join(folder_path, pattern)
                    new_file.data["media_type"] = "video"
                    new_file.data["duration"] = image_seq.Reader().info.duration
                    new_file.data["video_length"] = image_seq.Reader().info.video_length

                    log.info('Imported {} as image sequence {}'.format(
                        filepath, pattern))

                    # Remove any other image sequence files from the list we're processing
                    match_glob = "{}{}.{}".format(base_name, '[0-9]*', extension)
                    log.debug("Removing files from import list with glob: {}".format(match_glob))
                    for seq_file in glob.iglob(os.path.join(folder_path, match_glob)):
                        # Don't remove the current file, or we mess up the for loop
                        if seq_file in files and seq_file != filepath:
                            files.remove(seq_file)

                if not seq_info:
                    # Log our not-an-image-sequence import
                    log.info("Imported media file {}".format(filepath))

                # Save file
                new_file.save()

                if start_count > 15:
                    message = _("Importing %(count)d / %(total)d") % {
                            "count": count,
                            "total": len(files) - 1
                            }
                    app.window.statusBar.showMessage(message, 15000)

                # Let the event loop run to update the status bar
                get_app().processEvents()

                prev_path = app.project.get("import_path")
                if dir_path != prev_path:
                    app.updates.update_untracked(["import_path"], dir_path)

            except Exception as ex:
                # Log exception
                log.warning("Failed to import {}: {}".format(filepath, ex))

                if not quiet:
                    # Show message box to user
                    app.window.invalidImage(filename)

        # Reset list of ignored paths
        self.ignore_image_sequence_paths = []

        # Report completion
        self.base_model.endInsertRows()
        message = _("Imported %(count)d files") % {"count": len(files) - 1}
        app.window.statusBar.showMessage(message, 3000)

    def get_image_sequence_details(self, file_path):
        """Inspect a file path and determine if this is an image sequence"""

        # Get just the file name
        (dirName, fileName) = os.path.split(file_path)

        # Image sequence imports are one per directory per run
        if dirName in self.ignore_image_sequence_paths:
            return None

        extensions = ["png", "jpg", "jpeg", "gif", "tif", "svg"]
        match = re.findall(r"(.*[^\d])?(0*)(\d+)\.(%s)" % "|".join(extensions), fileName, re.I)

        if not match:
            # File name does not match an image sequence
            return None

        # Get the parts of image name
        base_name = match[0][0]
        fixlen = match[0][1] > ""
        number = int(match[0][2])
        digits = len(match[0][1] + match[0][2])
        extension = match[0][3]

        full_base_name = os.path.join(dirName, base_name)

        # Check for images which the file names have the different length
        fixlen = fixlen or not (
            glob.glob("%s%s.%s" % (full_base_name, "[0-9]" * (digits + 1), extension))
            or glob.glob("%s%s.%s" % (full_base_name, "[0-9]" * ((digits - 1) if digits > 1 else 3), extension))
        )

        # Check for previous or next image
        for x in range(max(0, number - 100), min(number + 101, 50000)):
            if x != number and os.path.exists(
               "%s%s.%s" % (full_base_name, str(x).rjust(digits, "0") if fixlen else str(x), extension)):
                break  # found one!
        else:
            # We didn't discover an image sequence
            return None

        # Found a sequence, ignore this path (no matter what the user answers)
        # To avoid issues with overlapping/conflicting sets of files,
        # we only attempt one image sequence match per directory
        log.debug("Ignoring path for image sequence imports: {}".format(dirName))
        self.ignore_image_sequence_paths.append(dirName)

        log.info('Prompt user to import sequence starting from {}'.format(fileName))
        if not get_app().window.promptImageSequence(fileName):
            # User said no, don't import as a sequence
            return None

        # Yes, import image sequence
        parameters = {
            "folder_path": dirName,
            "base_name": base_name,
            "fixlen": fixlen,
            "digits": digits,
            "extension": extension
        }
        return parameters

    def process_urls(self, qurl_list):
        """Recursively process QUrls from a QDropEvent"""
        import_quietly = False
        media_paths = []

        for uri in qurl_list:
            filepath = uri.toLocalFile()
            if not os.path.exists(filepath):
                continue
            if filepath.endswith(".osp") and os.path.isfile(filepath):
                # Auto load project passed as argument
                get_app().window.OpenProjectSignal.emit(filepath)
                return True
            if os.path.isdir(filepath):
                import_quietly = True
                log.info("Recursively importing {}".format(filepath))
                try:
                    for r, _, f in os.walk(filepath):
                        media_paths.extend(
                            [os.path.join(r, p) for p in f])
                except OSError:
                    log.warning("Directory recursion failed", exc_info=1)
            elif os.path.isfile(filepath):
                media_paths.append(filepath)
        if not media_paths:
            return
        # Import all new media files
        media_paths.sort()
        log.debug("Importing file list: {}".format(media_paths))
        self.add_files(media_paths, quiet=import_quietly)

    def update_file_thumbnail(self, file_id):
        """Update/re-generate the thumbnail of a specific file"""
        pass

    def selected_file_ids(self):
        """ Get a list of file IDs for all selected files """
        # Get the indexes for column 5 of all selected rows
        selected = self.selection_model.selectedRows(0)
        log.debug(", ".join([idx.data() for idx in selected]))

        return [idx.data(FileRoles.Id) for idx in selected]

    def selected_files(self):
        """ Get a list of File objects representing the current selection """
        files = []
        for id in self.selected_file_ids():
            files.append(File.get(id=id))
        return files

    def current_file_id(self):
        """ Get the file ID of the current files-view item, or the first selection """
        cur = self.selection_model.currentIndex()

        if not cur or not cur.isValid() and self.selection_model.hasSelection():
            cur = self.selection_model.selectedIndexes()[0]

        if cur and cur.isValid():
            return cur.data(FileRoles.Id)

    def current_file(self):
        """ Get the File object for the current files-view item, or the first selection """
        cur_id = self.current_file_id()
        if cur_id:
            return File.get(id=cur_id)

    def __init__(self, *args):
        # Call init for superclass QObject
        QObject.__init__(self, *args)

        # Add self as listener to project data updates
        # (undo/redo, as well as normal actions handled within this class all update the model)
        app = get_app()
        app.updates.add_listener(self)

        # Create standard model
        self.base_model = FilesModel()
        self.base_model.setObjectName("files.model")

        self.ignore_image_sequence_paths = []

        # Create proxy model (for sorting and filtering)
        self.proxy_model = FileFilterProxyModel(self)
        self.proxy_model.setObjectName("files.sortfilterproxy")
        self.proxy_model.setDynamicSortFilter(True)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.setSortCaseSensitivity(Qt.CaseSensitive)
        self.proxy_model.setSourceModel(self.base_model)
        self.proxy_model.setSortLocaleAware(True)

        # Create selection model to share between views
        self.selection_model = QItemSelectionModel(self.proxy_model, self)
        self.selection_model.setObjectName("files.selection")

        # "Alias" the model that faces the rest of the code
        self.model = self.proxy_model

        # Make the filtering slots visible to MainWindow
        self.filter_text_changed = self.proxy_model.setFilterFixedString
        self.filter_group_changed = self.proxy_model.update_filter_group

        # Attempt to load model testing interface, if requested
        # (will only succeed with Qt 5.11+)
        if "files" in info.MODEL_TEST or "all" in info.MODEL_TEST:
            try:
                # Create model tester objects
                from PyQt5.QtTest import QAbstractItemModelTester
                self.model_tests = []
                for m in [self.proxy_model, self.base_model]:
                    model_tester = QAbstractItemModelTester(
                        m, QAbstractItemModelTester.FailureReportingMode.Warning
                        )
                    name = f"ModelTester.{m.objectName()}"
                    model_tester.setObjectName(name)
                    self.model_tests.append(model_tester)
                log.info(
                    "Enabled %d model tests for project files data",
                    len(self.model_tests))
            except ImportError:
                pass

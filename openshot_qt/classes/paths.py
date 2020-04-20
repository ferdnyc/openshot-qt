"""
@file
@brief This file contains the current version number of OpenShot, along with other global settings.
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

import sys
import os
from pprint import pprint
from openshot_qt import OPENSHOT_PATH

# Application paths
PATH = OPENSHOT_PATH
RESOURCES = os.path.join(PATH, "resources")
PROFILES = os.path.join(PATH, "profiles")
IMAGES = os.path.join(PATH, "images")
EXPORT_PRESETS = os.path.join(PATH, "presets")

from PyQt5.QtCore import QStandardPaths as QSP

# User account top-level paths
HOME = QSP.standardLocations(QSP.HomeLocation)[0]

# Writable config storage
APP_DATA = QSP.writableLocation(QSP.AppDataLocation)
USER = APP_DATA
CONFIG = QSP.writableLocation(QSP.AppConfigLocation)

BACKUP_FILE = os.path.join(CONFIG, "backup.osp")
RECOVERY = os.path.join(CONFIG, "recovery")

# Writable cache
CACHE = QSP.writableLocation(QSP.CacheLocation)
PREVIEW_CACHE = os.path.join(CACHE, "preview-cache")

# Writable temp space
ASSETS = os.path.join(QSP.writableLocation(QSP.TempLocation), "assets")
BLENDER = os.path.join(ASSETS, "blender")
TITLE = os.path.join(ASSETS, "titles")

# Not necessarily writable (by us)
USER_CONTENT = os.path.join(QSP.standardLocations(QSP.DocumentsLocation)[0], "OpenShot")
USER_TRANSITIONS = os.path.join(USER_CONTENT, "transitions")
USER_TITLES = os.path.join(USER_CONTENT, "title_templates")
USER_PROFILES = os.path.join(USER_CONTENT, "profiles")
USER_PRESETS = os.path.join(USER_CONTENT, "presets")

# User files
USER_DEFAULT_PROJECT = os.path.join(USER_CONTENT, "default.project")

# Create user paths if they do not exist
# (this is where temp files are stored... such as cached thumbnails)
_paths = [
    APP_DATA,
    CONFIG,
    RECOVERY,
    PREVIEW_CACHE,
    BLENDER,
    TITLE,
    USER_TRANSITIONS,
    USER_TITLES,
    USER_PROFILES,
    USER_PRESETS,
]
_paths.sort()

# Debugging
def debug_paths():
    pprint(locals())

# Create any missing paths
def makedirs():
    try:
        dirs = [os.makedirs(os.fsencode(f), exist_ok=True) for f in _paths]
    except PermissionError as ex:
        print.stderr.write("Failed to create directory, {}".format(ex))


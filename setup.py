"""
 @file
 @brief Setup script to install OpenShot (on Linux and without any dependencies such as libopenshot)
 @author Jonathan Thomas <jonathan@openshot.org>

 @section LICENSE

 Copyright (c) 2008-2016 OpenShot Studios, LLC
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
import sys
import fnmatch
import subprocess
import setuptools
from shutil import copytree, rmtree, copy


from openshot_qt.classes import info
from logging import log, INFO

log(INFO, "Execution path: %s" % os.path.abspath(__file__))

# Boolean: running as root?
ROOT = os.geteuid() == 0
# For Debian packaging it could be a fakeroot so reset flag to prevent execution of
# system update services for Mime and Desktop registrations.
# The debian/openshot.postinst script must do those.
if not os.getenv("FAKEROOTKEY") == None:
    log(INFO, "NOTICE: Detected execution in a FakeRoot so disabling calls to system update services.")
    ROOT = False

os_files = [
    # XDG application description
    ('share/applications', ['xdg/org.openshot.OpenShot.desktop']),
    # AppStream metadata
    ('share/metainfo', ['xdg/org.openshot.OpenShot.appdata.xml']),
    # Debian menu system application icon
    ('share/pixmaps', ['xdg/openshot-qt.svg']),
    # XDG Freedesktop icon paths
    ('share/icons/hicolor/scalable/apps', ['xdg/openshot-qt.svg']),
    ('share/icons/hicolor/64x64/apps', ['xdg/icon/64/openshot-qt.png']),
    ('share/icons/hicolor/256x256/apps', ['xdg/icon/256/openshot-qt.png']),
    ('share/icons/hicolor/512x512/apps', ['xdg/icon/512/openshot-qt.png']),
    # XDG desktop mime types cache
    ('share/mime/packages', ['xdg/org.openshot.OpenShot.xml']),
    # launcher (mime.types)
    ('lib/mime/packages', ['xdg/openshot-qt']),
]

# Find files matching patterns
#def find_files(directory, patterns):
#    """ Recursively find all files in a folder tree """
#    for root, dirs, files in os.walk(directory):
#        for basename in files:
#            if ".pyc" not in basename and "__pycache__" not in basename:
#                for pattern in patterns:
#                    if fnmatch.fnmatch(basename, pattern):
#                        filename = os.path.join(root, basename)
#                        yield filename


#package_data = {}

# Find all project files
#src_files = []
#for filename in find_files(os.path.abspath("openshot_qt"), ["*"]):
#    src_files.append(filename.replace(os.path.abspath("openshot_qt"), ""))
#package_data["openshot_qt"] = src_files

# Call the main Distutils setup command
# -------------------------------------
dist = setuptools.setup(
    packages=setuptools.find_packages(),
    package_data={
        'openshot_qt': [
            'openshot_qt/*.*',
            'openshot_qt/classes/*.*',
            'openshot_qt/classes/**/*.*',
            'openshot_qt/windows/**/*.*',
            'openshot_qt/timeline/**/*.*',
            'openshot_qt/language/*',
            'openshot_qt/effects/icons/*.*',
            'openshot_qt/blender/**/*.*'
        ]
    },
    data_files=os_files,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['openshot-qt = openshot_qt:main']
    },
    python_requires=">=3.0",
    install_requires=[
        'openshot',
        'PyQt5',
        'PyQt5.QtWebkit',
        'zmq',
        'httplib2',
        'requests',
        'setuptools'
    ],
    **info.SETUP
)
# -------------------------------------

FAILED = 'Failed to update.'

if ROOT and dist != None:
    # update the XDG Shared MIME-Info database cache
    try:
        log(INFO, 'Updating the Shared MIME-Info database cache.')
        subprocess.call(["update-mime-database", os.path.join(sys.prefix, "share/mime/")])
    except:
        log(ERROR, FAILED)

    # update the mime.types database
    try:
        log(INFO, 'Updating the mime.types database.')
        subprocess.call("update-mime")
    except:
        log(ERROR, FAILED)

    # update the XDG .desktop file database
    try:
        log(INFO, 'Updating the .desktop file database.')
        subprocess.call(["update-desktop-database"])
    except:
        log(ERROR, FAILED)
    sys.stdout.write("\n-----------------------------------------------")
    sys.stdout.write("\nInstallation Finished!")
    sys.stdout.write("\nRun OpenShot by typing 'openshot-qt' or through the Applications menu.")
    sys.stdout.write("\n-----------------------------------------------\n")

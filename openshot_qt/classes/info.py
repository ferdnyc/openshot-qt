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

from PyQt5.QtCore import QDir

try:
    from openshot_qt import OPENSHOT_PATH
except ImportError as ex:
    print(
        "Can't locate openshot_qt! This won't go well... {}".format(ex),
        file=sys.stdout
    )

MINIMUM_LIBOPENSHOT_VERSION = "0.2.5"
DATE = "20200228000000"
NAME = "openshot-qt"
PRODUCT_NAME = "OpenShot Video Editor"
GPL_VERSION = "3"
DESCRIPTION = "Create and edit stunning videos, movies, and animations"
COMPANY_NAME = "OpenShot Studios, LLC"
COPYRIGHT = "Copyright (c) 2008-2018 %s" % COMPANY_NAME

CWD = os.getcwd()

# Blender minimum version required (a string value)
BLENDER_MIN_VERSION = "2.80"

# Languages
CMDLINE_LANGUAGE = None
CURRENT_LANGUAGE = 'en_US'
SUPPORTED_LANGUAGES = ['en_US']

try:
    from openshot_qt.language import openshot_lang  # unused
    language_path = ":/locale/"
except ImportError:
    language_path = os.path.join(OPENSHOT_PATH, 'language')
    print("Compiled translation resources missing!")
    print("Loading translations from: {}".format(language_path))

# Compile language list from :/locale resource
langdir = QDir(language_path)
langs = langdir.entryList(['OpenShot_*.qm'], QDir.NoDotAndDotDot | QDir.Files,
                          sort=QDir.Name)
for trpath in langs:
    SUPPORTED_LANGUAGES.append(trpath.split('.')[1])


def website_language():
    """Get the current website language code for URLs"""
    if CURRENT_LANGUAGE == "zh_CN":
        return "zh-hans/"
    elif CURRENT_LANGUAGE == "zh_TW":
        return "zh-hant/"
    elif CURRENT_LANGUAGE == "en_US":
        return ""
    else:
        return "%s/" % CURRENT_LANGUAGE.split("_")[0].lower()

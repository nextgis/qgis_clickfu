# ******************************************************************************
#
# Click-fu
# ---------------------------------------------------------
# Send click coordinates to various geoservices.
#
# Copyright (C) 2008-2010 Barry Rownligson (barry.rowlingson@gmail.com)
#               2014 NextGIS (info@nextgis.org)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/licenses/>. You can also obtain it by writing
# to the Free Software Foundation, 51 Franklin Street, Suite 500 Boston,
# MA 02110-1335 USA.
#
# ******************************************************************************

import os
from os import path

from qgis.core import QgsApplication
from qgis.PyQt.QtCore import QCoreApplication, QTranslator
from qgis.PyQt.QtWidgets import QAction, QApplication, QMenu

from .about_dialog import AboutDialog
from .flickrMap import flickrPics
from .geoHack import geoHack

# import resources
from .googlemaps import googleMap

# from geonames import gnExtended
from .osm import osmEditMap, osmEditMapJOSM, osmViewMap
from .rosreestr import Rosreestr


class MainPlugin:
    def __init__(self, iface):
        # Save a reference to the QGIS iface
        self.iface = iface
        self.plugin_dir = path.dirname(__file__)
        self._translator = None
        self.__init_translator()

    def initGui(self):
        # Create menu
        self.menu = QMenu("Click-fu")

        self.googleMaps = googleMap(self.iface)
        # self.gnExtended = gnExtended(self.iface)
        self.osmViewMap = osmViewMap(self.iface)
        self.osmEditMap = osmEditMap(self.iface)
        self.osmEditMapJOSM = osmEditMapJOSM(self.iface)
        self.flickr = flickrPics(self.iface)
        self.geoHack = geoHack(self.iface)
        self.Rosreestr = Rosreestr(self.iface)

        # Create action
        # self.about = QAction("About Click-fu",self.iface.mainWindow())
        self.actionAbout = QAction(
            QApplication.translate("Click-Fu", "About"),
            self.iface.mainWindow(),
        )
        self.actionAbout.triggered.connect(self.about)

        self.menu.addActions(
            [
                self.googleMaps,
                self.osmViewMap,
                self.osmEditMap,
                self.osmEditMapJOSM,
                self.flickr,
                self.geoHack,
                self.Rosreestr,
            ]
        )
        self.menu.addSeparator()
        self.menu.addAction(self.actionAbout)

        _temp_act = QAction("temp", self.iface.mainWindow())
        self.iface.addPluginToWebMenu("_tmp", _temp_act)
        self.iface.webMenu().addMenu(self.menu)
        self.iface.removePluginWebMenu("_tmp", _temp_act)

        self.iface.webMenu().addMenu(self.menu)

    def about(self):
        dialog = AboutDialog(os.path.basename(self.plugin_dir))
        dialog.exec_()

    def unload(self):
        # remove menu
        self.menu.deleteLater()

        # clean vars
        self.menu = None

    def __init_translator(self):
        # initialize locale
        locale = QgsApplication.instance().locale()

        def add_translator(locale_path):
            if not path.exists(locale_path):
                return
            translator = QTranslator()
            translator.load(locale_path)
            QCoreApplication.installTranslator(translator)
            self._translator = translator  # Should be kept in memory

        add_translator(
            path.join(self.plugin_dir, "i18n", f"clickfu_{locale}.qm")
        )

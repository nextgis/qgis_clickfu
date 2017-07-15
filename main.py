# -*- coding: utf-8 -*-

#******************************************************************************
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
#******************************************************************************

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from googlemaps import googleMap
from osm import osmViewMap, osmEditMap, osmEditMapJOSM
from flickrMap import flickrPics
from geoHack import geoHack
from rosreestr import Rosreestr


class MainPlugin(object):
    def __init__(self, iface):
        # Save a reference to the QGIS iface
        self.iface = iface

    def initGui(self):
        # Create action
        self.menu = QMenu("Go2Webmap")

        self.googleMaps = googleMap(self.iface)
        self.osmViewMap = osmViewMap(self.iface)
        self.osmEditMap = osmEditMap(self.iface)
        self.osmEditMapJOSM = osmEditMapJOSM(self.iface)
        self.flickr = flickrPics(self.iface)
        self.geoHack = geoHack(self.iface)
        self.rosreestr = Rosreestr(self.iface)

        self.menu.addActions([
            self.googleMaps,
            self.osmViewMap,
            self.osmEditMap,
            self.osmEditMapJOSM,
            self.flickr,
            self.geoHack,
            self.rosreestr
        ])

        menuBar = self.iface.mainWindow().menuBar()
        menuBar.addMenu(self.menu)

    def unload(self):
        # Remove the plugin
        pass

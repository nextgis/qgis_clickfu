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


class cfAction(QAction):
    def __init__(self, name, iface):
        QAction.__init__(self, self.name(), iface.mainWindow())
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.setWhatsThis(self.desc())
        self.setToolTip(self.desc())
        QObject.connect(self, SIGNAL("triggered()"), self.doit)

    def doit(self):
        self.tool = cfTool(self.iface, self.createURL)
        self.canvas.setMapTool(self.tool)
        return None


class cfTool(QgsMapTool):
    def __init__(self, iface, urlCreator):
        QgsMapTool.__init__(self, iface.mapCanvas())
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.urlCreator = urlCreator

    def canvasReleaseEvent(self, e):
        point = self.canvas.getCoordinateTransform().toMapPoint(e.pos().x(), e.pos().y())
        pt85 = pointToWGS84(point)
        url = self.urlCreator(pt85.y(), pt85.x())
        #print "event pos: ",e.pos().x(),",",e.pos().y()
        #print "point pos: ",point.x(),point.y()
        #print "point w84: ",pt85.x(),pt85.y()
        QDesktopServices.openUrl(QUrl(url))
        return None


def convertLat(lat):
    """ convert latitude in signed decimal degrees to (degrees, minutes, seconds, hemisphere) """
    return convertDMS(lat, "NS")


def convertLon(lon):
    return convertDMS(lon, "EW")


def convertDMS(dms, hemis):
    if dms > 0:
        hemi = hemis[0]
    else:
        hemi = hemis[1]
        dms = -dms
    d = int(dms)
    ms = (dms - d) * 60.0
    m = int(ms)
    s = (ms - m) * 60.0
    return (d, m, s, hemi)


def pointToWGS84(point):
    p = QgsProject.instance()
    (proj4string, ok) = p.readEntry("SpatialRefSys", "ProjectCRSProj4String")
    if not ok:
        return point
    t = QgsCoordinateReferenceSystem(4326)
    f = QgsCoordinateReferenceSystem()
    f.createFromProj4(proj4string)
    transformer = QgsCoordinateTransform(f, t)
    pt = transformer.transform(point)
    return pt

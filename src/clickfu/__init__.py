# -*- coding: utf-8 -*-

# ******************************************************************************
#
# Click-fu
# -----------------------------------------------------------------------------
# Send click coordinates to various geoservices to open their maps in browser
# at needed location
#
# Copyright (C) 2008-2010 Barry Rownligson (barry.rowlingson@gmail.com)
#               2014-2017 NextGIS (info@nextgis.com)
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


def classFactory(iface):
    from .main import MainPlugin

    return MainPlugin(iface)

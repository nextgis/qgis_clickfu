# -*- coding: utf-8 -*-

#******************************************************************************
#
# Click-fu
# ---------------------------------------------------------
# Send click coordinates to various geoservices.
#
# Copyright (C) 2008-2010 Barry Rownligson (barry.rowlingson@gmail.com)
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
import os

from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'ui/about.ui'))

class AboutDialog(QDialog, FORM_CLASS):
	def __init__(self, parent=None):
		super(AboutDialog, self).__init__(parent)
		#QDialog.__init__(self)
		# Set up the user interface from Designer.
		self.setupUi(self)
		

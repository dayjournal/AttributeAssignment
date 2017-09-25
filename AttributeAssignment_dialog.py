# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AttributeAssignment
                                 A QGIS plugin
 Easy to assign an attribute on QGIS
                              -------------------
        begin                : 2017-09-18
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Yasunori Kirimoto
        email                : contact@day-journal.com
        license              : GNU General Public License v2.0
 ***************************************************************************/
"""

import os
from PyQt4 import QtGui, uic
from qgis.gui import QgsFieldComboBox, QgsMapLayerComboBox, QgsMapLayerProxyModel
from AttributeAssignment_base import Ui_AttributeAssignment

class AttributeAssignmentDialog(QtGui.QDialog, Ui_AttributeAssignment):
    def __init__(self, parent=None):
        super(AttributeAssignmentDialog, self).__init__(parent)
        self.setupUi(self)
        self.mMapLayerComboBox.setCurrentIndex(-1)        

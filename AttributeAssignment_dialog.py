# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AttributeAssignment
                                 A QGIS plugin
 Easy to assign an attribute on QGIS
                              -------------------
        begin                : 2018-03-14
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Yasunori Kirimoto
        email                : contact@day-journal.com
        license              : GNU General Public License v2.0
 ***************************************************************************/
"""

import os

from PyQt5 import uic, QtWidgets, QtCore
from qgis.gui import *
from .AttributeAssignment_base import Ui_AttributeAssignment

class AttributeAssignmentDialog(QtWidgets.QDialog, Ui_AttributeAssignment):
    def __init__(self, parent=None):
        super(AttributeAssignmentDialog, self).__init__(parent)
        self.setupUi(self)      

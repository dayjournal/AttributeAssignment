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
import warnings

from qgis.PyQt.uic import loadUiType
from PyQt5.QtWidgets import QDialog, QHBoxLayout


def get_ui_class(ui_file):
    """Get UI Python class from .ui file.
       Can be filename.ui or subdirectory/filename.ui
    :param ui_file: The file of the ui in svir.ui
    :type ui_file: str
    """
    rel_file_path = os.path.join(os.path.dirname(__file__), 'ui', ui_file)
    ui_file_path = os.path.abspath(rel_file_path)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return loadUiType(ui_file_path)[0]

DIALOG_UI = get_ui_class('assignment_dialog.ui')

class AttributeAssignmentDialog(QDialog, DIALOG_UI):
    def __init__(self, parent=None):
        super(AttributeAssignmentDialog, self).__init__(parent)
        self.setupUi(self)

        self.mMapLayerComboBox.layerChanged.connect(self.mFieldComboBox.setLayer)
        self.mFieldComboBox.fieldChanged.connect(self.currentFieldChanged)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.mValuePlaceholder.setLayout(self.layout)

        self.wrapper = None
        self.widget = None

    def currentFieldChanged(self, fieldName):
        from qgis.gui import QgsGui
        reg = QgsGui.editorWidgetRegistry()

        if self.widget:
            self.layout.removeWidget(self.widget)
            self.widget = None

        if fieldName:
            fieldIndex = self.mMapLayerComboBox.currentLayer().fields().indexFromName(fieldName)
            self.wrapper = reg.create(self.mMapLayerComboBox.currentLayer(), fieldIndex, None, self.mValuePlaceholder)
            self.widget = self.wrapper.widget()
            self.layout.addWidget(self.widget)
        else:
            self.wrapper = None

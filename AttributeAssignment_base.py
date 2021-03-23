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

from qgsfieldcombobox import QgsFieldComboBox
from qgsmaplayercombobox import QgsMapLayerComboBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AttributeAssignment(object):
    def setupUi(self, AttributeAssignment):
        AttributeAssignment.setObjectName("AttributeAssignment")
        AttributeAssignment.setEnabled(True)
        AttributeAssignment.resize(240, 220)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.formLayout = QtWidgets.QFormLayout(AttributeAssignment)
        self.formLayout.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_layer = QtWidgets.QLabel(AttributeAssignment)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_layer.setFont(font)
        self.label_layer.setObjectName("label_layer")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_layer)
        self.mMapLayerComboBox = QgsMapLayerComboBox(AttributeAssignment)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(
            self.mMapLayerComboBox.sizePolicy().hasHeightForWidth())
        self.mMapLayerComboBox.setSizePolicy(sizePolicy)
        self.mMapLayerComboBox.setAllowEmptyLayer(False)
        self.mMapLayerComboBox.setShowCrs(False)
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.mMapLayerComboBox)
        self.label_field = QtWidgets.QLabel(AttributeAssignment)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_field.setFont(font)
        self.label_field.setObjectName("label_field")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_field)
        self.mFieldComboBox = QgsFieldComboBox(AttributeAssignment)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(
            self.mFieldComboBox.sizePolicy().hasHeightForWidth())
        self.mFieldComboBox.setSizePolicy(sizePolicy)
        self.mFieldComboBox.setObjectName("mFieldComboBox")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.SpanningRole, self.mFieldComboBox)
        self.label_value = QtWidgets.QLabel(AttributeAssignment)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_value.setFont(font)
        self.label_value.setObjectName("label_value")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.label_value)
        self.mValuePlaceholder = QtWidgets.QWidget(AttributeAssignment)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(
            self.mValuePlaceholder.sizePolicy().hasHeightForWidth())
        self.mValuePlaceholder.setSizePolicy(sizePolicy)
        self.mValuePlaceholder.setObjectName("mValuePlaceholder")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.SpanningRole, self.mValuePlaceholder)
        self.label_layer.raise_()
        self.mValuePlaceholder.raise_()
        self.label_field.raise_()
        self.mMapLayerComboBox.raise_()
        self.mFieldComboBox.raise_()
        self.label_value.raise_()
        self.retranslateUi(AttributeAssignment)
        QtCore.QMetaObject.connectSlotsByName(AttributeAssignment)

    def retranslateUi(self, AttributeAssignment):
        _translate = QtCore.QCoreApplication.translate
        AttributeAssignment.setWindowTitle(_translate(
            "AttributeAssignment", "AttributeAssignment"))
        self.label_layer.setText(_translate("AttributeAssignment", "Layer"))
        self.label_field.setText(_translate("AttributeAssignment", "Field"))
        self.label_value.setText(_translate("AttributeAssignment", "Value"))

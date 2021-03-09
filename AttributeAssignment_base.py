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
        AttributeAssignment.resize(240, 220)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.label_layer = QtWidgets.QLabel(AttributeAssignment)
        self.label_layer.setGeometry(QtCore.QRect(20, 15, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_layer.setFont(font)
        self.label_layer.setObjectName("label_layer")
        self.mMapLayerComboBox = QgsMapLayerComboBox(AttributeAssignment)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(20, 35, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mMapLayerComboBox.setFont(font)
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.label_field = QtWidgets.QLabel(AttributeAssignment)
        self.label_field.setGeometry(QtCore.QRect(20, 75, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_field.setFont(font)
        self.label_field.setObjectName("label_field")
        self.label_text = QtWidgets.QLabel(AttributeAssignment)
        self.label_text.setGeometry(QtCore.QRect(20, 140, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_text.setFont(font)
        self.label_text.setObjectName("label_text")
        self.mFieldComboBox = QgsFieldComboBox(AttributeAssignment)
        self.mFieldComboBox.setGeometry(QtCore.QRect(20, 95, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mFieldComboBox.setFont(font)
        self.mFieldComboBox.setObjectName("mFieldComboBox")
        self.lineEdit_text = QtWidgets.QLineEdit(AttributeAssignment)
        self.lineEdit_text.setGeometry(QtCore.QRect(20, 160, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_text.setFont(font)
        self.lineEdit_text.setObjectName("lineEdit_text")
        self.mMapLayerComboBox.layerChanged.connect(
            self.mFieldComboBox.setLayer)
        self.retranslateUi(AttributeAssignment)
        QtCore.QMetaObject.connectSlotsByName(AttributeAssignment)

    def retranslateUi(self, AttributeAssignment):
        _translate = QtCore.QCoreApplication.translate
        AttributeAssignment.setWindowTitle(_translate(
            "AttributeAssignment", "AttributeAssignment"))
        self.label_layer.setText(_translate("AttributeAssignment", "Layer"))
        self.label_field.setText(_translate("AttributeAssignment", "Field"))
        self.label_text.setText(_translate("AttributeAssignment", "Value"))

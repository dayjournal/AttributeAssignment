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

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_AttributeAssignment(object):
    def setupUi(self, AttributeAssignment):
        AttributeAssignment.setObjectName(_fromUtf8("AttributeAssignment"))
        AttributeAssignment.resize(240, 220)
        AttributeAssignment.move(50, 125)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.label_layer = QtWidgets.QLabel(AttributeAssignment)
        self.label_layer.setGeometry(QtCore.QRect(20, 15, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_layer.setFont(font)
        self.label_layer.setObjectName(_fromUtf8("label_layer"))
        self.mMapLayerComboBox = QgsMapLayerComboBox(AttributeAssignment)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(20, 35, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mMapLayerComboBox.setFont(font)
        self.mMapLayerComboBox.setObjectName(_fromUtf8("mMapLayerComboBox"))
        self.label_field = QtWidgets.QLabel(AttributeAssignment)
        self.label_field.setGeometry(QtCore.QRect(20, 75, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_field.setFont(font)
        self.label_field.setObjectName(_fromUtf8("label_field"))
        self.mFieldComboBox = QgsFieldComboBox(AttributeAssignment)
        self.mFieldComboBox.setGeometry(QtCore.QRect(20, 95, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mFieldComboBox.setFont(font)
        self.mFieldComboBox.setObjectName(_fromUtf8("mFieldComboBox"))
        self.label_text = QtWidgets.QLabel(AttributeAssignment)
        self.label_text.setGeometry(QtCore.QRect(20, 140, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_text.setFont(font)
        self.label_text.setObjectName(_fromUtf8("label_text"))
        self.lineEdit_text = QtWidgets.QLineEdit(AttributeAssignment)
        self.lineEdit_text.setGeometry(QtCore.QRect(20, 160, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_text.setFont(font)
        self.lineEdit_text.setObjectName(_fromUtf8("lineEdit_text"))
        self.retranslateUi(AttributeAssignment)
        # QtCore.QObject.connect(self.mMapLayerComboBox, QtCore.SIGNAL(_fromUtf8("layerChanged(QgsMapLayer*)")), self.mFieldComboBox.setLayer)
        self.mMapLayerComboBox.layerChanged.connect(self.mFieldComboBox.setLayer)
        QtCore.QMetaObject.connectSlotsByName(AttributeAssignment)

    def retranslateUi(self, AttributeAssignment):
        AttributeAssignment.setWindowTitle(_translate("AttributeAssignment", u"AttributeAssignment", None))
        self.label_layer.setText(_translate("AttributeAssignment", u"Layer", None))
        self.label_field.setText(_translate("AttributeAssignment", u"Field", None))
        self.label_text.setText(_translate("AttributeAssignment", u"Value", None)) 

from qgis.gui import QgsFieldComboBox, QgsMapLayerComboBox

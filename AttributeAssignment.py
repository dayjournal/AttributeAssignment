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

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *

from .resources import *
from .AttributeAssignment_dialog import AttributeAssignmentDialog

import os
import os.path
import sys
import codecs

QString = str

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class AttributeAssignment:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.dlg = AttributeAssignmentDialog()
        self.dlg.hide()  
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'AttributeAssignment_{}.qm'.format(locale))
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        self.actions = []
        self.menu = self.tr(u'&AttributeAssignment')
        self.toolbar = self.iface.addToolBar(u'AttributeAssignment')
        self.toolbar.setObjectName(u'AttributeAssignment')
    def tr(self, message):
        return QCoreApplication.translate('AttributeAssignment', message)
    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)
        if status_tip is not None:
            action.setStatusTip(status_tip)
        if whats_this is not None:
            action.setWhatsThis(whats_this)
        if add_to_toolbar:
            self.toolbar.addAction(action)
        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)
        self.actions.append(action)
        return action
    def initGui(self):
        icon_path = ':/plugins/AttributeAssignment/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'AttributeAssignment'),
            callback=self.run,
            parent=self.iface.mainWindow())
    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&AttributeAssignment'),
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar
    def run(self):
        self.dlg.show()
        self.dlg.mMapLayerComboBox.setLayer(self.iface.layerTreeView().currentLayer()) 
        self.toolClick = QgsMapToolClick(self.iface, self.canvas, self.dlg)
        self.canvas.setMapTool(self.toolClick)

class QgsMapToolClick(QgsMapTool):
    def __init__(self, iface, canvas, dlg):
        QgsMapTool.__init__(self, canvas)
        self.iface = iface
        self.canvas = canvas
        self.dlg = dlg
    def canvasPressEvent(self, mouseEvent):
        layer = self.dlg.mMapLayerComboBox.currentText()
        fieldname = self.dlg.mFieldComboBox.currentText()
        textvalue = self.dlg.lineEdit_text.text()
        layers = QgsProject.instance().mapLayers()
        for k,v in layers.items():
           if v.name() == layer:
               layer = v
           else:
               pass
        if not layer or layer.type() != QgsMapLayer.VectorLayer:
            QMessageBox.warning(None, u"Error", u"This is not a vector layer.")
            return
        mPosBefore = mouseEvent.mapPoint()
        layerCRS = layer.crs()
        destcrs = self.iface.mapCanvas().mapSettings().destinationCrs()
        Tf = QgsCoordinateTransform(destcrs, layerCRS, QgsProject.instance())
        mPos = Tf.transform(mPosBefore)
        width = 0.00001
        rect = QgsRectangle(mPos.x() - width,
                            mPos.y() - width,
                            mPos.x() + width,
                            mPos.y() + width)
        layer.startEditing()
        rectadd = layer.getFeatures(QgsFeatureRequest().setFilterRect(rect))
        featureid = "";
        for f in rectadd:
            attrs = f.attributes()
            findex = f.fieldNameIndex(fieldname)
            featureid = f.id()
        if featureid != "":
            layer.changeAttributeValue(featureid, findex, textvalue)
        else:
            QMessageBox.warning(None, u"Error", u"This is not a feature.")
        layer.triggerRepaint()

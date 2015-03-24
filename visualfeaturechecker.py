# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VisualFeatureChecker
                                 A QGIS plugin
 test
                              -------------------
        begin                : 2014-10-24
        copyright            : (C) 2014 by me
        email                : me
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from visualfeaturecheckerdialog import VisualFeatureCheckerDialog
import os.path


class VisualFeatureChecker:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'visualfeaturechecker_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = VisualFeatureCheckerDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/visualfeaturechecker/icon.png"),
            u"run loop", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Visual feature checker", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Visual feature checker", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            self.checkLoop()

    def checkLoop(self):
        currentLayer = self.iface.activeLayer()
        for feature in currentLayer.getFeatures():
            currentLayer.removeSelection()
            currentLayer.select(feature.id())
            self.iface.actionPanToSelected().trigger()
            #msgBoxResult = self.continueMessageBox
            #if msgBoxResult != QMessageBox.Ok: return

            self.dlg.show()
            result = self.dlg.exec_()
            if result != 1: return

    def continueMessageBox(self):
        msgBox = QMessageBox()
        msgBox.setText('Continue?')
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msgBox.setWindowModality(Qt::NonModal)
        msgBox.exec_();
        #self.dlg.show()
        #result = self.dlg.exec_()
        #if result != True: return
        #raw_input("waiting...")

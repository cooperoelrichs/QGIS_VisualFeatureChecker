# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_visualfeaturechecker.ui'
#
# Created: Fri Oct 24 14:38:22 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_VisualFeatureChecker(object):
    def setupUi(self, VisualFeatureChecker):
        VisualFeatureChecker.setObjectName(_fromUtf8("VisualFeatureChecker"))
        #VisualFeatureChecker.resize(175, 50)
        VisualFeatureChecker.setGeometry(QtCore.QRect(500, 200, 175, 50))
        self.buttonBox = QtGui.QDialogButtonBox(VisualFeatureChecker)
        self.buttonBox.setGeometry(QtCore.QRect(40, 10, 100, 50))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.label = QtGui.QLabel(VisualFeatureChecker)
        self.label.setText(_fromUtf8("Run the Visual Feature Checker?"))
        self.label.setGeometry(QtCore.QRect(10, 5, 160, 10))
        self.label.setVisible(True)

        self.retranslateUi(VisualFeatureChecker)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VisualFeatureChecker.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VisualFeatureChecker.reject)
        QtCore.QMetaObject.connectSlotsByName(VisualFeatureChecker)

    def retranslateUi(self, VisualFeatureChecker):
        VisualFeatureChecker.setWindowTitle(_translate("VisualFeatureChecker", "VisualFeatureChecker", None))


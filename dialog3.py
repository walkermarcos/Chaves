# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog3.ui'
#
# Created: Fri Dec  4 14:17:08 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Dialog_3(object):
    def setupUi(self, Dialog_3):
        Dialog_3.setObjectName(_fromUtf8("Dialog_3"))
        Dialog_3.resize(363, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_3.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton_2 = QtGui.QPushButton(Dialog_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.retranslateUi(Dialog_3)
        QtCore.QMetaObject.connectSlotsByName(Dialog_3)

    def retranslateUi(self, Dialog_3):
        Dialog_3.setWindowTitle(_translate("Dialog_3", "Dialog", None))
        self.label.setText(_translate("Dialog_3", "TextLabel", None))
        self.pushButton_2.setText(_translate("Dialog_3", "Cancelar", None))
        self.pushButton.setText(_translate("Dialog_3", "OK", None))

import logo_rc

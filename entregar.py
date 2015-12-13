# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entregar.ui'
#
# Created: Sun Dec 13 09:52:00 2015
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

class Ui_Mainentrega(object):
    def setupUi(self, Mainentrega):
        Mainentrega.setObjectName(_fromUtf8("Mainentrega"))
        Mainentrega.resize(480, 414)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Mainentrega.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Mainentrega)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.combo_sal = QtGui.QComboBox(self.centralwidget)
        self.combo_sal.setObjectName(_fromUtf8("combo_sal"))
        self.gridLayout.addWidget(self.combo_sal, 7, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(459, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 3)
        self.but_proc = QtGui.QPushButton(self.centralwidget)
        self.but_proc.setObjectName(_fromUtf8("but_proc"))
        self.gridLayout.addWidget(self.but_proc, 5, 2, 1, 1)
        self.but_canc = QtGui.QPushButton(self.centralwidget)
        self.but_canc.setObjectName(_fromUtf8("but_canc"))
        self.gridLayout.addWidget(self.but_canc, 12, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(459, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 11, 0, 1, 3)
        self.combo_pred = QtGui.QComboBox(self.centralwidget)
        self.combo_pred.setObjectName(_fromUtf8("combo_pred"))
        self.gridLayout.addWidget(self.combo_pred, 3, 1, 1, 2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 28))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.but_ent = QtGui.QPushButton(self.centralwidget)
        self.but_ent.setObjectName(_fromUtf8("but_ent"))
        self.gridLayout.addWidget(self.but_ent, 12, 0, 1, 2)
        Mainentrega.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mainentrega)
        QtCore.QMetaObject.connectSlotsByName(Mainentrega)

    def retranslateUi(self, Mainentrega):
        Mainentrega.setWindowTitle(_translate("Mainentrega", "Entregar Chave", None))
        self.label_3.setText(_translate("Mainentrega", "Sala:", None))
        self.but_proc.setText(_translate("Mainentrega", "Procurar", None))
        self.but_canc.setText(_translate("Mainentrega", "Cancelar", None))
        self.label.setText(_translate("Mainentrega", "<html><head/><body><p><img src=\":/logo/logo_ufpel.png\"/></p></body></html>", None))
        self.label_2.setText(_translate("Mainentrega", "Predio:", None))
        self.label_4.setText(_translate("Mainentrega", "Usuario:", None))
        self.but_ent.setText(_translate("Mainentrega", "Entregar chave", None))

import logo_rc

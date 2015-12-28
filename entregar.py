# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entregar.ui'
#
# Created: Mon Dec 28 15:10:56 2015
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
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(459, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 3)
        self.but_proc = QtGui.QPushButton(self.centralwidget)
        self.but_proc.setObjectName(_fromUtf8("but_proc"))
        self.gridLayout.addWidget(self.but_proc, 6, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.combo_pred = QtGui.QComboBox(self.centralwidget)
        self.combo_pred.setObjectName(_fromUtf8("combo_pred"))
        self.gridLayout.addWidget(self.combo_pred, 4, 1, 1, 2)
        self.but_ent = QtGui.QPushButton(self.centralwidget)
        self.but_ent.setObjectName(_fromUtf8("but_ent"))
        self.gridLayout.addWidget(self.but_ent, 13, 0, 1, 2)
        self.but_canc = QtGui.QPushButton(self.centralwidget)
        self.but_canc.setObjectName(_fromUtf8("but_canc"))
        self.gridLayout.addWidget(self.but_canc, 13, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 28))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 6, 1, 1, 1)
        self.combo_sal = QtGui.QComboBox(self.centralwidget)
        self.combo_sal.setObjectName(_fromUtf8("combo_sal"))
        self.gridLayout.addWidget(self.combo_sal, 8, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(459, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 12, 0, 1, 3)
        self.lista = QtGui.QFrame(self.centralwidget)
        self.lista.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lista.setFrameShadow(QtGui.QFrame.Raised)
        self.lista.setObjectName(_fromUtf8("lista"))
        self.gridLayout_3 = QtGui.QGridLayout(self.lista)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.lista)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.lista)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(self.lista)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.lista, 2, 0, 1, 1)
        Mainentrega.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mainentrega)
        QtCore.QMetaObject.connectSlotsByName(Mainentrega)

    def retranslateUi(self, Mainentrega):
        Mainentrega.setWindowTitle(_translate("Mainentrega", "Entregar Chave", None))
        self.label_3.setText(_translate("Mainentrega", "Sala:", None))
        self.but_proc.setText(_translate("Mainentrega", "Procurar", None))
        self.label.setText(_translate("Mainentrega", "<html><head/><body><p><img src=\":/logo/logo_ufpel.png\"/></p></body></html>", None))
        self.label_4.setText(_translate("Mainentrega", "Usuario:", None))
        self.but_ent.setText(_translate("Mainentrega", "Entregar chave", None))
        self.but_canc.setText(_translate("Mainentrega", "Cancelar", None))
        self.label_2.setText(_translate("Mainentrega", "Predio:", None))
        self.pushButton_2.setText(_translate("Mainentrega", "Cancelar", None))
        self.pushButton.setText(_translate("Mainentrega", "Ok", None))

import logo_rc

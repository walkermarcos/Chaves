# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cad_login.ui'
#
# Created: Thu Dec 10 15:58:06 2015
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

class Ui_Cad_Logins(object):
    def setupUi(self, Cad_Logins):
        Cad_Logins.setObjectName(_fromUtf8("Cad_Logins"))
        Cad_Logins.resize(557, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Cad_Logins.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Cad_Logins)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setInputMask(_fromUtf8(""))
        self.lineEdit_4.setMaxLength(999999999)
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        Cad_Logins.setCentralWidget(self.centralwidget)

        self.retranslateUi(Cad_Logins)
        QtCore.QMetaObject.connectSlotsByName(Cad_Logins)

    def retranslateUi(self, Cad_Logins):
        Cad_Logins.setWindowTitle(_translate("Cad_Logins", "Cadastro Logins", None))
        self.label.setText(_translate("Cad_Logins", "Nome:", None))
        self.label_2.setText(_translate("Cad_Logins", "Nivel:", None))
        self.comboBox_2.setItemText(0, _translate("Cad_Logins", "Nivel 1", None))
        self.comboBox_2.setItemText(1, _translate("Cad_Logins", "Nivel 2", None))
        self.label_3.setText(_translate("Cad_Logins", "Login:", None))
        self.label_4.setText(_translate("Cad_Logins", "Senha:", None))
        self.pushButton_2.setText(_translate("Cad_Logins", "Voltar", None))
        self.pushButton.setText(_translate("Cad_Logins", "OK", None))

import logo_rc

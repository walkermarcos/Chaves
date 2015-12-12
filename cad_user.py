# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cad_user.ui'
#
# Created: Sat Dec 12 08:57:08 2015
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

class Ui_Cadast_user(object):
    def setupUi(self, Cadast_user):
        Cadast_user.setObjectName(_fromUtf8("Cadast_user"))
        Cadast_user.resize(516, 430)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Cadast_user.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Cadast_user)
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
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 2)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 2)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        Cadast_user.setCentralWidget(self.centralwidget)

        self.retranslateUi(Cadast_user)
        QtCore.QMetaObject.connectSlotsByName(Cadast_user)

    def retranslateUi(self, Cadast_user):
        Cadast_user.setWindowTitle(_translate("Cadast_user", "Cadastro Usuários", None))
        self.label.setText(_translate("Cadast_user", "Nome:", None))
        self.label_2.setText(_translate("Cadast_user", "Cod.Barras:", None))
        self.label_3.setText(_translate("Cadast_user", "Email:", None))
        self.label_4.setText(_translate("Cadast_user", "Cpf:", None))
        self.label_5.setText(_translate("Cadast_user", "Tipo:", None))
        self.pushButton_2.setText(_translate("Cadast_user", "Voltar", None))
        self.pushButton.setText(_translate("Cadast_user", "Salvar", None))
        self.comboBox.setItemText(0, _translate("Cadast_user", "Professor", None))
        self.comboBox.setItemText(1, _translate("Cadast_user", "Aluno", None))
        self.comboBox.setItemText(2, _translate("Cadast_user", "Servidor", None))
        self.lineEdit_4.setInputMask(_translate("Cadast_user", "nnn.nnn.nnn-nn ; ", None))

import logo_rc

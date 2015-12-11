# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Thu Dec 10 17:25:37 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(320, 375)
        MainWindow.setMinimumSize(QtCore.QSize(320, 350))
        MainWindow.setMaximumSize(QtCore.QSize(320, 375))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.edit_nome = QtGui.QLineEdit(self.centralwidget)
        self.edit_nome.setMinimumSize(QtCore.QSize(0, 30))
        self.edit_nome.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edit_nome.setObjectName(_fromUtf8("edit_nome"))
        self.verticalLayout.addWidget(self.edit_nome)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.edit_senha = QtGui.QLineEdit(self.centralwidget)
        self.edit_senha.setMinimumSize(QtCore.QSize(0, 30))
        self.edit_senha.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edit_senha.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.edit_senha.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_senha.setObjectName(_fromUtf8("edit_senha"))
        self.verticalLayout.addWidget(self.edit_senha)
        self.but_ok = QtGui.QPushButton(self.centralwidget)
        self.but_ok.setObjectName(_fromUtf8("but_ok"))
        self.verticalLayout.addWidget(self.but_ok)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.but_sair = QtGui.QPushButton(self.centralwidget)
        self.but_sair.setObjectName(_fromUtf8("but_sair"))
        self.verticalLayout.addWidget(self.but_sair)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Projeto Chaves", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/logo/logo_ufpel.png\"/></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Login:", None))
        self.label_2.setText(_translate("MainWindow", "Senha:", None))
        self.but_ok.setText(_translate("MainWindow", "Entrar", None))
        self.pushButton.setText(_translate("MainWindow", "Configurações", None))
        self.but_sair.setText(_translate("MainWindow", "Sair", None))

import logo_rc

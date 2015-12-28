# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conf.ui'
#
# Created: Thu Nov 26 02:34:25 2015
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

class Ui_Conf(object):
    def setupUi(self, Conf):
        Conf.setObjectName(_fromUtf8("Conf"))
        Conf.resize(209, 179)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Conf.setWindowIcon(icon)
        self.widget = QtGui.QWidget(Conf)
        self.widget.setGeometry(QtCore.QRect(0, 10, 205, 161))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget)
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 2)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 3)

        self.retranslateUi(Conf)
        QtCore.QMetaObject.connectSlotsByName(Conf)

    def retranslateUi(self, Conf):
        Conf.setWindowTitle(_translate("Conf", "Configurações", None))
        self.label.setText(_translate("Conf", "Host", None))
        self.lineEdit.setText(_translate("Conf", "localhost", None))
        self.label_2.setText(_translate("Conf", "Database", None))
        self.lineEdit_2.setText(_translate("Conf", "chaves", None))
        self.label_3.setText(_translate("Conf", "User", None))
        self.lineEdit_3.setText(_translate("Conf", "postgres", None))
        self.label_4.setText(_translate("Conf", "Password", None))
        self.lineEdit_4.setText(_translate("Conf", "123456789", None))
        self.pushButton.setText(_translate("Conf", "Ok", None))

import logo_rc

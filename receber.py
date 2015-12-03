# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receber.ui'
#
# Created: Fri Nov 27 09:48:10 2015
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

class Ui_receber(object):
    def setupUi(self, receber):
        receber.setObjectName(_fromUtf8("receber"))
        receber.resize(400, 294)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        receber.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(receber)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.but_rec = QtGui.QPushButton(self.centralwidget)
        self.but_rec.setObjectName(_fromUtf8("but_rec"))
        self.gridLayout.addWidget(self.but_rec, 6, 1, 1, 1)
        self.combo_pred = QtGui.QComboBox(self.centralwidget)
        self.combo_pred.setObjectName(_fromUtf8("combo_pred"))
        self.gridLayout.addWidget(self.combo_pred, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(379, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        self.combo_chav = QtGui.QComboBox(self.centralwidget)
        self.combo_chav.setObjectName(_fromUtf8("combo_chav"))
        self.gridLayout.addWidget(self.combo_chav, 4, 1, 1, 1)
        self.but_canc = QtGui.QPushButton(self.centralwidget)
        self.but_canc.setObjectName(_fromUtf8("but_canc"))
        self.gridLayout.addWidget(self.but_canc, 6, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(379, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 2)
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
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        receber.setCentralWidget(self.centralwidget)

        self.retranslateUi(receber)
        QtCore.QMetaObject.connectSlotsByName(receber)

    def retranslateUi(self, receber):
        receber.setWindowTitle(_translate("receber", "Receber Chave", None))
        self.label_2.setText(_translate("receber", "Chaves em aberto:", None))
        self.but_rec.setText(_translate("receber", "Receber", None))
        self.label.setText(_translate("receber", "<html><head/><body><p><img src=\":/logo/logo_ufpel.png\"/></p></body></html>", None))
        self.but_canc.setText(_translate("receber", "Voltar", None))
        self.label_3.setText(_translate("receber", "Predio:", None))
        self.label_4.setText(_translate("receber", "Sala:", None))

import logo_rc

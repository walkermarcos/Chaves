# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nivel1.ui'
#
# Created: Fri Dec 11 13:08:46 2015
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

class Ui_Nivel1(object):
    def setupUi(self, Nivel1):
        Nivel1.setObjectName(_fromUtf8("Nivel1"))
        Nivel1.setWindowModality(QtCore.Qt.NonModal)
        Nivel1.resize(663, 490)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Nivel1.sizePolicy().hasHeightForWidth())
        Nivel1.setSizePolicy(sizePolicy)
        Nivel1.setMinimumSize(QtCore.QSize(663, 490))
        Nivel1.setMaximumSize(QtCore.QSize(9999999, 9999999))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Nivel1.setWindowIcon(icon)
        Nivel1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(Nivel1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(642, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 5)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777211, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 4)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 5)
        self.but_entr = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_entr.sizePolicy().hasHeightForWidth())
        self.but_entr.setSizePolicy(sizePolicy)
        self.but_entr.setObjectName(_fromUtf8("but_entr"))
        self.gridLayout.addWidget(self.but_entr, 4, 0, 1, 2)
        self.but_rec = QtGui.QPushButton(self.centralwidget)
        self.but_rec.setObjectName(_fromUtf8("but_rec"))
        self.gridLayout.addWidget(self.but_rec, 4, 2, 1, 2)
        self.but_sair = QtGui.QPushButton(self.centralwidget)
        self.but_sair.setObjectName(_fromUtf8("but_sair"))
        self.gridLayout.addWidget(self.but_sair, 4, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 5)
        Nivel1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Nivel1)
        QtCore.QMetaObject.connectSlotsByName(Nivel1)

    def retranslateUi(self, Nivel1):
        Nivel1.setWindowTitle(_translate("Nivel1", "Projeto Chaves Nivel 1", None))
        self.label.setText(_translate("Nivel1", "<html><head/><body><p><img src=\":/logo/logo_ufpel.png\"/></p></body></html>", None))
        self.label_2.setText(_translate("Nivel1", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; vertical-align:sub;\">Projeto </span></p><p align=\"center\"><span style=\" font-size:12pt; vertical-align:sub;\">Chaves </span></p><p align=\"center\"><span style=\" font-size:12pt; vertical-align:sub;\">Ceng</span></p></body></html>", None))
        self.label_3.setText(_translate("Nivel1", "Filtro:", None))
        self.but_entr.setText(_translate("Nivel1", "Entregar chave", None))
        self.but_rec.setText(_translate("Nivel1", "Receber chave", None))
        self.but_sair.setText(_translate("Nivel1", "Sair", None))

import logo_rc

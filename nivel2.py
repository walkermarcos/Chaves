# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nivel2.ui'
#
# Created: Sun Dec  6 11:41:34 2015
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

class Ui_nivel2(object):
    def setupUi(self, nivel2):
        nivel2.setObjectName(_fromUtf8("nivel2"))
        nivel2.resize(596, 566)
        nivel2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/ufpel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        nivel2.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(nivel2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 171))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 151))
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget.setViewMode(QtGui.QListView.ListMode)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(575, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(True)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.retir = QtGui.QWidget()
        self.retir.setGeometry(QtCore.QRect(0, 0, 578, 216))
        self.retir.setObjectName(_fromUtf8("retir"))
        self.gridLayout_2 = QtGui.QGridLayout(self.retir)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.comboBox = QtGui.QComboBox(self.retir)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.retir)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.retir)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.retir)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.retir)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.retir)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.gridLayout_2.addWidget(self.comboBox_4, 1, 5, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.retir)
        self.tableWidget.setMaximumSize(QtCore.QSize(9999999, 999999))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.tableWidget, 4, 0, 1, 6)
        self.pushButton_4 = QtGui.QPushButton(self.retir)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 5, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.retir)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_2, 3, 2, 1, 3)
        self.label_7 = QtGui.QLabel(self.retir)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.retir)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.toolBox.addItem(self.retir, icon, _fromUtf8(""))
        self.cad = QtGui.QWidget()
        self.cad.setGeometry(QtCore.QRect(0, -79, 564, 295))
        self.cad.setObjectName(_fromUtf8("cad"))
        self.gridLayout_4 = QtGui.QGridLayout(self.cad)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tabWidget = QtGui.QTabWidget(self.cad)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(348, 277))
        self.tabWidget.setMaximumSize(QtCore.QSize(9999999, 9999999))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setMaximumSize(QtCore.QSize(9999999, 9999999))
        self.tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab.setAutoFillBackground(True)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_6 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.tableWidget_2 = QtGui.QTableWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableWidget_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tableWidget_2, 1, 0, 1, 4)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_8 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.comboBox_5 = QtGui.QComboBox(self.tab_2)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.gridLayout_5.addWidget(self.comboBox_5, 0, 1, 2, 1)
        self.label_9 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_5.addWidget(self.label_9, 0, 2, 1, 1)
        self.comboBox_6 = QtGui.QComboBox(self.tab_2)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.gridLayout_5.addWidget(self.comboBox_6, 0, 3, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_5.addWidget(self.lineEdit_4, 1, 3, 2, 1)
        self.label_10 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_5.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_5.addWidget(self.label_11, 2, 2, 1, 1)
        self.listWidget_2 = QtGui.QListWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        self.listWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listWidget_2.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.gridLayout_5.addWidget(self.listWidget_2, 3, 0, 1, 2)
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_3.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableWidget_3.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.tableWidget_3, 3, 2, 1, 2)
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_5.addWidget(self.pushButton_5, 4, 0, 1, 2)
        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_5.addWidget(self.pushButton_6, 4, 2, 1, 2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.toolBox.addItem(self.cad, icon, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 578, 216))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.toolBox, 3, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        nivel2.setCentralWidget(self.centralwidget)

        self.retranslateUi(nivel2)
        self.toolBox.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(nivel2)

    def retranslateUi(self, nivel2):
        nivel2.setWindowTitle(_translate("nivel2", "Nivel 2", None))
        self.label.setText(_translate("nivel2", "<html><head/><body><p align=\"justify\"><img src=\":/logo/logo_ufpel.png\"/><span style=\" font-weight:600; font-style:italic;\">Projeto Chaves Ceng</span></p></body></html>", None))
        self.label_5.setText(_translate("nivel2", "Logins ativos:", None))
        self.label_4.setText(_translate("nivel2", "Ano:", None))
        self.label_3.setText(_translate("nivel2", "Mes:", None))
        self.label_2.setText(_translate("nivel2", "Predio:", None))
        self.pushButton_4.setText(_translate("nivel2", "Excluir", None))
        self.comboBox_2.setItemText(0, _translate("nivel2", "Todas", None))
        self.comboBox_2.setItemText(1, _translate("nivel2", "Em aberto", None))
        self.comboBox_2.setItemText(2, _translate("nivel2", "Encerradas", None))
        self.label_7.setText(_translate("nivel2", "Filtrar:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.retir), _translate("nivel2", "Retiradas", None))
        self.label_6.setText(_translate("nivel2", "Filtrar Nome:", None))
        self.pushButton_2.setText(_translate("nivel2", "Novo", None))
        self.pushButton_3.setText(_translate("nivel2", "Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("nivel2", "Usuários", None))
        self.label_8.setText(_translate("nivel2", "Predio:", None))
        self.label_9.setText(_translate("nivel2", "Sala:", None))
        self.label_10.setText(_translate("nivel2", "Usuários:", None))
        self.label_11.setText(_translate("nivel2", "Autorizações:", None))
        self.pushButton_5.setText(_translate("nivel2", "Adicionar", None))
        self.pushButton_6.setText(_translate("nivel2", "Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("nivel2", "Autorizações", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.cad), _translate("nivel2", "Cadastros", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("nivel2", "Page 2", None))
        self.pushButton.setText(_translate("nivel2", "Sair", None))

import logo_rc

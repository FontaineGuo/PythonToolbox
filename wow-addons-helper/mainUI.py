# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 881, 371))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.backupProcessBar = QtWidgets.QProgressBar(self.tab)
        self.backupProcessBar.setGeometry(QtCore.QRect(50, 100, 811, 23))
        self.backupProcessBar.setProperty("value", 24)
        self.backupProcessBar.setObjectName("backupProcessBar")
        self.backupDetailText = QtWidgets.QTextBrowser(self.tab)
        self.backupDetailText.setGeometry(QtCore.QRect(50, 140, 791, 192))
        self.backupDetailText.setObjectName("backupDetailText")
        self.backupPathText = QtWidgets.QTextBrowser(self.tab)
        self.backupPathText.setGeometry(QtCore.QRect(50, 50, 691, 31))
        self.backupPathText.setObjectName("backupPathText")
        self.choseBtnOne = QtWidgets.QPushButton(self.tab)
        self.choseBtnOne.setGeometry(QtCore.QRect(770, 50, 75, 31))
        self.choseBtnOne.setObjectName("choseBtnOne")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 10, 700, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.importDetailText = QtWidgets.QTextBrowser(self.tab_2)
        self.importDetailText.setGeometry(QtCore.QRect(50, 140, 791, 192))
        self.importDetailText.setObjectName("importDetailText")
        self.importProcessBar = QtWidgets.QProgressBar(self.tab_2)
        self.importProcessBar.setGeometry(QtCore.QRect(50, 100, 811, 23))
        self.importProcessBar.setProperty("value", 24)
        self.importProcessBar.setObjectName("importProcessBar")
        self.importPathText = QtWidgets.QTextBrowser(self.tab_2)
        self.importPathText.setGeometry(QtCore.QRect(50, 50, 691, 31))
        self.importPathText.setObjectName("importPathText")
        self.choseBtn2 = QtWidgets.QPushButton(self.tab_2)
        self.choseBtn2.setGeometry(QtCore.QRect(770, 50, 75, 31))
        self.choseBtn2.setObjectName("choseBtn2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 700, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choseBtnOne.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Choose the fold path of /\'World of Warcraft/_retail_\'"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "BackUp"))
        self.choseBtn2.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "Choose the fold path of /\'World of Warcraft/_retail_\'"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Import"))


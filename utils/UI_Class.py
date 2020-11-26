# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(550, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_Information = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Information.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Information.sizePolicy().hasHeightForWidth())
        self.groupBox_Information.setSizePolicy(sizePolicy)
        self.groupBox_Information.setMaximumSize(QtCore.QSize(230, 170))
        self.groupBox_Information.setObjectName("groupBox_Information")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_Information)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_BSP = QtWidgets.QLabel(self.groupBox_Information)
        self.label_BSP.setObjectName("label_BSP")
        self.horizontalLayout.addWidget(self.label_BSP)
        self.lineEdit_BSP = QtWidgets.QLineEdit(self.groupBox_Information)
        self.lineEdit_BSP.setReadOnly(True)
        self.lineEdit_BSP.setObjectName("lineEdit_BSP")
        self.horizontalLayout.addWidget(self.lineEdit_BSP)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_JetPack = QtWidgets.QLabel(self.groupBox_Information)
        self.label_JetPack.setObjectName("label_JetPack")
        self.horizontalLayout_2.addWidget(self.label_JetPack)
        self.lineEdit_JetPack = QtWidgets.QLineEdit(self.groupBox_Information)
        self.lineEdit_JetPack.setReadOnly(True)
        self.lineEdit_JetPack.setObjectName("lineEdit_JetPack")
        self.horizontalLayout_2.addWidget(self.lineEdit_JetPack)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Camera = QtWidgets.QLabel(self.groupBox_Information)
        self.label_Camera.setObjectName("label_Camera")
        self.horizontalLayout_3.addWidget(self.label_Camera)
        self.lineEdit_Camera = QtWidgets.QLineEdit(self.groupBox_Information)
        self.lineEdit_Camera.setTabletTracking(False)
        self.lineEdit_Camera.setReadOnly(True)
        self.lineEdit_Camera.setObjectName("lineEdit_Camera")
        self.horizontalLayout_3.addWidget(self.lineEdit_Camera)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_Support = QtWidgets.QLabel(self.groupBox_Information)
        self.label_Support.setObjectName("label_Support")
        self.horizontalLayout_4.addWidget(self.label_Support)
        self.lineEdit_Support = QtWidgets.QLineEdit(self.groupBox_Information)
        self.lineEdit_Support.setObjectName("lineEdit_Support")
        self.horizontalLayout_4.addWidget(self.lineEdit_Support)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox_Information)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(230, 160))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_gondanpart = QtWidgets.QLabel(self.groupBox)
        self.label_gondanpart.setObjectName("label_gondanpart")
        self.verticalLayout_2.addWidget(self.label_gondanpart)
        self.lineEdit_gondanpart = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_gondanpart.setObjectName("lineEdit_gondanpart")
        self.verticalLayout_2.addWidget(self.lineEdit_gondanpart)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_board = QtWidgets.QLabel(self.groupBox)
        self.label_board.setObjectName("label_board")
        self.verticalLayout_4.addWidget(self.label_board)
        self.lineEdit_board = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_board.setObjectName("lineEdit_board")
        self.verticalLayout_4.addWidget(self.lineEdit_board)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_Test = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Test.setMaximumSize(QtCore.QSize(230, 144))
        self.groupBox_Test.setObjectName("groupBox_Test")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_Test)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_Test)
        self.pushButton_start.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_5.addWidget(self.pushButton_start)
        self.verticalLayout_6.addWidget(self.groupBox_Test)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.groupBox_Status = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Status.setObjectName("groupBox_Status")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_Status)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView = QtWidgets.QTableView(self.groupBox_Status)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout_6.addWidget(self.groupBox_Status)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 584, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menuBar)
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setCheckable(True)
        self.actionDebug.setObjectName("actionDebug")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actionDebug)
        self.menuSetting.addAction(self.actionExit)
        self.menuBar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_Information.setTitle(_translate("MainWindow", "Information"))
        self.label_BSP.setText(_translate("MainWindow", "BSP:"))
        self.lineEdit_BSP.setText(_translate("MainWindow", "wait..."))
        self.label_JetPack.setText(_translate("MainWindow", "JetPack:"))
        self.lineEdit_JetPack.setText(_translate("MainWindow", "wait..."))
        self.label_Camera.setText(_translate("MainWindow", "Camera:"))
        self.lineEdit_Camera.setText(_translate("MainWindow", "wait..."))
        self.label_Support.setText(_translate("MainWindow", "Support:"))
        self.lineEdit_Support.setText(_translate("MainWindow", "Check..."))
        self.groupBox.setTitle(_translate("MainWindow", "Board"))
        self.label_gondanpart.setText(_translate("MainWindow", "工單號碼及品號"))
        self.label_board.setText(_translate("MainWindow", "底板序號"))
        self.groupBox_Test.setTitle(_translate("MainWindow", "Test"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.groupBox_Status.setTitle(_translate("MainWindow", "Status"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scripts\OrtusUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ortus(object):
    def setupUi(self, Ortus):
        Ortus.setObjectName("Ortus")
        Ortus.setEnabled(True)
        Ortus.resize(1000, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Ortus.sizePolicy().hasHeightForWidth())
        Ortus.setSizePolicy(sizePolicy)
        Ortus.setBaseSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(Ortus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setBaseSize(QtCore.QSize(1800, 1500))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 591, 321))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_info = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_info.setObjectName("label_info")
        self.verticalLayout_3.addWidget(self.label_info)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.line_username = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_username.setObjectName("line_username")
        self.verticalLayout_3.addWidget(self.line_username)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.line_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.verticalLayout_3.addWidget(self.line_password)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.button_login = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_login.setObjectName("button_login")
        self.horizontalLayout_8.addWidget(self.button_login)
        self.button_register = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_register.setObjectName("button_register")
        self.horizontalLayout_8.addWidget(self.button_register)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_log = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_log.setObjectName("label_log")
        self.verticalLayout_3.addWidget(self.label_log)
        self.text_log = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.text_log.setObjectName("text_log")
        self.verticalLayout_3.addWidget(self.text_log)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_14.addWidget(self.label_12)
        self.line_keyword = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_keyword.setObjectName("line_keyword")
        self.verticalLayout_14.addWidget(self.line_keyword)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_14.addWidget(self.label_13)
        self.line_output_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_output_password.setObjectName("line_output_password")
        self.verticalLayout_14.addWidget(self.line_output_password)
        self.horizontalLayout_11.addLayout(self.verticalLayout_14)
        self.button_generate_password = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_generate_password.setObjectName("button_generate_password")
        self.horizontalLayout_11.addWidget(self.button_generate_password)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_11.addLayout(self.verticalLayout_13)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.text_passwords = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.text_passwords.sizePolicy().hasHeightForWidth())
        self.text_passwords.setSizePolicy(sizePolicy)
        self.text_passwords.setFrameShape(QtWidgets.QFrame.Box)
        self.text_passwords.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.text_passwords.setObjectName("text_passwords")
        self.horizontalLayout_10.addWidget(self.text_passwords)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        Ortus.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Ortus)
        self.statusBar.setObjectName("statusBar")
        Ortus.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(Ortus)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuExit = QtWidgets.QMenu(self.menuBar)
        self.menuExit.setObjectName("menuExit")
        Ortus.setMenuBar(self.menuBar)
        self.actionFile = QtWidgets.QAction(Ortus)
        self.actionFile.setObjectName("actionFile")
        self.actionExit = QtWidgets.QAction(Ortus)
        self.actionExit.setObjectName("actionExit")
        self.menuExit.addAction(self.actionExit)
        self.menuBar.addAction(self.menuExit.menuAction())

        self.retranslateUi(Ortus)
        QtCore.QMetaObject.connectSlotsByName(Ortus)

    def retranslateUi(self, Ortus):
        _translate = QtCore.QCoreApplication.translate
        Ortus.setWindowTitle(_translate("Ortus", "Ortus"))
        self.label_info.setText(_translate("Ortus", "Ortus - password manager. More info avaliable at: \n"
"https://github.com/danielgafni/Ortus"))
        self.label_10.setText(_translate("Ortus", "Username"))
        self.label_9.setText(_translate("Ortus", "Password"))
        self.button_login.setText(_translate("Ortus", "Log In"))
        self.button_register.setText(_translate("Ortus", "Register"))
        self.label_log.setText(_translate("Ortus", "Output log"))
        self.label_12.setText(_translate("Ortus", "Enter keyword"))
        self.label_13.setText(_translate("Ortus", "Generated password"))
        self.button_generate_password.setText(_translate("Ortus", "Generate"))
        self.menuExit.setTitle(_translate("Ortus", "Action"))
        self.actionFile.setText(_translate("Ortus", "File"))
        self.actionExit.setText(_translate("Ortus", "Exit"))

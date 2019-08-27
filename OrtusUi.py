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
        Ortus.resize(2000, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ortus.sizePolicy().hasHeightForWidth())
        Ortus.setSizePolicy(sizePolicy)
        Ortus.setBaseSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(Ortus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setBaseSize(QtCore.QSize(1800, 1500))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1101, 752))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.line_username = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_username.setFont(font)
        self.line_username.setObjectName("line_username")
        self.verticalLayout.addWidget(self.line_username)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.line_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_password.setFont(font)
        self.line_password.setText("")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.verticalLayout.addWidget(self.line_password)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.button_login = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.horizontalLayout_7.addWidget(self.button_login)
        self.button_register = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_register.setFont(font)
        self.button_register.setObjectName("button_register")
        self.horizontalLayout_7.addWidget(self.button_register)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.text_output_log = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_output_log.sizePolicy().hasHeightForWidth())
        self.text_output_log.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_output_log.setFont(font)
        self.text_output_log.setObjectName("text_output_log")
        self.verticalLayout_2.addWidget(self.text_output_log)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.line_keyword = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_keyword.setFont(font)
        self.line_keyword.setObjectName("line_keyword")
        self.verticalLayout_5.addWidget(self.line_keyword)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.line_output_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_output_password.setFont(font)
        self.line_output_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_output_password.setReadOnly(True)
        self.line_output_password.setObjectName("line_output_password")
        self.verticalLayout_5.addWidget(self.line_output_password)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem)
        self.button_generate_password = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_generate_password.setFont(font)
        self.button_generate_password.setObjectName("button_generate_password")
        self.verticalLayout_9.addWidget(self.button_generate_password)
        self.button_save_password = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_save_password.setFont(font)
        self.button_save_password.setObjectName("button_save_password")
        self.verticalLayout_9.addWidget(self.button_save_password)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.passwords = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwords.setFont(font)
        self.passwords.setObjectName("passwords")
        self.horizontalLayout_4.addWidget(self.passwords)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        Ortus.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Ortus)
        self.statusBar.setObjectName("statusBar")
        Ortus.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(Ortus)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 2000, 25))
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
        self.label.setText(_translate("Ortus", "Ortus - password manager. More info avaliable at: \n"
"https://github.com/danielgafni/Ortus"))
        self.label_3.setText(_translate("Ortus", "Username"))
        self.label_4.setText(_translate("Ortus", "Password"))
        self.button_login.setText(_translate("Ortus", "Log In"))
        self.button_register.setText(_translate("Ortus", "Register"))
        self.label_7.setText(_translate("Ortus", "Output log"))
        self.label_5.setText(_translate("Ortus", "                      Enter keyword                      "))
        self.label_6.setText(_translate("Ortus", "Generated password"))
        self.button_generate_password.setText(_translate("Ortus", "Generate Password"))
        self.button_save_password.setText(_translate("Ortus", "Save Password"))
        self.label_2.setText(_translate("Ortus", "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\\n\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\\n\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.menuExit.setTitle(_translate("Ortus", "Action"))
        self.actionFile.setText(_translate("Ortus", "File"))
        self.actionExit.setText(_translate("Ortus", "Exit"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BasicUI.ui'
#
# Created: Fri Nov 11 17:27:00 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 316)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblFirstName = QtGui.QLabel(self.centralwidget)
        self.lblFirstName.setGeometry(QtCore.QRect(15, 31, 81, 21))
        self.lblFirstName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblFirstName.setObjectName("lblFirstName")
        self.firstNameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setGeometry(QtCore.QRect(105, 31, 201, 20))
        self.firstNameLineEdit.setText("")
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.lastNameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setGeometry(QtCore.QRect(405, 31, 201, 20))
        self.lastNameLineEdit.setText("")
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.lblLastName = QtGui.QLabel(self.centralwidget)
        self.lblLastName.setGeometry(QtCore.QRect(330, 30, 71, 21))
        self.lblLastName.setObjectName("lblLastName")
        self.addressLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.addressLineEdit.setGeometry(QtCore.QRect(105, 71, 501, 20))
        self.addressLineEdit.setText("")
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.lblAddress = QtGui.QLabel(self.centralwidget)
        self.lblAddress.setGeometry(QtCore.QRect(25, 71, 71, 21))
        self.lblAddress.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAddress.setObjectName("lblAddress")
        self.cityLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.cityLineEdit.setGeometry(QtCore.QRect(105, 111, 201, 20))
        self.cityLineEdit.setText("")
        self.cityLineEdit.setObjectName("cityLineEdit")
        self.lblCity = QtGui.QLabel(self.centralwidget)
        self.lblCity.setGeometry(QtCore.QRect(55, 111, 41, 21))
        self.lblCity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCity.setObjectName("lblCity")
        self.lblState = QtGui.QLabel(self.centralwidget)
        self.lblState.setGeometry(QtCore.QRect(355, 111, 41, 21))
        self.lblState.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblState.setObjectName("lblState")
        self.stateLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.stateLineEdit.setGeometry(QtCore.QRect(405, 111, 41, 20))
        self.stateLineEdit.setText("")
        self.stateLineEdit.setObjectName("stateLineEdit")
        self.zipLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.zipLineEdit.setGeometry(QtCore.QRect(505, 111, 101, 20))
        self.zipLineEdit.setObjectName("zipLineEdit")
        self.lblZip = QtGui.QLabel(self.centralwidget)
        self.lblZip.setGeometry(QtCore.QRect(455, 111, 41, 21))
        self.lblZip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblZip.setObjectName("lblZip")
        self.emailLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.emailLineEdit.setGeometry(QtCore.QRect(105, 151, 501, 20))
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.lblEmail = QtGui.QLabel(self.centralwidget)
        self.lblEmail.setGeometry(QtCore.QRect(55, 151, 41, 16))
        self.lblEmail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblEmail.setObjectName("lblEmail")
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(103, 240, 75, 23))
        self.clearButton.setObjectName("clearButton")
        self.saveToTargetButton = QtGui.QPushButton(self.centralwidget)
        self.saveToTargetButton.setEnabled(False)
        self.saveToTargetButton.setGeometry(QtCore.QRect(245, 240, 151, 23))
        self.saveToTargetButton.setObjectName("saveToTargetButton")
        self.loadButton = QtGui.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(460, 240, 75, 23))
        self.loadButton.setObjectName("loadButton")
        self.errorInfoLabel = QtGui.QLabel(self.centralwidget)
        self.errorInfoLabel.setEnabled(True)
        self.errorInfoLabel.setGeometry(QtCore.QRect(110, 190, 491, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.errorInfoLabel.setFont(font)
        self.errorInfoLabel.setText("")
        self.errorInfoLabel.setObjectName("errorInfoLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.firstNameLineEdit, self.lastNameLineEdit)
        MainWindow.setTabOrder(self.lastNameLineEdit, self.addressLineEdit)
        MainWindow.setTabOrder(self.addressLineEdit, self.cityLineEdit)
        MainWindow.setTabOrder(self.cityLineEdit, self.stateLineEdit)
        MainWindow.setTabOrder(self.stateLineEdit, self.zipLineEdit)
        MainWindow.setTabOrder(self.zipLineEdit, self.emailLineEdit)
        MainWindow.setTabOrder(self.emailLineEdit, self.clearButton)
        MainWindow.setTabOrder(self.clearButton, self.saveToTargetButton)
        MainWindow.setTabOrder(self.saveToTargetButton, self.loadButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFirstName.setText(QtGui.QApplication.translate("MainWindow", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLastName.setText(QtGui.QApplication.translate("MainWindow", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAddress.setText(QtGui.QApplication.translate("MainWindow", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCity.setText(QtGui.QApplication.translate("MainWindow", "City", None, QtGui.QApplication.UnicodeUTF8))
        self.lblState.setText(QtGui.QApplication.translate("MainWindow", "State", None, QtGui.QApplication.UnicodeUTF8))
        self.lblZip.setText(QtGui.QApplication.translate("MainWindow", "ZIP", None, QtGui.QApplication.UnicodeUTF8))
        self.lblEmail.setText(QtGui.QApplication.translate("MainWindow", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.saveToTargetButton.setText(QtGui.QApplication.translate("MainWindow", "Save to \"target.xml\"", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate("MainWindow", "Load ...", None, QtGui.QApplication.UnicodeUTF8))


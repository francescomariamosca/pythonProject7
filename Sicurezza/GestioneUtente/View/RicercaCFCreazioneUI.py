# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RicercaCFcreazione.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class RicercaCFCreazioneUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 140)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.ricercacfdip = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ricercacfdip.sizePolicy().hasHeightForWidth())
        self.ricercacfdip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        self.ricercacfdip.setFont(font)
        self.ricercacfdip.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;")
        self.ricercacfdip.setText("")
        self.ricercacfdip.setObjectName("ricercacfdip")
        self.gridLayout.addWidget(self.ricercacfdip, 1, 0, 1, 1)
        self.tornahome = QtWidgets.QCommandLinkButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tornahome.setFont(font)
        self.tornahome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tornahome.setObjectName("tornahome")
        self.gridLayout.addWidget(self.tornahome, 2, 0, 2, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.confermaricercacfdip = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confermaricercacfdip.sizePolicy().hasHeightForWidth())
        self.confermaricercacfdip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confermaricercacfdip.setFont(font)
        self.confermaricercacfdip.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}\n"
"")
        self.confermaricercacfdip.setObjectName("confermaricercacfdip")
        self.gridLayout.addWidget(self.confermaricercacfdip, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Inserisci il CF del dipendente a cui vuoi associare un nuovo utente:"))
        self.tornahome.setText(_translate("MainWindow", "Torna alla Home"))
        self.confermaricercacfdip.setText(_translate("MainWindow", "Conferma"))

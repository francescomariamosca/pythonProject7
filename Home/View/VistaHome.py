# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaHomeFinale.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Campi.Logica.LogicaCampi import LogicaCampi
from Dipendenti.Logica.LogicaDipendente import LogicaDipendente
from Fornitori.Logica.LogicaFornitore import LogicaFornitore
from Liquidita.Logica.LogicaLiquidita import LogicaLiquidita
from Sicurezza.GestioneUtente.Logica.LogicaUtente import LogicaUtente
from Soci.Logica.LogicaSocio import LogicaSocio
from Utility import source



class VistaHome(object):
    def __init__(self, home):
        self.logicaDipendente = LogicaDipendente(home)
        self.logicaSoci = LogicaSocio(home)
        self.logicaUtente = LogicaUtente(home)
        self.logicaCampi = LogicaCampi(home)
        self.logicaLiquidita = LogicaLiquidita(home)
        self.logicaFornitori = LogicaFornitore(home)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 770)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1202, 770))
        MainWindow.setMaximumSize(QtCore.QSize(1202, 770))
        MainWindow.setStyleSheet("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhHiddenText)

        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 280, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 1201, 841))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-image: url(:/newPrefix/camposfondo.png.jpeg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 360, 1081, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dipendenti = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dipendenti.sizePolicy().hasHeightForWidth())
        self.dipendenti.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.dipendenti.setFont(font)
        self.dipendenti.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"")
        self.dipendenti.setObjectName("dipendenti")
        self.gridLayout.addWidget(self.dipendenti, 2, 0, 1, 1)
        self.soci = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soci.sizePolicy().hasHeightForWidth())
        self.soci.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.soci.setFont(font)
        self.soci.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;")
        self.soci.setObjectName("soci")
        self.gridLayout.addWidget(self.soci, 1, 0, 1, 1)
        self.fornitori = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fornitori.sizePolicy().hasHeightForWidth())
        self.fornitori.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.fornitori.setFont(font)
        self.fornitori.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"")
        self.fornitori.setObjectName("fornitori")
        self.gridLayout.addWidget(self.fornitori, 2, 1, 1, 1)
        self.sicurezza = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sicurezza.sizePolicy().hasHeightForWidth())
        self.sicurezza.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sicurezza.setFont(font)
        self.sicurezza.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;")
        self.sicurezza.setObjectName("sicurezza")
        self.gridLayout.addWidget(self.sicurezza, 1, 1, 1, 1)
        self.contabilita = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contabilita.sizePolicy().hasHeightForWidth())
        self.contabilita.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.contabilita.setFont(font)
        self.contabilita.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"")
        self.contabilita.setObjectName("Liquidità")
        self.gridLayout.addWidget(self.contabilita, 0, 1, 1, 1)
        self.campi = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campi.sizePolicy().hasHeightForWidth())
        self.campi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.campi.setFont(font)
        self.campi.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"")
        self.campi.setObjectName("campi")
        self.gridLayout.addWidget(self.campi, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 10, 501, 271))
        self.label_3.setStyleSheet("image: url(:/newPrefix/logo.png.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.label_2.raise_()
        self.gridLayoutWidget.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.passaDipendenti()
        self.passaSoci()
        self.passaCampi()
        self.passaUtenti()
        self.passaLiquidita()
        self.passaFornitori()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Centro Sportivo \"UNIVPM\""))
        self.dipendenti.setText(_translate("MainWindow", "Gestione Dipendenti"))
        self.soci.setText(_translate("MainWindow", "Gestione Soci"))
        self.fornitori.setText(_translate("MainWindow", "Gestione Fornitori"))
        self.sicurezza.setText(_translate("MainWindow", "Sicurezza"))
        self.contabilita.setText(_translate("MainWindow", "Gestione Liquidità"))
        self.campi.setText(_translate("MainWindow", "Prenotazione Campi"))

    def passaDipendenti(self):
        self.dipendenti.clicked.connect(self.logicaDipendente.passaDipendenti)

    def passaSoci(self):

        self.soci.clicked.connect(self.logicaSoci.passaSoci)

    def passaUtenti(self):
        self.sicurezza.clicked.connect(self.logicaUtente.passaGestioneUtenti)

    def passaCampi(self):
        self.campi.clicked.connect(self.logicaCampi.passaCampi)

    def passaLiquidita(self):
        self.contabilita.clicked.connect(self.logicaLiquidita.passaLiquidita)

    def passaFornitori(self):
        self.fornitori.clicked.connect(self.logicaFornitori.passaFornitori)
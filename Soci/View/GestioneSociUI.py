# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GestioneSoci.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class GestioneSociUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tabellasoci = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabellasoci.sizePolicy().hasHeightForWidth())
        self.tabellasoci.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabellasoci.setFont(font)
        self.tabellasoci.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 2px solid white;")
        self.tabellasoci.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabellasoci.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tabellasoci.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabellasoci.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tabellasoci.setObjectName("tabellasoci")
        self.tabellasoci.setColumnCount(7)
        self.tabellasoci.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        item.setFont(font)
        self.tabellasoci.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabellasoci.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabellasoci.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        item.setFont(font)
        self.tabellasoci.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabellasoci.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabellasoci.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabellasoci.setHorizontalHeaderItem(6, item)
        self.verticalLayout_2.addWidget(self.tabellasoci)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        self.tornahome = QtWidgets.QCommandLinkButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tornahome.setFont(font)
        self.tornahome.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tornahome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tornahome.setObjectName("tornahome")
        self.gridLayout.addWidget(self.tornahome, 1, 0, 2, 1)
        self.modificainfosocio = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modificainfosocio.sizePolicy().hasHeightForWidth())
        self.modificainfosocio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        self.modificainfosocio.setFont(font)
        self.modificainfosocio.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}\n"
"")
        self.modificainfosocio.setObjectName("modificainfosocio")
        self.gridLayout.addWidget(self.modificainfosocio, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aggsocio = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aggsocio.sizePolicy().hasHeightForWidth())
        self.aggsocio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.aggsocio.setFont(font)
        self.aggsocio.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}\n"
"")
        self.aggsocio.setObjectName("aggsocio")
        self.horizontalLayout.addWidget(self.aggsocio)
        self.eliminasocio = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eliminasocio.sizePolicy().hasHeightForWidth())
        self.eliminasocio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        self.eliminasocio.setFont(font)
        self.eliminasocio.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: rgb(221, 214, 73);\n"
"border: 3px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 155);\n"
"}\n"
"")
        self.eliminasocio.setObjectName("eliminasocio")
        self.horizontalLayout.addWidget(self.eliminasocio)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ALBO SOCIALE"))
        item = self.tabellasoci.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Socio"))
        item = self.tabellasoci.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "e-mail"))
        item = self.tabellasoci.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CF"))
        item = self.tabellasoci.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tabellasoci.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cognome"))
        item = self.tabellasoci.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tabellasoci.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Data Rinnovo"))
        self.tornahome.setText(_translate("MainWindow", "Torna alla Home"))
        self.modificainfosocio.setText(_translate("MainWindow", "Modifica Info Socio"))
        self.aggsocio.setText(_translate("MainWindow", " + Aggiungi Socio"))
        self.eliminasocio.setText(_translate("MainWindow", " - Elimina Socio"))
        self.tabellasoci.setColumnWidth(0, 300)
        self.tabellasoci.setColumnWidth(1, 300)
        self.tabellasoci.setColumnWidth(2, 300)
        self.tabellasoci.setColumnWidth(3, 300)
        self.tabellasoci.setColumnWidth(4, 300)
        self.tabellasoci.setColumnWidth(5, 300)
        self.tabellasoci.setColumnWidth(6, 300)
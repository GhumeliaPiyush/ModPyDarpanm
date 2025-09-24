# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Protocol_SettingDia.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.resize(600, 420)
        self.setMinimumSize(QSize(0, 420))
        self.setMaximumSize(QSize(600, 420))
        self.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(244, 246, 250);\n"
"}\n"
"    QLabel {\n"
"        padding: 4px;                /* Space inside label */\n"
"        background-color: #F4F6FA;   /* Optional background */\n"
"        color: #1C1C1C;              /* Text color */\n"
"		}")
        self.TitielBar = QWidget(self)
        self.TitielBar.setObjectName(u"TitielBar")
        self.TitielBar.setGeometry(QRect(0, 0, 600, 40))
        self.TitielBar.setStyleSheet(u"background-color: rgb(30, 42, 56);\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(self.TitielBar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 600, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ChParaForm = QWidget(self)
        self.ChParaForm.setObjectName(u"ChParaForm")
        self.ChParaForm.setGeometry(QRect(0, 40, 600, 380))
        self.ChParaForm.setMinimumSize(QSize(0, 380))
        self.ChParaForm.setMaximumSize(QSize(600, 380))
        self.ChParaForm.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"    QLabel {\n"
"        padding: 4px;                /* Space inside label */\n"
"        background-color: #ffffff;   /* Optional background */\n"
"        color: #2E3A48;              /* Text color */\n"
"		}\n"
"QLineEdit, QComboBox {\n"
"    border: 1px solid #E0E0E0;      /* default border */\n"
"    border-radius: 4px;             /* smooth corners */\n"
"    padding: 4px;                   /* inner spacing */\n"
"    background-color: #FFFFFF;      /* clean white bg */\n"
"    color: #1C1C1C;                 /* text color */\n"
"    selection-background-color: #1976D2; /* highlight */\n"
"    selection-color: #FFFFFF;       /* highlighted text */\n"
"  font-family: \"Segoe UI\", \"Roboto\", sans-serif;\n"
"    font-size: 12pt; \n"
"}\n"
"\n"
"QLineEdit:focus, QComboBox:focus {\n"
"    border: 1px solid #1976D2;      /* blue highlight when focused */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #E0E0E0;\n"
"    selec"
                        "tion-background-color: #1976D2;\n"
"    selection-color: #FFFFFF;\n"
"}")
        self.formLayout = QFormLayout(self.ChParaForm)
        self.formLayout.setObjectName(u"formLayout")
        self.chLbl = QLabel(self.ChParaForm)
        self.chLbl.setObjectName(u"chLbl")
        self.chLbl.setMinimumSize(QSize(250, 30))
        self.chLbl.setMaximumSize(QSize(250, 30))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.chLbl.setFont(font1)
        self.chLbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.chLbl)

        self.chanelType_combo = QComboBox(self.ChParaForm)
        self.chanelType_combo.addItem("")
        self.chanelType_combo.addItem("")
        self.chanelType_combo.setObjectName(u"chanelType_combo")
        self.chanelType_combo.setMinimumSize(QSize(0, 30))
        self.chanelType_combo.setMaximumSize(QSize(1000, 3))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.chanelType_combo.setFont(font2)
        self.chanelType_combo.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.chanelType_combo)

        self.portLbl = QLabel(self.ChParaForm)
        self.portLbl.setObjectName(u"portLbl")
        self.portLbl.setMinimumSize(QSize(250, 30))
        self.portLbl.setMaximumSize(QSize(250, 30))
        self.portLbl.setFont(font1)
        self.portLbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.portLbl)

        self.comPort_combo = QComboBox(self.ChParaForm)
        self.comPort_combo.addItem("")
        self.comPort_combo.setObjectName(u"comPort_combo")
        self.comPort_combo.setMinimumSize(QSize(0, 30))
        self.comPort_combo.setMaximumSize(QSize(1000, 30))
        self.comPort_combo.setFont(font2)
        self.comPort_combo.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comPort_combo)

        self.baudLbl = QLabel(self.ChParaForm)
        self.baudLbl.setObjectName(u"baudLbl")
        self.baudLbl.setMinimumSize(QSize(250, 30))
        self.baudLbl.setMaximumSize(QSize(250, 30))
        self.baudLbl.setFont(font1)
        self.baudLbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.baudLbl)

        self.baudRate_combo = QComboBox(self.ChParaForm)
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.addItem("")
        self.baudRate_combo.setObjectName(u"baudRate_combo")
        self.baudRate_combo.setMinimumSize(QSize(0, 30))
        self.baudRate_combo.setMaximumSize(QSize(1000, 30))
        self.baudRate_combo.setFont(font2)
        self.baudRate_combo.setStyleSheet(u"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.baudRate_combo)

        self.dbLbl = QLabel(self.ChParaForm)
        self.dbLbl.setObjectName(u"dbLbl")
        self.dbLbl.setMinimumSize(QSize(250, 30))
        self.dbLbl.setMaximumSize(QSize(250, 30))
        self.dbLbl.setFont(font1)
        self.dbLbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.dbLbl)

        self.dataBit_combo = QComboBox(self.ChParaForm)
        self.dataBit_combo.addItem("")
        self.dataBit_combo.addItem("")
        self.dataBit_combo.addItem("")
        self.dataBit_combo.setObjectName(u"dataBit_combo")
        self.dataBit_combo.setMinimumSize(QSize(0, 30))
        self.dataBit_combo.setMaximumSize(QSize(1000, 30))
        self.dataBit_combo.setFont(font2)
        self.dataBit_combo.setStyleSheet(u"")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.dataBit_combo)

        self.StpLbl = QLabel(self.ChParaForm)
        self.StpLbl.setObjectName(u"StpLbl")
        self.StpLbl.setMinimumSize(QSize(250, 30))
        self.StpLbl.setMaximumSize(QSize(250, 30))
        self.StpLbl.setFont(font1)
        self.StpLbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.StpLbl)

        self.stopBit_combo = QComboBox(self.ChParaForm)
        self.stopBit_combo.addItem("")
        self.stopBit_combo.addItem("")
        self.stopBit_combo.addItem("")
        self.stopBit_combo.setObjectName(u"stopBit_combo")
        self.stopBit_combo.setMinimumSize(QSize(0, 30))
        self.stopBit_combo.setMaximumSize(QSize(1000, 30))
        self.stopBit_combo.setFont(font2)
        self.stopBit_combo.setStyleSheet(u"")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.stopBit_combo)

        self.PariLbl = QLabel(self.ChParaForm)
        self.PariLbl.setObjectName(u"PariLbl")
        self.PariLbl.setMinimumSize(QSize(250, 30))
        self.PariLbl.setMaximumSize(QSize(250, 30))
        self.PariLbl.setFont(font1)
        self.PariLbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.PariLbl)

        self.parityCombo = QComboBox(self.ChParaForm)
        self.parityCombo.addItem("")
        self.parityCombo.addItem("")
        self.parityCombo.addItem("")
        self.parityCombo.addItem("")
        self.parityCombo.setObjectName(u"parityCombo")
        self.parityCombo.setMinimumSize(QSize(0, 30))
        self.parityCombo.setMaximumSize(QSize(1000, 30))
        self.parityCombo.setFont(font2)
        self.parityCombo.setStyleSheet(u"")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.parityCombo)

        self.ipLbl = QLabel(self.ChParaForm)
        self.ipLbl.setObjectName(u"ipLbl")
        self.ipLbl.setMinimumSize(QSize(250, 30))
        self.ipLbl.setMaximumSize(QSize(250, 30))
        self.ipLbl.setFont(font1)
        self.ipLbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.ipLbl)

        self.IpEdit = QLineEdit(self.ChParaForm)
        self.IpEdit.setObjectName(u"IpEdit")
        self.IpEdit.setMinimumSize(QSize(0, 30))
        self.IpEdit.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.IpEdit)

        self.SaveProtocol_button = QPushButton(self.ChParaForm)
        self.SaveProtocol_button.setObjectName(u"SaveProtocol_button")
        self.SaveProtocol_button.setMinimumSize(QSize(181, 45))
        self.SaveProtocol_button.setMaximumSize(QSize(181, 45))
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.SaveProtocol_button.setFont(font3)
        self.SaveProtocol_button.setStyleSheet(u"QPushButton{\n"
"	background-color:green;\n"
"	color:white;\n"
"	border:None;\n"
"	border-radius:5px;\n"
"	font-weight:bold;\n"
"	height:45px;\n"
"}")
        self.SaveProtocol_button.setCheckable(True)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.SaveProtocol_button)

        self.cancle_channel = QPushButton(self.ChParaForm)
        self.cancle_channel.setObjectName(u"cancle_channel")
        self.cancle_channel.setMinimumSize(QSize(181, 45))
        self.cancle_channel.setMaximumSize(QSize(181, 45))
        self.cancle_channel.setFont(font3)
        self.cancle_channel.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(144, 144, 144);\n"
"	color:white;\n"
"	border:None;\n"
"	border-radius:5px;\n"
"	font-weight:bold;\n"
"	height:45px;\n"
"}")
        self.cancle_channel.setCheckable(True)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.cancle_channel)

        self.slaveLbl = QLabel(self.ChParaForm)
        self.slaveLbl.setObjectName(u"slaveLbl")
        self.slaveLbl.setMinimumSize(QSize(250, 30))
        self.slaveLbl.setMaximumSize(QSize(250, 30))
        self.slaveLbl.setFont(font1)
        self.slaveLbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.slaveLbl)

        self.slaveId_combo = QComboBox(self.ChParaForm)
        self.slaveId_combo.addItem("")
        self.slaveId_combo.setObjectName(u"slaveId_combo")
        self.slaveId_combo.setMinimumSize(QSize(0, 30))
        self.slaveId_combo.setMaximumSize(QSize(1000, 30))
        self.slaveId_combo.setFont(font2)
        self.slaveId_combo.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.slaveId_combo)


        self.retranslateUi()
        self.cancle_channel.toggled.connect(self.close)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Update Protocol", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Communication Protocol Setting", None))
        self.chLbl.setText(QCoreApplication.translate("Dialog", u"Prorocol Type:", None))
        self.chanelType_combo.setItemText(0, QCoreApplication.translate("Dialog", u"MODBUS-RTU", None))
        self.chanelType_combo.setItemText(1, QCoreApplication.translate("Dialog", u"MODBUS-TCP", None))

        self.portLbl.setText(QCoreApplication.translate("Dialog", u"Port :", None))
        # self.comPort_combo.setItemText(0, "")
        com_port = []
        for i in range(1,256):
                val = "COM"+str(i)
                com_port.append(val)
        self.comPort_combo.addItems(com_port)

        self.baudLbl.setText(QCoreApplication.translate("Dialog", u"Baud Rate :", None))
        self.baudRate_combo.setItemText(0, "")
        self.baudRate_combo.setItemText(1, QCoreApplication.translate("Dialog", u"300", None))
        self.baudRate_combo.setItemText(2, QCoreApplication.translate("Dialog", u"600", None))
        self.baudRate_combo.setItemText(3, QCoreApplication.translate("Dialog", u"1200", None))
        self.baudRate_combo.setItemText(4, QCoreApplication.translate("Dialog", u"2400", None))
        self.baudRate_combo.setItemText(5, QCoreApplication.translate("Dialog", u"4800", None))
        self.baudRate_combo.setItemText(6, QCoreApplication.translate("Dialog", u"7200", None))
        self.baudRate_combo.setItemText(7, QCoreApplication.translate("Dialog", u"9600", None))
        self.baudRate_combo.setItemText(8, QCoreApplication.translate("Dialog", u"14400", None))
        self.baudRate_combo.setItemText(9, QCoreApplication.translate("Dialog", u"19200", None))
        self.baudRate_combo.setItemText(10, QCoreApplication.translate("Dialog", u"38400", None))
        self.baudRate_combo.setItemText(11, QCoreApplication.translate("Dialog", u"57600", None))
        self.baudRate_combo.setItemText(12, QCoreApplication.translate("Dialog", u"115200", None))
        self.baudRate_combo.setItemText(13, QCoreApplication.translate("Dialog", u"230400", None))
        self.baudRate_combo.setItemText(14, QCoreApplication.translate("Dialog", u"460800", None))
        self.baudRate_combo.setItemText(15, QCoreApplication.translate("Dialog", u"921600", None))

        self.dbLbl.setText(QCoreApplication.translate("Dialog", u"Data Bits :", None))
        self.dataBit_combo.setItemText(0, "")
        self.dataBit_combo.setItemText(1, QCoreApplication.translate("Dialog", u"7", None))
        self.dataBit_combo.setItemText(2, QCoreApplication.translate("Dialog", u"8", None))

        self.StpLbl.setText(QCoreApplication.translate("Dialog", u"Stop Bits :", None))
        self.stopBit_combo.setItemText(0, "")
        self.stopBit_combo.setItemText(1, QCoreApplication.translate("Dialog", u"1", None))
        self.stopBit_combo.setItemText(2, QCoreApplication.translate("Dialog", u"2", None))

        self.PariLbl.setText(QCoreApplication.translate("Dialog", u"Parity :", None))
        self.parityCombo.setItemText(0, "")
        self.parityCombo.setItemText(1, QCoreApplication.translate("Dialog", u"E", None))
        self.parityCombo.setItemText(2, QCoreApplication.translate("Dialog", u"O", None))
        self.parityCombo.setItemText(3, QCoreApplication.translate("Dialog", u"N", None))

        self.ipLbl.setText(QCoreApplication.translate("Dialog", u"I/p Add. Port :", None))
        self.SaveProtocol_button.setText(QCoreApplication.translate("Dialog", u"Save Channel", None))
        self.cancle_channel.setText(QCoreApplication.translate("Dialog", u"Cancle", None))
        self.slaveLbl.setText(QCoreApplication.translate("Dialog", u"Slave Id :", None))
        # self.slaveId_combo.setItemText(0, "")
        id_add = []
        for i in range(1,256):
                id_add.append(str(i))
        self.slaveId_combo.addItems(id_add)
        
        self.chanelType_combo.currentTextChanged.connect(self.update_fields)
        
        # Set default state
        self.update_fields("MODBUS-RTU")
    # retranslateUi
    
    def update_fields(self, text):
        if text == "MODBUS-RTU":
            self.comPort_combo.show()
            self.baudRate_combo.show()
            self.dataBit_combo.show()
            self.parityCombo.show()
            self.stopBit_combo.show()
            self.IpEdit.hide()
     
        else:  # Modbus-TCP
            self.comPort_combo.hide()
            self.baudRate_combo.hide()
            self.dataBit_combo.hide()
            self.parityCombo.hide()
            self.stopBit_combo.hide()
            self.IpEdit.show()



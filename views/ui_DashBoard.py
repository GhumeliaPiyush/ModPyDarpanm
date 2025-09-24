# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashBoard.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QWidget)
from UI import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet(u"background-color: rgb(244, 246, 250);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.SideBar_frame = QFrame(self.centralwidget)
        self.SideBar_frame.setObjectName(u"SideBar_frame")
        self.SideBar_frame.setGeometry(QRect(0, 80, 250, 660))
        self.SideBar_frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 170, 255);\n"
"	background-color: rgb(47, 59, 82);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(62, 76, 109);\n"
"	text-align:center;\n"
"	height:50px;\n"
"	border:None;\n"
"	padding-left:5px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #4DD0E1;\n"
"	color:#1f95ef;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
" QComboBox {\n"
"    border: 1px solid #E0E0E0;      /* default border */\n"
"    border-radius: 4px;             /* smooth corners */\n"
"    padding: 4px;                   /* inner spacing */\n"
"    background-color: rgb(62, 76, 109);      /* clean white bg */\n"
"    color: #FFFFFF;                 /* text color */\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #E0E0E0;\n"
"    background-color: rgb(62, 76, 109);  /* dark blue-gray background */\n"
"    font-family: \"Segoe UI\", \"Roboto\", sans-serif;\n"
"    font-size: 12pt;\n"
"    color: #F4F6FA;                      /* default text color (light) *"
                        "/\n"
"    selection-background-color: #4DD0E1; /* teal highlight */\n"
"    selection-color: #1f95ef;            /* text color for focused item */\n"
"}\n"
"\n"
"/* Optional: spacing between dropdown items */\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 6px 10px;\n"
"}\n"
"")
        self.SideBar_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SideBar_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Settings_btn = QPushButton(self.SideBar_frame)
        self.Settings_btn.setObjectName(u"Settings_btn")
        self.Settings_btn.setGeometry(QRect(20, 50, 210, 50))
        self.Settings_btn.setMaximumSize(QSize(210, 50))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        self.Settings_btn.setFont(font)
        self.Settings_btn.setCheckable(True)
        self.Connect_btn = QPushButton(self.SideBar_frame)
        self.Connect_btn.setObjectName(u"Connect_btn")
        self.Connect_btn.setGeometry(QRect(20, 350, 210, 50))
        self.Connect_btn.setMaximumSize(QSize(210, 50))
        self.Connect_btn.setFont(font)
        self.Connect_btn.setCheckable(True)
        self.RegisterCombo = QComboBox(self.SideBar_frame)
        self.RegisterCombo.addItem("")
        self.RegisterCombo.addItem("")
        self.RegisterCombo.setObjectName(u"RegisterCombo")
        self.RegisterCombo.setGeometry(QRect(20, 125, 210, 50))
        self.RegisterCombo.setMinimumSize(QSize(210, 50))
        self.RegisterCombo.setMaximumSize(QSize(210, 50))
        self.RegisterCombo.setFont(font)
        self.EndienCombo = QComboBox(self.SideBar_frame)
        self.EndienCombo.addItem("")
        self.EndienCombo.addItem("")
        self.EndienCombo.setObjectName(u"EndienCombo")
        self.EndienCombo.setGeometry(QRect(20, 200, 210, 50))
        self.EndienCombo.setMinimumSize(QSize(210, 50))
        self.EndienCombo.setMaximumSize(QSize(210, 50))
        self.EndienCombo.setFont(font)
        self.DataTypeCombo = QComboBox(self.SideBar_frame)
        self.DataTypeCombo.addItem("")
        self.DataTypeCombo.addItem("")
        self.DataTypeCombo.addItem("")
        self.DataTypeCombo.addItem("")
        self.DataTypeCombo.addItem("")
        self.DataTypeCombo.setObjectName(u"DataTypeCombo")
        self.DataTypeCombo.setGeometry(QRect(20, 275, 210, 50))
        self.DataTypeCombo.setMinimumSize(QSize(210, 50))
        self.DataTypeCombo.setMaximumSize(QSize(210, 50))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.DataTypeCombo.setFont(font1)
        self.DataTypeCombo.setStyleSheet(u"")
        self.Header_frame = QFrame(self.centralwidget)
        self.Header_frame.setObjectName(u"Header_frame")
        self.Header_frame.setGeometry(QRect(0, 0, 1280, 80))
        self.Header_frame.setStyleSheet(u"background-color: rgb(30, 42, 56);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 20pt \"Arial\";")
        self.Header_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Header_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Title = QLabel(self.Header_frame)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(420, 14, 411, 56))
        self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Logo = QLabel(self.Header_frame)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(0, 0, 302, 80))
        self.Logo.setPixmap(QPixmap(u":/icons/logo.png"))
        self.Logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.AlarmFrm = QFrame(self.centralwidget)
        self.AlarmFrm.setObjectName(u"AlarmFrm")
        self.AlarmFrm.setGeometry(QRect(0, 740, 1280, 60))
        self.AlarmFrm.setStyleSheet(u"background-color: rgb(183, 28, 28);\n"
"color: rgb(255, 235, 59);\n"
"font: 500 14pt \"Roboto Medium\";")
        self.AlarmFrm.setFrameShape(QFrame.Shape.StyledPanel)
        self.AlarmFrm.setFrameShadow(QFrame.Shadow.Raised)
        self.AlarmWid = QWidget(self.AlarmFrm)
        self.AlarmWid.setObjectName(u"AlarmWid")
        self.AlarmWid.setGeometry(QRect(0, 0, 1280, 60))
        self.AlarmWid.setMinimumSize(QSize(1280, 60))
        self.AlarmWid.setMaximumSize(QSize(1280, 60))
        self.AlarmWid.setStyleSheet(u"QWidget{\n"
"background-color: rgb(183, 28, 28);\n"
"color: rgb(255, 235, 59);\n"
"font: 500 14pt \"Roboto Medium\";\n"
"}")
        self.toolbar_widg = QWidget(self.centralwidget)
        self.toolbar_widg.setObjectName(u"toolbar_widg")
        self.toolbar_widg.setGeometry(QRect(250, 80, 1030, 120))
        self.toolbar_widg.setStyleSheet(u"Qwidget{\n"
"border: 1px solid #2E3A48;   /* Border color */\n"
"        border-radius: 4px;          /* Rounded corners */}")
        self.Lable_1 = QLabel(self.toolbar_widg)
        self.Lable_1.setObjectName(u"Lable_1")
        self.Lable_1.setGeometry(QRect(10, 10, 140, 40))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        self.Lable_1.setFont(font2)
        self.Lable_1.setStyleSheet(u"color: rgb(46, 58, 72);")
        self.Lable_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.AddDisp = QLabel(self.toolbar_widg)
        self.AddDisp.setObjectName(u"AddDisp")
        self.AddDisp.setGeometry(QRect(160, 10, 180, 40))
        self.AddDisp.setFont(font2)
        self.AddDisp.setStyleSheet(u"    QLabel {\n"
"        border: 1px solid #2E3A48;   /* Border color */\n"
"        border-radius: 4px;          /* Rounded corners */\n"
"        padding: 4px;                /* Space inside label */\n"
"        background-color: #F4F6FA;   /* Optional background */\n"
"        color: #1C1C1C;              /* Text color */\n"
"		}")
        self.AddDisp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.RngDisp = QLabel(self.toolbar_widg)
        self.RngDisp.setObjectName(u"RngDisp")
        self.RngDisp.setGeometry(QRect(160, 60, 180, 40))
        self.RngDisp.setFont(font2)
        self.RngDisp.setStyleSheet(u"    QLabel {\n"
"        border: 1px solid #2E3A48;   /* Border color */\n"
"        border-radius: 4px;          /* Rounded corners */\n"
"        padding: 4px;                /* Space inside label */\n"
"        background-color: #F4F6FA;   /* Optional background */\n"
"        color: #1C1C1C;              /* Text color */\n"
"		}")
        self.RngDisp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Lable_2 = QLabel(self.toolbar_widg)
        self.Lable_2.setObjectName(u"Lable_2")
        self.Lable_2.setGeometry(QRect(10, 60, 140, 40))
        self.Lable_2.setFont(font2)
        self.Lable_2.setStyleSheet(u"color: rgb(46, 58, 72);")
        self.Lable_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Lable_6 = QLabel(self.toolbar_widg)
        self.Lable_6.setObjectName(u"Lable_6")
        self.Lable_6.setGeometry(QRect(350, 10, 140, 40))
        self.Lable_6.setFont(font2)
        self.Lable_6.setStyleSheet(u"color: rgb(46, 58, 72);")
        self.Lable_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ChDisp = QLabel(self.toolbar_widg)
        self.ChDisp.setObjectName(u"ChDisp")
        self.ChDisp.setGeometry(QRect(500, 60, 180, 40))
        self.ChDisp.setFont(font2)
        self.ChDisp.setStyleSheet(u"    QLabel {\n"
"        border: 1px solid #2E3A48;   /* Border color */\n"
"        border-radius: 4px;          /* Rounded corners */\n"
"        padding: 4px;                /* Space inside label */\n"
"        background-color: #F4F6FA;   /* Optional background */\n"
"        color: #1C1C1C;              /* Text color */\n"
"		}")
        self.ChDisp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.SlaveDisp = QLabel(self.toolbar_widg)
        self.SlaveDisp.setObjectName(u"SlaveDisp")
        self.SlaveDisp.setGeometry(QRect(500, 10, 180, 40))
        self.SlaveDisp.setFont(font2)
        self.SlaveDisp.setStyleSheet(u"    QLabel {\n"
"        border: 1px solid #2E3A48;   /* Border color */\n"
"        border-radius: 4px;          /* Rounded corners */\n"
"        padding: 4px;                /* Space inside label */\n"
"        background-color: #F4F6FA;   /* Optional background */\n"
"        color: #1C1C1C;              /* Text color */\n"
"		}")
        self.SlaveDisp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Lable_5 = QLabel(self.toolbar_widg)
        self.Lable_5.setObjectName(u"Lable_5")
        self.Lable_5.setGeometry(QRect(350, 60, 140, 40))
        self.Lable_5.setFont(font2)
        self.Lable_5.setStyleSheet(u"color: rgb(46, 58, 72);")
        self.Lable_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Lable_7 = QLabel(self.toolbar_widg)
        self.Lable_7.setObjectName(u"Lable_7")
        self.Lable_7.setGeometry(QRect(690, 10, 140, 40))
        self.Lable_7.setFont(font2)
        self.Lable_7.setStyleSheet(u"color: rgb(46, 58, 72);")
        self.Lable_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Lable_8 = QLabel(self.toolbar_widg)
        self.Lable_8.setObjectName(u"Lable_8")
        self.Lable_8.setGeometry(QRect(690, 60, 140, 40))
        self.Lable_8.setFont(font2)
        self.Lable_8.setStyleSheet(u"color: rgb(46, 58, 72);")
        self.Lable_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.FrmtDisp = QLabel(self.toolbar_widg)
        self.FrmtDisp.setObjectName(u"FrmtDisp")
        self.FrmtDisp.setGeometry(QRect(840, 60, 180, 40))
        self.FrmtDisp.setFont(font2)
        self.FrmtDisp.setStyleSheet(u"    QLabel {\n"
"        border: 1px solid #2E3A48;   /* Border color */\n"
"        border-radius: 4px;          /* Rounded corners */\n"
"        padding: 4px;                /* Space inside label */\n"
"        background-color: #F4F6FA;   /* Optional background */\n"
"        color: #1C1C1C;              /* Text color */\n"
"		}")
        self.FrmtDisp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.PortDisp = QLabel(self.toolbar_widg)
        self.PortDisp.setObjectName(u"PortDisp")
        self.PortDisp.setGeometry(QRect(840, 10, 180, 40))
        self.PortDisp.setFont(font2)
        self.PortDisp.setStyleSheet(u"    QLabel {\n"
"        border: 1px solid #2E3A48;   /* Border color */\n"
"        border-radius: 4px;          /* Rounded corners */\n"
"        padding: 4px;                /* Space inside label */\n"
"        background-color: #F4F6FA;   /* Optional background */\n"
"        color: #1C1C1C;              /* Text color */\n"
"		}")
        self.PortDisp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.DispScroll = QScrollArea(self.centralwidget)
        self.DispScroll.setObjectName(u"DispScroll")
        self.DispScroll.setGeometry(QRect(250, 200, 1030, 540))
        self.DispScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.DispScroll.setWidgetResizable(True)
        self.DispScrollWidget = QWidget()
        self.DispScrollWidget.setObjectName(u"DispScrollWidget")
        self.DispScrollWidget.setGeometry(QRect(0, 0, 1028, 521))
        self.DispScroll.setWidget(self.DispScrollWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setMinimumSize(QSize(1280,800))
        MainWindow.setMaximumSize(QSize(1280, 800))
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Settings_btn.setText(QCoreApplication.translate("MainWindow", u"Select Protocol", None))
        self.Connect_btn.setText(QCoreApplication.translate("MainWindow", u"Link Off", None))
        # self.RegisterCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Coil Status Reg.", None))
        # self.RegisterCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Input Status Reg.", None))
        self.RegisterCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Input Registers", None))
        self.RegisterCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Holding Registers", None))

        self.EndienCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Big Endian ", None))
        self.EndienCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Little Endian", None))

        self.DataTypeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"INT", None))
        self.DataTypeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"UINT", None))
        self.DataTypeCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"LONG", None))
        self.DataTypeCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"ULONG", None))
        self.DataTypeCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"FLOAT", None))

        self.Title.setText(QCoreApplication.translate("MainWindow", u"DASH BOARD", None))
        self.Logo.setText("")
        self.Lable_1.setText(QCoreApplication.translate("MainWindow", u"Starting Add. :", None))
        self.AddDisp.setText(QCoreApplication.translate("MainWindow", u"#######", None))
        self.RngDisp.setText(QCoreApplication.translate("MainWindow", u"#######", None))
        self.Lable_2.setText(QCoreApplication.translate("MainWindow", u"Dispaly Range :", None))
        self.Lable_6.setText(QCoreApplication.translate("MainWindow", u"Slave Id :", None))
        self.ChDisp.setText(QCoreApplication.translate("MainWindow", u"#######", None))
        self.SlaveDisp.setText(QCoreApplication.translate("MainWindow", u"#######", None))
        self.Lable_5.setText(QCoreApplication.translate("MainWindow", u"Protocol Used :", None))
        self.Lable_7.setText(QCoreApplication.translate("MainWindow", u"Port / Ip Add. :", None))
        self.Lable_8.setText(QCoreApplication.translate("MainWindow", u"Data Formate :", None))
        self.FrmtDisp.setText(QCoreApplication.translate("MainWindow", u"#######", None))
        self.PortDisp.setText(QCoreApplication.translate("MainWindow", u"#######", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrometercom_gui2.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QStackedWidget, QWidget)
import graphics.buttons_rc

class Ui_speccom_mainwin(object):
    def setupUi(self, speccom_mainwin):
        if not speccom_mainwin.objectName():
            speccom_mainwin.setObjectName(u"speccom_mainwin")
        speccom_mainwin.resize(458, 645)
        speccom_mainwin.setStyleSheet(u"button->setStyleSheet(\"border-image:url(:/icons/arrow_l.png);\");")
        self.frame = QFrame(speccom_mainwin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 451, 621))
        self.frame.setStyleSheet(u"background-color: rgb(50, 49, 52);\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(20, 10, 231, 31))
        self.label.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.horizontalSlider_bright = QSlider(self.frame)
        self.horizontalSlider_bright.setObjectName(u"horizontalSlider_bright")
        self.horizontalSlider_bright.setGeometry(QRect(100, 140, 301, 22))
        self.horizontalSlider_bright.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_bright.setMinimum(0)
        self.horizontalSlider_bright.setValue(0)
        self.horizontalSlider_bright.setOrientation(Qt.Horizontal)
        self.horizontalSlider_bright.setInvertedAppearance(False)
        self.horizontalSlider_gain = QSlider(self.frame)
        self.horizontalSlider_gain.setObjectName(u"horizontalSlider_gain")
        self.horizontalSlider_gain.setGeometry(QRect(100, 170, 301, 20))
        self.horizontalSlider_gain.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_gain.setMinimum(1)
        self.horizontalSlider_gain.setMaximum(100)
        self.horizontalSlider_gain.setValue(1)
        self.horizontalSlider_gain.setOrientation(Qt.Horizontal)
        self.horizontalSlider_gain.setInvertedAppearance(False)
        self.horizontalSlider_exposure = QSlider(self.frame)
        self.horizontalSlider_exposure.setObjectName(u"horizontalSlider_exposure")
        self.horizontalSlider_exposure.setGeometry(QRect(100, 110, 301, 22))
        self.horizontalSlider_exposure.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_exposure.setMinimum(-14)
        self.horizontalSlider_exposure.setMaximum(0)
        self.horizontalSlider_exposure.setValue(-8)
        self.horizontalSlider_exposure.setSliderPosition(-8)
        self.horizontalSlider_exposure.setOrientation(Qt.Horizontal)
        self.horizontalSlider_exposure.setInvertedAppearance(False)
        self.horizontalSlider_exposure.setInvertedControls(False)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 45, 481, 51))
        self.frame_2.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.comboBox_camport = QComboBox(self.frame_2)
        self.comboBox_camport.setObjectName(u"comboBox_camport")
        self.comboBox_camport.setGeometry(QRect(110, 15, 111, 22))
        self.comboBox_camport.setStyleSheet(u"color: rgb(220,220,220)\n"
"")
        self.pushButton_comrefresh = QPushButton(self.frame_2)
        self.pushButton_comrefresh.setObjectName(u"pushButton_comrefresh")
        self.pushButton_comrefresh.setGeometry(QRect(230, 10, 101, 31))
        self.pushButton_comrefresh.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_comconnect = QPushButton(self.frame_2)
        self.pushButton_comconnect.setObjectName(u"pushButton_comconnect")
        self.pushButton_comconnect.setGeometry(QRect(340, 10, 101, 31))
        self.pushButton_comconnect.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 91, 31))
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_exposure = QLabel(self.frame)
        self.label_exposure.setObjectName(u"label_exposure")
        self.label_exposure.setGeometry(QRect(401, 110, 31, 21))
        self.label_exposure.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;")
        self.label_exposure.setAlignment(Qt.AlignCenter)
        self.label_bright = QLabel(self.frame)
        self.label_bright.setObjectName(u"label_bright")
        self.label_bright.setGeometry(QRect(401, 140, 31, 21))
        self.label_bright.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;")
        self.label_bright.setAlignment(Qt.AlignCenter)
        self.label_aver = QLabel(self.frame)
        self.label_aver.setObjectName(u"label_aver")
        self.label_aver.setGeometry(QRect(401, 200, 31, 21))
        self.label_aver.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;")
        self.label_aver.setAlignment(Qt.AlignCenter)
        self.label_status = QLabel(self.frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(160, 5, 221, 31))
        self.label_status.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 140, 81, 21))
        self.label_17.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 170, 61, 20))
        self.label_18.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 110, 71, 21))
        self.label_14.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 200, 61, 20))
        self.label_19.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.horizontalSlider_average = QSlider(self.frame)
        self.horizontalSlider_average.setObjectName(u"horizontalSlider_average")
        self.horizontalSlider_average.setGeometry(QRect(100, 200, 301, 20))
        self.horizontalSlider_average.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_average.setMinimum(1)
        self.horizontalSlider_average.setMaximum(100)
        self.horizontalSlider_average.setValue(20)
        self.horizontalSlider_average.setOrientation(Qt.Horizontal)
        self.horizontalSlider_average.setInvertedAppearance(False)
        self.label_gain = QLabel(self.frame)
        self.label_gain.setObjectName(u"label_gain")
        self.label_gain.setGeometry(QRect(400, 170, 31, 21))
        self.label_gain.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;")
        self.label_gain.setAlignment(Qt.AlignCenter)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-10, 235, 791, 51))
        self.frame_4.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_settings = QPushButton(self.frame_4)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        self.pushButton_settings.setGeometry(QRect(130, 10, 30, 31))
        self.pushButton_settings.setToolTipDuration(3)
        self.pushButton_settings.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/settings.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/settingsb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_settings.setCheckable(False)
        self.pushButton_savespec = QPushButton(self.frame_4)
        self.pushButton_savespec.setObjectName(u"pushButton_savespec")
        self.pushButton_savespec.setGeometry(QRect(380, 10, 61, 31))
        self.pushButton_savespec.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(120,0,0);\n"
"	background-image: url(:/icons/takeimage.png);\n"
"	color: white;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.pushButton_savespec.setCheckable(False)
        self.pushButton_freeze = QPushButton(self.frame_4)
        self.pushButton_freeze.setObjectName(u"pushButton_freeze")
        self.pushButton_freeze.setGeometry(QRect(300, 10, 31, 31))
        self.pushButton_freeze.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/pause.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/pauseb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_freeze.setCheckable(False)
        self.pushButton_average = QPushButton(self.frame_4)
        self.pushButton_average.setObjectName(u"pushButton_average")
        self.pushButton_average.setGeometry(QRect(340, 10, 31, 31))
        self.pushButton_average.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/summe.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/summeb.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_average.setCheckable(False)
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(160, 15, 50, 21))
        self.label_21.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"\n"
"")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label_21.setWordWrap(False)
        self.pushButton_infobox = QPushButton(self.frame_4)
        self.pushButton_infobox.setObjectName(u"pushButton_infobox")
        self.pushButton_infobox.setGeometry(QRect(260, 10, 31, 31))
        self.pushButton_infobox.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/info.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/infob.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_cali = QPushButton(self.frame_4)
        self.pushButton_cali.setObjectName(u"pushButton_cali")
        self.pushButton_cali.setGeometry(QRect(30, 10, 91, 31))
        self.pushButton_cali.setToolTipDuration(3)
        self.pushButton_cali.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 65), stop:0.166 rgba(255, 255, 0,65), stop:0.333 rgba(0, 255, 0, 65), stop:0.5 rgba(0, 255, 255,65), stop:0.666 rgba(0, 0, 255, 65), stop:0.833 rgba(255, 0, 255,65), stop:1 rgba(255, 0, 0, 65));\n"
"\n"
"	font: 75 12pt \"Futura Md BT\";\n"
"	color:  rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 150), stop:0.166 rgba(255, 255, 0,150), stop:0.333 rgba(0, 255, 0, 150), stop:0.5 rgba(0, 255, 255, 150), stop:0.666 rgba(0, 0, 255, 150), stop:0.833 rgba(255, 0, 255, 150), stop:1 rgba(255, 0, 0, 150));\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, "
                        "255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	color: white;\n"
"}")
        self.pushButton_cali.setCheckable(False)
        self.stackedWidgetsettings = QStackedWidget(self.frame)
        self.stackedWidgetsettings.setObjectName(u"stackedWidgetsettings")
        self.stackedWidgetsettings.setGeometry(QRect(9, 290, 431, 321))
        self.camsettings = QWidget()
        self.camsettings.setObjectName(u"camsettings")
        self.frame_3 = QFrame(self.camsettings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-10, 0, 451, 141))
        self.frame_3.setStyleSheet(u"background-color: rgba(0,0,0, 30);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.checkBox_flipy = QCheckBox(self.frame_3)
        self.checkBox_flipy.setObjectName(u"checkBox_flipy")
        self.checkBox_flipy.setGeometry(QRect(120, 40, 80, 31))
        self.checkBox_flipy.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QRect(30, 0, 121, 31))
        self.label_2.setStyleSheet(u"background: transparent;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.checkBox_flipx = QCheckBox(self.frame_3)
        self.checkBox_flipx.setObjectName(u"checkBox_flipx")
        self.checkBox_flipx.setGeometry(QRect(20, 40, 80, 31))
        self.checkBox_flipx.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.pushButton_liveview = QPushButton(self.frame_3)
        self.pushButton_liveview.setObjectName(u"pushButton_liveview")
        self.pushButton_liveview.setGeometry(QRect(250, 5, 181, 24))
        self.pushButton_liveview.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(150, 0, 0);\n"
"	color: white;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QToolTip {\n"
" color: #ffffff; background-color: #000000; border: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit_ymin = QLineEdit(self.frame_3)
        self.lineEdit_ymin.setObjectName(u"lineEdit_ymin")
        self.lineEdit_ymin.setEnabled(False)
        self.lineEdit_ymin.setGeometry(QRect(190, 80, 31, 23))
        self.lineEdit_ymin.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
" }")
        self.lineEdit_ymin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(220, 80, 21, 23))
        self.label_35.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(120, 110, 41, 21))
        self.label_36.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;\n"
"\n"
"")
        self.label_36.setWordWrap(False)
        self.label_37 = QLabel(self.frame_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(220, 110, 21, 23))
        self.label_37.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.lineEdit_ymax = QLineEdit(self.frame_3)
        self.lineEdit_ymax.setObjectName(u"lineEdit_ymax")
        self.lineEdit_ymax.setEnabled(False)
        self.lineEdit_ymax.setGeometry(QRect(190, 110, 31, 23))
        self.lineEdit_ymax.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
" }")
        self.lineEdit_ymax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 70, 281, 71))
        self.frame_5.setStyleSheet(u"background-color: rgb(35,35,35);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton_yminmin = QPushButton(self.frame_5)
        self.pushButton_yminmin.setObjectName(u"pushButton_yminmin")
        self.pushButton_yminmin.setGeometry(QRect(140, 10, 31, 23))
        self.pushButton_yminmin.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.checkBox_useROI = QCheckBox(self.frame_5)
        self.checkBox_useROI.setObjectName(u"checkBox_useROI")
        self.checkBox_useROI.setGeometry(QRect(10, 0, 61, 31))
        self.checkBox_useROI.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.pushButton_yminplu = QPushButton(self.frame_5)
        self.pushButton_yminplu.setObjectName(u"pushButton_yminplu")
        self.pushButton_yminplu.setGeometry(QRect(240, 10, 31, 23))
        self.pushButton_yminplu.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.pushButton_ymaxmin = QPushButton(self.frame_5)
        self.pushButton_ymaxmin.setObjectName(u"pushButton_ymaxmin")
        self.pushButton_ymaxmin.setGeometry(QRect(140, 40, 31, 23))
        self.pushButton_ymaxmin.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.pushButton_ymaxplu = QPushButton(self.frame_5)
        self.pushButton_ymaxplu.setObjectName(u"pushButton_ymaxplu")
        self.pushButton_ymaxplu.setGeometry(QRect(240, 40, 31, 23))
        self.pushButton_ymaxplu.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(120, 80, 41, 21))
        self.label_34.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;\n"
"\n"
"")
        self.label_34.setWordWrap(False)
        self.checkBox_bayercorr = QCheckBox(self.frame_3)
        self.checkBox_bayercorr.setObjectName(u"checkBox_bayercorr")
        self.checkBox_bayercorr.setGeometry(QRect(320, 40, 111, 31))
        self.checkBox_bayercorr.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.checkBox_bayercorr.setChecked(False)
        self.checkBox_grayscale = QCheckBox(self.frame_3)
        self.checkBox_grayscale.setObjectName(u"checkBox_grayscale")
        self.checkBox_grayscale.setGeometry(QRect(220, 40, 80, 31))
        self.checkBox_grayscale.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.pushButton_screenmode = QPushButton(self.frame_3)
        self.pushButton_screenmode.setObjectName(u"pushButton_screenmode")
        self.pushButton_screenmode.setGeometry(QRect(215, 7, 20, 20))
        self.pushButton_screenmode.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(100,100,100);\n"
"	background-image: url(:/icons/screenmode.png);\n"
"	color: white;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.label_2.raise_()
        self.frame_5.raise_()
        self.checkBox_flipy.raise_()
        self.checkBox_flipx.raise_()
        self.pushButton_liveview.raise_()
        self.lineEdit_ymin.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.lineEdit_ymax.raise_()
        self.label_34.raise_()
        self.checkBox_bayercorr.raise_()
        self.checkBox_grayscale.raise_()
        self.pushButton_screenmode.raise_()
        self.frame_6 = QFrame(self.camsettings)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(-10, 150, 451, 171))
        self.frame_6.setStyleSheet(u"background-color: rgba(0,0,0, 30);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(214, 140, 16, 21))
        self.label_24.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_imgnumber = QLineEdit(self.frame_6)
        self.lineEdit_imgnumber.setObjectName(u"lineEdit_imgnumber")
        self.lineEdit_imgnumber.setEnabled(True)
        self.lineEdit_imgnumber.setGeometry(QRect(183, 108, 30, 23))
        self.lineEdit_imgnumber.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(60,60,60);\n"
"	border-radius: 5px;\n"
" }")
        self.lineEdit_filepath = QLineEdit(self.frame_6)
        self.lineEdit_filepath.setObjectName(u"lineEdit_filepath")
        self.lineEdit_filepath.setGeometry(QRect(130, 40, 281, 23))
        self.lineEdit_filepath.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(60,60,60);\n"
"	border-radius: 5px;\n"
" }")
        self.label_25 = QLabel(self.frame_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(270, 138, 141, 21))
        self.label_25.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(29, 78, 121, 21))
        self.label_22.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_22.setWordWrap(False)
        self.lineEdit_imgformat = QLineEdit(self.frame_6)
        self.lineEdit_imgformat.setObjectName(u"lineEdit_imgformat")
        self.lineEdit_imgformat.setGeometry(QRect(221, 108, 31, 23))
        self.lineEdit_imgformat.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(60,60,60);\n"
"	border-radius: 5px;\n"
" }")
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(214, 110, 16, 21))
        self.label_23.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_filename = QLineEdit(self.frame_6)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")
        self.lineEdit_filename.setGeometry(QRect(63, 108, 113, 23))
        self.lineEdit_filename.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_filename.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(60,60,60);\n"
"	border-radius: 5px;\n"
" }")
        self.lineEdit_filename.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 2, 201, 31))
        self.label_4.setStyleSheet(u"background: transparent;")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_browse = QPushButton(self.frame_6)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setGeometry(QRect(30, 40, 91, 23))
        self.pushButton_browse.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.label_26 = QLabel(self.frame_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(270, 108, 131, 21))
        self.label_26.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.checkBox_autoaddimgnumber = QCheckBox(self.frame_6)
        self.checkBox_autoaddimgnumber.setObjectName(u"checkBox_autoaddimgnumber")
        self.checkBox_autoaddimgnumber.setGeometry(QRect(270, 80, 161, 17))
        self.checkBox_autoaddimgnumber.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.checkBox_autoaddimgnumber.setChecked(True)
        self.lineEdit_specformat = QLineEdit(self.frame_6)
        self.lineEdit_specformat.setObjectName(u"lineEdit_specformat")
        self.lineEdit_specformat.setGeometry(QRect(221, 138, 31, 23))
        self.lineEdit_specformat.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(60,60,60);\n"
"	border-radius: 5px;\n"
" }")
        self.stackedWidgetsettings.addWidget(self.camsettings)
        self.help = QWidget()
        self.help.setObjectName(u"help")
        self.label_38 = QLabel(self.help)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 0, 421, 121))
        self.label_38.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_38.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.stackedWidgetsettings.addWidget(self.help)
        self.calibration = QWidget()
        self.calibration.setObjectName(u"calibration")
        self.frame_7 = QFrame(self.calibration)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(-10, 0, 451, 321))
        self.frame_7.setStyleSheet(u"background-color: rgba(0,0,0, 30);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QRect(30, 0, 201, 31))
        self.label_5.setStyleSheet(u"background: transparent;")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalSlider_wlcalmode = QSlider(self.frame_7)
        self.horizontalSlider_wlcalmode.setObjectName(u"horizontalSlider_wlcalmode")
        self.horizontalSlider_wlcalmode.setGeometry(QRect(280, 100, 31, 22))
        self.horizontalSlider_wlcalmode.setStyleSheet(u"QSlider{\n"
"background:transparent;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.horizontalSlider_wlcalmode.setMinimum(2)
        self.horizontalSlider_wlcalmode.setMaximum(3)
        self.horizontalSlider_wlcalmode.setValue(3)
        self.horizontalSlider_wlcalmode.setSliderPosition(3)
        self.horizontalSlider_wlcalmode.setTracking(False)
        self.horizontalSlider_wlcalmode.setOrientation(Qt.Horizontal)
        self.horizontalSlider_wlcalmode.setInvertedAppearance(False)
        self.horizontalSlider_wlcalmode.setInvertedControls(False)
        self.pushButton_getP1 = QPushButton(self.frame_7)
        self.pushButton_getP1.setObjectName(u"pushButton_getP1")
        self.pushButton_getP1.setGeometry(QRect(70, 150, 131, 23))
        self.pushButton_getP1.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.pushButton_getP2 = QPushButton(self.frame_7)
        self.pushButton_getP2.setObjectName(u"pushButton_getP2")
        self.pushButton_getP2.setGeometry(QRect(70, 180, 131, 23))
        self.pushButton_getP2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.lineEdit_wl1 = QLineEdit(self.frame_7)
        self.lineEdit_wl1.setObjectName(u"lineEdit_wl1")
        self.lineEdit_wl1.setGeometry(QRect(220, 150, 41, 23))
        self.lineEdit_wl1.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_wl1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(270, 180, 21, 23))
        self.label_20.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(270, 150, 21, 23))
        self.label_27.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.pushButton_calwlaxis = QPushButton(self.frame_7)
        self.pushButton_calwlaxis.setObjectName(u"pushButton_calwlaxis")
        self.pushButton_calwlaxis.setGeometry(QRect(125, 245, 211, 31))
        self.pushButton_calwlaxis.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(150, 0, 0);\n"
"	color: white;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QToolTip {\n"
" color: #ffffff; background-color: #000000; border: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit_wl2 = QLineEdit(self.frame_7)
        self.lineEdit_wl2.setObjectName(u"lineEdit_wl2")
        self.lineEdit_wl2.setGeometry(QRect(220, 180, 41, 23))
        self.lineEdit_wl2.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_wl2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_savewlaxis = QPushButton(self.frame_7)
        self.pushButton_savewlaxis.setObjectName(u"pushButton_savewlaxis")
        self.pushButton_savewlaxis.setGeometry(QRect(60, 290, 101, 23))
        self.pushButton_savewlaxis.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.label_28 = QLabel(self.frame_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(210, 100, 61, 21))
        self.label_28.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_28.setWordWrap(False)
        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(330, 100, 61, 21))
        self.label_29.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_29.setWordWrap(False)
        self.pushButton_getP3 = QPushButton(self.frame_7)
        self.pushButton_getP3.setObjectName(u"pushButton_getP3")
        self.pushButton_getP3.setGeometry(QRect(70, 210, 131, 23))
        self.pushButton_getP3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.label_30 = QLabel(self.frame_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(215, 125, 91, 21))
        self.label_30.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_30.setWordWrap(False)
        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(320, 125, 91, 21))
        self.label_31.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_31.setWordWrap(False)
        self.lineEdit_wl3 = QLineEdit(self.frame_7)
        self.lineEdit_wl3.setObjectName(u"lineEdit_wl3")
        self.lineEdit_wl3.setGeometry(QRect(220, 210, 41, 23))
        self.lineEdit_wl3.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_wl3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_32 = QLabel(self.frame_7)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(270, 210, 21, 23))
        self.label_32.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_px1 = QLineEdit(self.frame_7)
        self.lineEdit_px1.setObjectName(u"lineEdit_px1")
        self.lineEdit_px1.setGeometry(QRect(320, 150, 41, 23))
        self.lineEdit_px1.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_px1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_px2 = QLineEdit(self.frame_7)
        self.lineEdit_px2.setObjectName(u"lineEdit_px2")
        self.lineEdit_px2.setGeometry(QRect(320, 180, 41, 23))
        self.lineEdit_px2.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_px2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_px3 = QLineEdit(self.frame_7)
        self.lineEdit_px3.setObjectName(u"lineEdit_px3")
        self.lineEdit_px3.setGeometry(QRect(320, 210, 41, 23))
        self.lineEdit_px3.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_px3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_loadwlaxis = QPushButton(self.frame_7)
        self.pushButton_loadwlaxis.setObjectName(u"pushButton_loadwlaxis")
        self.pushButton_loadwlaxis.setGeometry(QRect(180, 290, 101, 23))
        self.pushButton_loadwlaxis.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(70, 100, 141, 21))
        self.label_33.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_33.setWordWrap(False)
        self.pushButton_clearcal = QPushButton(self.frame_7)
        self.pushButton_clearcal.setObjectName(u"pushButton_clearcal")
        self.pushButton_clearcal.setGeometry(QRect(300, 290, 101, 23))
        self.pushButton_clearcal.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}")
        self.label_39 = QLabel(self.frame_7)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 35, 391, 51))
        self.label_39.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_39.setWordWrap(True)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(30, 100, 391, 21))
        self.frame_9.setStyleSheet(u"background-color: rgb(35,35,35);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.raise_()
        self.label_5.raise_()
        self.label_33.raise_()
        self.horizontalSlider_wlcalmode.raise_()
        self.pushButton_getP1.raise_()
        self.pushButton_getP2.raise_()
        self.lineEdit_wl1.raise_()
        self.label_20.raise_()
        self.pushButton_calwlaxis.raise_()
        self.lineEdit_wl2.raise_()
        self.pushButton_savewlaxis.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.pushButton_getP3.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.lineEdit_wl3.raise_()
        self.lineEdit_px1.raise_()
        self.lineEdit_px2.raise_()
        self.lineEdit_px3.raise_()
        self.pushButton_loadwlaxis.raise_()
        self.label_31.raise_()
        self.pushButton_clearcal.raise_()
        self.label_32.raise_()
        self.label_39.raise_()
        self.stackedWidgetsettings.addWidget(self.calibration)
        self.pushButton_exit = QPushButton(speccom_mainwin)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(420, 20, 20, 20))
        self.pushButton_exit.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(120,0,0);\n"
"	background-image: url(:/icons/exit.png);\n"
"	color: white;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.pushButton_mini = QPushButton(speccom_mainwin)
        self.pushButton_mini.setObjectName(u"pushButton_mini")
        self.pushButton_mini.setGeometry(QRect(395, 20, 20, 20))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_mini.setFont(font)
        self.pushButton_mini.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(100,100,100);\n"
"	background-image: url(:/icons/minimize.png);\n"
"	color: white;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"")

        self.retranslateUi(speccom_mainwin)

        self.stackedWidgetsettings.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(speccom_mainwin)
    # setupUi

    def retranslateUi(self, speccom_mainwin):
        speccom_mainwin.setWindowTitle(QCoreApplication.translate("speccom_mainwin", u"Form", None))
        self.label.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#f0f0f0;\">SpecControl</span></p><p><br/></p></body></html>", None))
        self.pushButton_comrefresh.setText(QCoreApplication.translate("speccom_mainwin", u"refresh", None))
        self.pushButton_comconnect.setText(QCoreApplication.translate("speccom_mainwin", u"connect", None))
        self.label_3.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#6496c8;\">camera</span></p></body></html>", None))
        self.label_exposure.setText(QCoreApplication.translate("speccom_mainwin", u"-10", None))
        self.label_bright.setText(QCoreApplication.translate("speccom_mainwin", u"0", None))
        self.label_aver.setText(QCoreApplication.translate("speccom_mainwin", u"20", None))
        self.label_status.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">waiting</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Brightness</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Gain</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Exposure</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Average</span></p></body></html>", None))
        self.label_gain.setText(QCoreApplication.translate("speccom_mainwin", u"1", None))
#if QT_CONFIG(tooltip)
        self.pushButton_settings.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_settings.setText("")
        self.pushButton_savespec.setText("")
        self.pushButton_freeze.setText("")
        self.pushButton_average.setText("")
        self.label_21.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Settings</span></p></body></html>", None))
        self.pushButton_infobox.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_cali.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_cali.setText(QCoreApplication.translate("speccom_mainwin", u"calibration", None))
        self.checkBox_flipy.setText(QCoreApplication.translate("speccom_mainwin", u"flip y-axis", None))
        self.label_2.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">camera source</span></p></body></html>", None))
        self.checkBox_flipx.setText(QCoreApplication.translate("speccom_mainwin", u"flip x-axis", None))
        self.pushButton_liveview.setText(QCoreApplication.translate("speccom_mainwin", u"live view", None))
        self.lineEdit_ymin.setText(QCoreApplication.translate("speccom_mainwin", u"200", None))
        self.label_35.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" color:#ffffff;\">px</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">y</span><span style=\" font-size:10pt; font-weight:600; color:#ffffff; vertical-align:sub;\">max</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" color:#ffffff;\">px</span></p></body></html>", None))
        self.lineEdit_ymax.setText(QCoreApplication.translate("speccom_mainwin", u"880", None))
        self.pushButton_yminmin.setText(QCoreApplication.translate("speccom_mainwin", u"-", None))
        self.checkBox_useROI.setText(QCoreApplication.translate("speccom_mainwin", u"use ROI", None))
        self.pushButton_yminplu.setText(QCoreApplication.translate("speccom_mainwin", u"+", None))
        self.pushButton_ymaxmin.setText(QCoreApplication.translate("speccom_mainwin", u"-", None))
        self.pushButton_ymaxplu.setText(QCoreApplication.translate("speccom_mainwin", u"+", None))
        self.label_34.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">y</span><span style=\" font-size:10pt; font-weight:600; color:#ffffff; vertical-align:sub;\">min</span></p></body></html>", None))
        self.checkBox_bayercorr.setText(QCoreApplication.translate("speccom_mainwin", u"bayer correction", None))
        self.checkBox_grayscale.setText(QCoreApplication.translate("speccom_mainwin", u"grayscale", None))
        self.pushButton_screenmode.setText("")
        self.label_24.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">.</span></p></body></html>", None))
        self.lineEdit_imgnumber.setText(QCoreApplication.translate("speccom_mainwin", u"1", None))
        self.lineEdit_filepath.setText(QCoreApplication.translate("speccom_mainwin", u"C:\\", None))
        self.label_25.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" color:#ffffff;\">spectrum format (tabular)</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#bebebe;\">Selected filename:</span></p></body></html>", None))
        self.lineEdit_imgformat.setText(QCoreApplication.translate("speccom_mainwin", u"bmp", None))
        self.label_23.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">.</span></p></body></html>", None))
        self.lineEdit_filename.setText(QCoreApplication.translate("speccom_mainwin", u"data", None))
        self.label_4.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">storage settings</span></p></body></html>", None))
        self.pushButton_browse.setText(QCoreApplication.translate("speccom_mainwin", u"browse", None))
        self.label_26.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" color:#ffffff;\">frame/image format</span></p></body></html>", None))
        self.checkBox_autoaddimgnumber.setText(QCoreApplication.translate("speccom_mainwin", u"autoadd image numbers", None))
        self.lineEdit_specformat.setText(QCoreApplication.translate("speccom_mainwin", u"csv", None))
        self.label_38.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">SpecControl - PrintedLabs</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Version: 1.0 - 10/20/2023</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Would you like to learn more about ScopeControl and get<br/>a tutorial on all implemented functions. You can find this and<br/>much more on our website </span><a href=\"https://printedlabs.uni-bayreuth.de/\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#dc0000;\">printedlabs.uni-bayreuth.de</span></a><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">!</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">wavelength calibration</span></p></body></html>", None))
        self.pushButton_getP1.setText(QCoreApplication.translate("speccom_mainwin", u"set calibration point", None))
        self.pushButton_getP2.setText(QCoreApplication.translate("speccom_mainwin", u"set calibration point", None))
        self.lineEdit_wl1.setText(QCoreApplication.translate("speccom_mainwin", u"400", None))
        self.label_20.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" color:#ffffff;\">nm</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" color:#ffffff;\">nm</span></p></body></html>", None))
        self.pushButton_calwlaxis.setText(QCoreApplication.translate("speccom_mainwin", u"compute calibration curve", None))
        self.lineEdit_wl2.setText(QCoreApplication.translate("speccom_mainwin", u"500", None))
        self.pushButton_savewlaxis.setText(QCoreApplication.translate("speccom_mainwin", u"save calibration", None))
        self.label_28.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">2 Points</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">3 Points</span></p></body></html>", None))
        self.pushButton_getP3.setText(QCoreApplication.translate("speccom_mainwin", u"set calibration point", None))
        self.label_30.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">wavelength</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">camera px</span></p></body></html>", None))
        self.lineEdit_wl3.setText(QCoreApplication.translate("speccom_mainwin", u"700", None))
        self.label_32.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" color:#ffffff;\">nm</span></p></body></html>", None))
        self.lineEdit_px1.setText(QCoreApplication.translate("speccom_mainwin", u"1", None))
        self.lineEdit_px2.setText(QCoreApplication.translate("speccom_mainwin", u"1", None))
        self.lineEdit_px3.setText(QCoreApplication.translate("speccom_mainwin", u"1", None))
        self.pushButton_loadwlaxis.setText(QCoreApplication.translate("speccom_mainwin", u"load calibration", None))
        self.label_33.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">calibration mode:</span></p></body></html>", None))
        self.pushButton_clearcal.setText(QCoreApplication.translate("speccom_mainwin", u"delete calibration", None))
        self.label_39.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">For highest accuracy, mark 3 known wavelengths in the spectrum and set calibration points for each. Then calculate the calibration curve.</span></p></body></html>", None))
        self.pushButton_exit.setText("")
        self.pushButton_mini.setText("")
    # retranslateUi


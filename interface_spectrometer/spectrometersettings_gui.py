# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrometersettings_gui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QWidget)
import graphics.buttons_rc

class Ui_spectrometer_settingswin(object):
    def setupUi(self, spectrometer_settingswin):
        if not spectrometer_settingswin.objectName():
            spectrometer_settingswin.setObjectName(u"spectrometer_settingswin")
        spectrometer_settingswin.resize(767, 332)
        spectrometer_settingswin.setStyleSheet(u"button->setStyleSheet(\"border-image:url(:/icons/arrow_l.png);\");")
        self.frame = QFrame(spectrometer_settingswin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-40, -30, 801, 351))
        self.frame.setStyleSheet(u"background-color: rgb(50, 49, 52);\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_exit = QPushButton(self.frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(765, 40, 20, 20))
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
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(50, 40, 361, 121))
        self.frame_2.setStyleSheet(u"background-color: rgba(0,0,0, 30);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.checkBox_flipy = QCheckBox(self.frame_2)
        self.checkBox_flipy.setObjectName(u"checkBox_flipy")
        self.checkBox_flipy.setGeometry(QRect(20, 65, 80, 31))
        self.checkBox_flipy.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(10, 0, 121, 31))
        self.label.setStyleSheet(u"background: transparent;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.checkBox_flipx = QCheckBox(self.frame_2)
        self.checkBox_flipx.setObjectName(u"checkBox_flipx")
        self.checkBox_flipx.setGeometry(QRect(20, 40, 80, 31))
        self.checkBox_flipx.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.pushButton_liveview = QPushButton(self.frame_2)
        self.pushButton_liveview.setObjectName(u"pushButton_liveview")
        self.pushButton_liveview.setGeometry(QRect(190, 5, 161, 23))
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
        self.checkBox_imginfo = QCheckBox(self.frame_2)
        self.checkBox_imginfo.setObjectName(u"checkBox_imginfo")
        self.checkBox_imginfo.setGeometry(QRect(20, 90, 101, 31))
        self.checkBox_imginfo.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.lineEdit_ymin = QLineEdit(self.frame_2)
        self.lineEdit_ymin.setObjectName(u"lineEdit_ymin")
        self.lineEdit_ymin.setEnabled(False)
        self.lineEdit_ymin.setGeometry(QRect(260, 45, 31, 23))
        self.lineEdit_ymin.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
" }")
        self.lineEdit_ymin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(290, 45, 21, 23))
        self.label_35.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_36 = QLabel(self.frame_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(190, 80, 41, 21))
        self.label_36.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;\n"
"\n"
"")
        self.label_36.setWordWrap(False)
        self.label_37 = QLabel(self.frame_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(290, 80, 21, 23))
        self.label_37.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.lineEdit_ymax = QLineEdit(self.frame_2)
        self.lineEdit_ymax.setObjectName(u"lineEdit_ymax")
        self.lineEdit_ymax.setEnabled(False)
        self.lineEdit_ymax.setGeometry(QRect(260, 80, 31, 23))
        self.lineEdit_ymax.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
" }")
        self.lineEdit_ymax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(100, 40, 256, 76))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton_yminmin = QPushButton(self.frame_5)
        self.pushButton_yminmin.setObjectName(u"pushButton_yminmin")
        self.pushButton_yminmin.setGeometry(QRect(120, 5, 31, 23))
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
        self.pushButton_yminplu.setGeometry(QRect(220, 5, 31, 23))
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
        self.pushButton_ymaxmin.setGeometry(QRect(120, 40, 31, 23))
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
        self.pushButton_ymaxplu.setGeometry(QRect(220, 40, 31, 23))
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
        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(190, 45, 41, 21))
        self.label_34.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;\n"
"\n"
"")
        self.label_34.setWordWrap(False)
        self.frame_5.raise_()
        self.checkBox_flipy.raise_()
        self.label.raise_()
        self.checkBox_flipx.raise_()
        self.pushButton_liveview.raise_()
        self.checkBox_imginfo.raise_()
        self.lineEdit_ymin.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.lineEdit_ymax.raise_()
        self.label_34.raise_()
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(420, 40, 371, 301))
        self.frame_3.setStyleSheet(u"background-color: rgba(0,0,0, 30);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QRect(10, 0, 201, 31))
        self.label_2.setStyleSheet(u"background: transparent;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalSlider_wlcalmode = QSlider(self.frame_3)
        self.horizontalSlider_wlcalmode.setObjectName(u"horizontalSlider_wlcalmode")
        self.horizontalSlider_wlcalmode.setGeometry(QRect(240, 40, 31, 22))
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
        self.pushButton_getP1 = QPushButton(self.frame_3)
        self.pushButton_getP1.setObjectName(u"pushButton_getP1")
        self.pushButton_getP1.setGeometry(QRect(30, 100, 131, 23))
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
        self.pushButton_getP2 = QPushButton(self.frame_3)
        self.pushButton_getP2.setObjectName(u"pushButton_getP2")
        self.pushButton_getP2.setGeometry(QRect(30, 130, 131, 23))
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
        self.lineEdit_wl1 = QLineEdit(self.frame_3)
        self.lineEdit_wl1.setObjectName(u"lineEdit_wl1")
        self.lineEdit_wl1.setGeometry(QRect(180, 100, 41, 23))
        self.lineEdit_wl1.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_wl1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(230, 130, 21, 23))
        self.label_20.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(230, 100, 21, 23))
        self.label_19.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.pushButton_calwlaxis = QPushButton(self.frame_3)
        self.pushButton_calwlaxis.setObjectName(u"pushButton_calwlaxis")
        self.pushButton_calwlaxis.setGeometry(QRect(80, 210, 211, 31))
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
        self.lineEdit_wl2 = QLineEdit(self.frame_3)
        self.lineEdit_wl2.setObjectName(u"lineEdit_wl2")
        self.lineEdit_wl2.setGeometry(QRect(180, 130, 41, 23))
        self.lineEdit_wl2.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_wl2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_savewlaxis = QPushButton(self.frame_3)
        self.pushButton_savewlaxis.setObjectName(u"pushButton_savewlaxis")
        self.pushButton_savewlaxis.setGeometry(QRect(20, 260, 101, 23))
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
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(170, 40, 61, 21))
        self.label_27.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_27.setWordWrap(False)
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(290, 40, 61, 21))
        self.label_28.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_28.setWordWrap(False)
        self.pushButton_getP3 = QPushButton(self.frame_3)
        self.pushButton_getP3.setObjectName(u"pushButton_getP3")
        self.pushButton_getP3.setGeometry(QRect(30, 160, 131, 23))
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
        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(175, 75, 91, 21))
        self.label_29.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_29.setWordWrap(False)
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(280, 75, 91, 21))
        self.label_30.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_30.setWordWrap(False)
        self.lineEdit_wl3 = QLineEdit(self.frame_3)
        self.lineEdit_wl3.setObjectName(u"lineEdit_wl3")
        self.lineEdit_wl3.setGeometry(QRect(180, 160, 41, 23))
        self.lineEdit_wl3.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_wl3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(230, 160, 21, 23))
        self.label_21.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_px1 = QLineEdit(self.frame_3)
        self.lineEdit_px1.setObjectName(u"lineEdit_px1")
        self.lineEdit_px1.setGeometry(QRect(280, 100, 41, 23))
        self.lineEdit_px1.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_px1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_px2 = QLineEdit(self.frame_3)
        self.lineEdit_px2.setObjectName(u"lineEdit_px2")
        self.lineEdit_px2.setGeometry(QRect(280, 130, 41, 23))
        self.lineEdit_px2.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_px2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_px3 = QLineEdit(self.frame_3)
        self.lineEdit_px3.setObjectName(u"lineEdit_px3")
        self.lineEdit_px3.setGeometry(QRect(280, 160, 41, 23))
        self.lineEdit_px3.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_px3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_loadwlaxis = QPushButton(self.frame_3)
        self.pushButton_loadwlaxis.setObjectName(u"pushButton_loadwlaxis")
        self.pushButton_loadwlaxis.setGeometry(QRect(135, 260, 101, 23))
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
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 70, 351, 131))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(30, 40, 141, 21))
        self.label_31.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_31.setWordWrap(False)
        self.pushButton_clearcal = QPushButton(self.frame_3)
        self.pushButton_clearcal.setObjectName(u"pushButton_clearcal")
        self.pushButton_clearcal.setGeometry(QRect(250, 260, 101, 23))
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
        self.frame_6.raise_()
        self.label_2.raise_()
        self.horizontalSlider_wlcalmode.raise_()
        self.pushButton_getP1.raise_()
        self.pushButton_getP2.raise_()
        self.lineEdit_wl1.raise_()
        self.label_20.raise_()
        self.label_19.raise_()
        self.pushButton_calwlaxis.raise_()
        self.lineEdit_wl2.raise_()
        self.pushButton_savewlaxis.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.pushButton_getP3.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.lineEdit_wl3.raise_()
        self.label_21.raise_()
        self.lineEdit_px1.raise_()
        self.lineEdit_px2.raise_()
        self.lineEdit_px3.raise_()
        self.pushButton_loadwlaxis.raise_()
        self.label_31.raise_()
        self.pushButton_clearcal.raise_()
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(50, 170, 361, 171))
        self.frame_4.setStyleSheet(u"background-color: rgba(0,0,0, 30);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(154, 140, 16, 21))
        self.label_24.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_imgnumber = QLineEdit(self.frame_4)
        self.lineEdit_imgnumber.setObjectName(u"lineEdit_imgnumber")
        self.lineEdit_imgnumber.setEnabled(True)
        self.lineEdit_imgnumber.setGeometry(QRect(123, 108, 30, 23))
        self.lineEdit_imgnumber.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(60,60,60);\n"
"	border-radius: 5px;\n"
" }")
        self.lineEdit_filepath = QLineEdit(self.frame_4)
        self.lineEdit_filepath.setObjectName(u"lineEdit_filepath")
        self.lineEdit_filepath.setGeometry(QRect(102, 40, 231, 23))
        self.lineEdit_filepath.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(60,60,60);\n"
"	border-radius: 5px;\n"
" }")
        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(210, 138, 141, 21))
        self.label_25.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(2, 78, 121, 21))
        self.label_22.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_22.setWordWrap(False)
        self.lineEdit_imgformat = QLineEdit(self.frame_4)
        self.lineEdit_imgformat.setObjectName(u"lineEdit_imgformat")
        self.lineEdit_imgformat.setGeometry(QRect(161, 108, 31, 23))
        self.lineEdit_imgformat.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(60,60,60);\n"
"	border-radius: 5px;\n"
" }")
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(154, 110, 16, 21))
        self.label_23.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_filename = QLineEdit(self.frame_4)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")
        self.lineEdit_filename.setGeometry(QRect(3, 108, 113, 23))
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
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(9, 2, 201, 31))
        self.label_3.setStyleSheet(u"background: transparent;")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_browse = QPushButton(self.frame_4)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setGeometry(QRect(2, 40, 91, 23))
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
        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(210, 108, 131, 21))
        self.label_26.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.checkBox_autoaddimgnumber = QCheckBox(self.frame_4)
        self.checkBox_autoaddimgnumber.setObjectName(u"checkBox_autoaddimgnumber")
        self.checkBox_autoaddimgnumber.setGeometry(QRect(161, 80, 161, 17))
        self.checkBox_autoaddimgnumber.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.checkBox_autoaddimgnumber.setChecked(True)
        self.lineEdit_specformat = QLineEdit(self.frame_4)
        self.lineEdit_specformat.setObjectName(u"lineEdit_specformat")
        self.lineEdit_specformat.setGeometry(QRect(161, 138, 31, 23))
        self.lineEdit_specformat.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(60,60,60);\n"
"	border-radius: 5px;\n"
" }")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(50, 350, 741, 31))
        self.frame_7.setStyleSheet(u"background-color: rgba(0,0,0, 30);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.pushButton_exit.raise_()
        self.frame_7.raise_()

        self.retranslateUi(spectrometer_settingswin)

        QMetaObject.connectSlotsByName(spectrometer_settingswin)
    # setupUi

    def retranslateUi(self, spectrometer_settingswin):
        spectrometer_settingswin.setWindowTitle(QCoreApplication.translate("spectrometer_settingswin", u"Form", None))
        self.pushButton_exit.setText("")
        self.checkBox_flipy.setText(QCoreApplication.translate("spectrometer_settingswin", u"flip y-axis", None))
        self.label.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">camera source</span></p></body></html>", None))
        self.checkBox_flipx.setText(QCoreApplication.translate("spectrometer_settingswin", u"flip x-axis", None))
        self.pushButton_liveview.setText(QCoreApplication.translate("spectrometer_settingswin", u"live view", None))
        self.checkBox_imginfo.setText(QCoreApplication.translate("spectrometer_settingswin", u"show info", None))
        self.lineEdit_ymin.setText(QCoreApplication.translate("spectrometer_settingswin", u"200", None))
        self.label_35.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" color:#ffffff;\">px</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">y</span><span style=\" font-size:10pt; font-weight:600; color:#ffffff; vertical-align:sub;\">max</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" color:#ffffff;\">px</span></p></body></html>", None))
        self.lineEdit_ymax.setText(QCoreApplication.translate("spectrometer_settingswin", u"880", None))
        self.pushButton_yminmin.setText(QCoreApplication.translate("spectrometer_settingswin", u"-", None))
        self.checkBox_useROI.setText(QCoreApplication.translate("spectrometer_settingswin", u"use ROI", None))
        self.pushButton_yminplu.setText(QCoreApplication.translate("spectrometer_settingswin", u"+", None))
        self.pushButton_ymaxmin.setText(QCoreApplication.translate("spectrometer_settingswin", u"-", None))
        self.pushButton_ymaxplu.setText(QCoreApplication.translate("spectrometer_settingswin", u"+", None))
        self.label_34.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">y</span><span style=\" font-size:10pt; font-weight:600; color:#ffffff; vertical-align:sub;\">min</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">wavelength calibration</span></p></body></html>", None))
        self.pushButton_getP1.setText(QCoreApplication.translate("spectrometer_settingswin", u"get calibration point", None))
        self.pushButton_getP2.setText(QCoreApplication.translate("spectrometer_settingswin", u"get calibration point", None))
        self.lineEdit_wl1.setText(QCoreApplication.translate("spectrometer_settingswin", u"400", None))
        self.label_20.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" color:#ffffff;\">nm</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" color:#ffffff;\">nm</span></p></body></html>", None))
        self.pushButton_calwlaxis.setText(QCoreApplication.translate("spectrometer_settingswin", u"compute calibration curve", None))
        self.lineEdit_wl2.setText(QCoreApplication.translate("spectrometer_settingswin", u"500", None))
        self.pushButton_savewlaxis.setText(QCoreApplication.translate("spectrometer_settingswin", u"save calibration", None))
        self.label_27.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">2 Points</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">3 Points</span></p></body></html>", None))
        self.pushButton_getP3.setText(QCoreApplication.translate("spectrometer_settingswin", u"get calibration point", None))
        self.label_29.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">wavelength</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">camera px</span></p></body></html>", None))
        self.lineEdit_wl3.setText(QCoreApplication.translate("spectrometer_settingswin", u"700", None))
        self.label_21.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" color:#ffffff;\">nm</span></p></body></html>", None))
        self.lineEdit_px1.setText(QCoreApplication.translate("spectrometer_settingswin", u"1", None))
        self.lineEdit_px2.setText(QCoreApplication.translate("spectrometer_settingswin", u"1", None))
        self.lineEdit_px3.setText(QCoreApplication.translate("spectrometer_settingswin", u"1", None))
        self.pushButton_loadwlaxis.setText(QCoreApplication.translate("spectrometer_settingswin", u"load calibration", None))
        self.label_31.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">calibration mode:</span></p></body></html>", None))
        self.pushButton_clearcal.setText(QCoreApplication.translate("spectrometer_settingswin", u"delete calibration", None))
        self.label_24.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">.</span></p></body></html>", None))
        self.lineEdit_imgnumber.setText(QCoreApplication.translate("spectrometer_settingswin", u"1", None))
        self.lineEdit_filepath.setText(QCoreApplication.translate("spectrometer_settingswin", u"C:\\", None))
        self.label_25.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" color:#ffffff;\">spectrum format (tabular)</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#bebebe;\">Selected filename:</span></p></body></html>", None))
        self.lineEdit_imgformat.setText(QCoreApplication.translate("spectrometer_settingswin", u"bmp", None))
        self.label_23.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">.</span></p></body></html>", None))
        self.lineEdit_filename.setText(QCoreApplication.translate("spectrometer_settingswin", u"data", None))
        self.label_3.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">storage settings</span></p></body></html>", None))
        self.pushButton_browse.setText(QCoreApplication.translate("spectrometer_settingswin", u"browse", None))
        self.label_26.setText(QCoreApplication.translate("spectrometer_settingswin", u"<html><head/><body><p><span style=\" color:#ffffff;\">frame/image format</span></p></body></html>", None))
        self.checkBox_autoaddimgnumber.setText(QCoreApplication.translate("spectrometer_settingswin", u"autoadd image numbers", None))
        self.lineEdit_specformat.setText(QCoreApplication.translate("spectrometer_settingswin", u"csv", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrometercom_gui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSlider, QWidget)
import graphics.buttons_rc

class Ui_speccom_mainwin(object):
    def setupUi(self, speccom_mainwin):
        if not speccom_mainwin.objectName():
            speccom_mainwin.setObjectName(u"speccom_mainwin")
        speccom_mainwin.resize(458, 298)
        speccom_mainwin.setStyleSheet(u"button->setStyleSheet(\"border-image:url(:/icons/arrow_l.png);\");")
        self.frame = QFrame(speccom_mainwin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 451, 281))
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
        self.horizontalSlider_bright.setGeometry(QRect(89, 140, 301, 22))
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
        self.horizontalSlider_gain.setGeometry(QRect(89, 170, 301, 22))
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
        self.horizontalSlider_gain.setValue(20)
        self.horizontalSlider_gain.setOrientation(Qt.Horizontal)
        self.horizontalSlider_gain.setInvertedAppearance(False)
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 140, 61, 21))
        self.label_15.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.checkBox_bayercorr = QCheckBox(self.frame)
        self.checkBox_bayercorr.setObjectName(u"checkBox_bayercorr")
        self.checkBox_bayercorr.setGeometry(QRect(320, 200, 111, 31))
        self.checkBox_bayercorr.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.checkBox_bayercorr.setChecked(False)
        self.horizontalSlider_exposure = QSlider(self.frame)
        self.horizontalSlider_exposure.setObjectName(u"horizontalSlider_exposure")
        self.horizontalSlider_exposure.setGeometry(QRect(89, 110, 301, 22))
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
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 170, 61, 21))
        self.label_16.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 110, 61, 21))
        self.label_14.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
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
        self.comboBox_camport.setGeometry(QRect(130, 15, 51, 22))
        self.comboBox_camport.setStyleSheet(u"color: rgb(255,255,255)\n"
"")
        self.pushButton_comrefresh = QPushButton(self.frame_2)
        self.pushButton_comrefresh.setObjectName(u"pushButton_comrefresh")
        self.pushButton_comrefresh.setGeometry(QRect(220, 10, 101, 30))
        self.pushButton_comrefresh.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: white;\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
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
        self.pushButton_comconnect.setGeometry(QRect(330, 10, 101, 30))
        self.pushButton_comconnect.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: white;\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
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
        self.label_3.setGeometry(QRect(30, 10, 91, 31))
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.checkBox_spectrum = QCheckBox(self.frame)
        self.checkBox_spectrum.setObjectName(u"checkBox_spectrum")
        self.checkBox_spectrum.setGeometry(QRect(30, 200, 80, 31))
        self.checkBox_spectrum.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.checkBox_average = QCheckBox(self.frame)
        self.checkBox_average.setObjectName(u"checkBox_average")
        self.checkBox_average.setGeometry(QRect(130, 200, 101, 31))
        self.checkBox_average.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.pushButton_settings = QPushButton(self.frame)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        self.pushButton_settings.setGeometry(QRect(30, 240, 121, 31))
        self.pushButton_settings.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_settings.setCheckable(False)
        self.pushButton_savespec = QPushButton(self.frame)
        self.pushButton_savespec.setObjectName(u"pushButton_savespec")
        self.pushButton_savespec.setGeometry(QRect(300, 240, 121, 31))
        self.pushButton_savespec.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_savespec.setCheckable(False)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(450, 95, 311, 191))
        self.frame_3.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.comboBox_devices = QComboBox(self.frame_3)
        self.comboBox_devices.setObjectName(u"comboBox_devices")
        self.comboBox_devices.setGeometry(QRect(20, 145, 171, 31))
        self.comboBox_devices.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color: rgba(0,0,0,100);\n"
"")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 10, 271, 31))
        self.label_9.setStyleSheet(u"background-color: transparent;\n"
"background: rgba(0,0,0,100);\n"
"color: rgb(100,150,200);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.pushButton_adddev = QPushButton(self.frame_3)
        self.pushButton_adddev.setObjectName(u"pushButton_adddev")
        self.pushButton_adddev.setGeometry(QRect(205, 145, 41, 31))
        self.pushButton_adddev.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgba(255,255,255,20);\n"
"border: none;\n"
"background-image: url(:/icons/plus.png);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgba(255,255,255,40);\n"
"border: none;\n"
"background-image: url(:/icons/plusH.png);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(100,150,200,255);\n"
"border: none;\n"
"background-image: url(:/icons/plusH.png);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_deldev = QPushButton(self.frame_3)
        self.pushButton_deldev.setObjectName(u"pushButton_deldev")
        self.pushButton_deldev.setGeometry(QRect(250, 145, 41, 31))
        self.pushButton_deldev.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgba(255,255,255,20);\n"
"border: none;\n"
"background-image: url(:/icons/minus.png);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgba(255,255,255,40);\n"
"border: none;\n"
"background-image: url(:/icons/minusH.png);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(100,150,200,255);\n"
"border: none;\n"
"background-image: url(:/icons/minusH.png);\n"
"}\n"
"\n"
"\n"
"")
        self.listWidget_interf = QListWidget(self.frame_3)
        self.listWidget_interf.setObjectName(u"listWidget_interf")
        self.listWidget_interf.setGeometry(QRect(20, 45, 271, 91))
        self.listWidget_interf.setStyleSheet(u"QListWidget\n"
"{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(210,210,210);\n"
"background: rgba(0,0,0,100);\n"
"border: 2px white;\n"
"}\n"
"\n"
"QListView::item:selected\n"
"{\n"
"color: rgb(255,255,255);\n"
"background : rgb(100,150,200);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 15px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(60, 110, 160);\n"
"    min-height: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"      border: none;\n"
"      background: none;\n"
"}")
        self.listWidget_interf.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pushButton_saveimg = QPushButton(self.frame)
        self.pushButton_saveimg.setObjectName(u"pushButton_saveimg")
        self.pushButton_saveimg.setGeometry(QRect(165, 240, 121, 31))
        self.pushButton_saveimg.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_saveimg.setCheckable(False)
        self.checkBox_grayscale = QCheckBox(self.frame)
        self.checkBox_grayscale.setObjectName(u"checkBox_grayscale")
        self.checkBox_grayscale.setGeometry(QRect(230, 200, 80, 31))
        self.checkBox_grayscale.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	color: white;\n"
"}")
        self.label_exposure = QLabel(self.frame)
        self.label_exposure.setObjectName(u"label_exposure")
        self.label_exposure.setGeometry(QRect(390, 110, 31, 21))
        self.label_exposure.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;")
        self.label_exposure.setAlignment(Qt.AlignCenter)
        self.label_bright = QLabel(self.frame)
        self.label_bright.setObjectName(u"label_bright")
        self.label_bright.setGeometry(QRect(390, 140, 31, 21))
        self.label_bright.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;")
        self.label_bright.setAlignment(Qt.AlignCenter)
        self.label_aver = QLabel(self.frame)
        self.label_aver.setObjectName(u"label_aver")
        self.label_aver.setGeometry(QRect(390, 170, 31, 21))
        self.label_aver.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: white;")
        self.label_aver.setAlignment(Qt.AlignCenter)
        self.label_status = QLabel(self.frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(190, 5, 181, 31))
        self.label_status.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_exit = QPushButton(speccom_mainwin)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(415, 22, 20, 20))
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
        self.pushButton_help = QPushButton(speccom_mainwin)
        self.pushButton_help.setObjectName(u"pushButton_help")
        self.pushButton_help.setGeometry(QRect(390, 22, 20, 20))
        self.pushButton_help.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(100,100,100);\n"
"	background-image: url(:/icons/help.png);\n"
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

        self.retranslateUi(speccom_mainwin)

        QMetaObject.connectSlotsByName(speccom_mainwin)
    # setupUi

    def retranslateUi(self, speccom_mainwin):
        speccom_mainwin.setWindowTitle(QCoreApplication.translate("speccom_mainwin", u"Form", None))
        self.label.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#f0f0f0;\">SpecControl</span></p><p><br/></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Gain</span></p></body></html>", None))
        self.checkBox_bayercorr.setText(QCoreApplication.translate("speccom_mainwin", u"bayer correction", None))
        self.label_16.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Average</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Exposure</span></p></body></html>", None))
        self.pushButton_comrefresh.setText(QCoreApplication.translate("speccom_mainwin", u"refresh", None))
        self.pushButton_comconnect.setText(QCoreApplication.translate("speccom_mainwin", u"connect", None))
        self.label_3.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">source ID:</span></p></body></html>", None))
        self.checkBox_spectrum.setText(QCoreApplication.translate("speccom_mainwin", u"spectrum", None))
        self.checkBox_average.setText(QCoreApplication.translate("speccom_mainwin", u"averaging", None))
        self.pushButton_settings.setText(QCoreApplication.translate("speccom_mainwin", u"settings", None))
        self.pushButton_savespec.setText(QCoreApplication.translate("speccom_mainwin", u"save spectrum", None))
        self.label_9.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#6496c8;\">active analyses tools</span></p></body></html>", None))
        self.pushButton_adddev.setText("")
        self.pushButton_deldev.setText("")
        self.pushButton_saveimg.setText(QCoreApplication.translate("speccom_mainwin", u"save frame", None))
        self.checkBox_grayscale.setText(QCoreApplication.translate("speccom_mainwin", u"grayscale", None))
        self.label_exposure.setText(QCoreApplication.translate("speccom_mainwin", u"-10", None))
        self.label_bright.setText(QCoreApplication.translate("speccom_mainwin", u"0", None))
        self.label_aver.setText(QCoreApplication.translate("speccom_mainwin", u"1", None))
        self.label_status.setText(QCoreApplication.translate("speccom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">waiting</span></p></body></html>", None))
        self.pushButton_exit.setText("")
        self.pushButton_help.setText("")
    # retranslateUi


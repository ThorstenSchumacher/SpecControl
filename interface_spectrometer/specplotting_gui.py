# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'specplotting_gui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPushButton, QSizePolicy, QSlider, QWidget)

from interface_spectrometer.mplwidget_specplotter import MplWidget
import graphics.buttons_rc

class Ui_specplottingwin(object):
    def setupUi(self, specplottingwin):
        if not specplottingwin.objectName():
            specplottingwin.setObjectName(u"specplottingwin")
        specplottingwin.resize(1723, 900)
        specplottingwin.setStyleSheet(u"button->setStyleSheet(\"border-image:url(:/icons/arrow_l.png);\");")
        self.frame = QFrame(specplottingwin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 1700, 881))
        self.frame.setStyleSheet(u"background-color: rgb(50, 49, 52);\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(20, 15, 221, 31))
        self.MplWidget = MplWidget(self.frame)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setGeometry(QRect(19, 49, 1661, 811))
        self.MplWidget.setStyleSheet(u"border-radius: 10px;")
        self.label_28 = QLabel(self.MplWidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(480, 40, 111, 21))
        self.label_28.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_28.setWordWrap(False)
        self.label_27 = QLabel(self.MplWidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(350, 40, 61, 21))
        self.label_27.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_27.setWordWrap(False)
        self.horizontalSlider_axisswitch = QSlider(self.MplWidget)
        self.horizontalSlider_axisswitch.setObjectName(u"horizontalSlider_axisswitch")
        self.horizontalSlider_axisswitch.setEnabled(True)
        self.horizontalSlider_axisswitch.setGeometry(QRect(430, 40, 31, 22))
        self.horizontalSlider_axisswitch.setStyleSheet(u"QSlider{\n"
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
        self.horizontalSlider_axisswitch.setMinimum(0)
        self.horizontalSlider_axisswitch.setMaximum(1)
        self.horizontalSlider_axisswitch.setValue(0)
        self.horizontalSlider_axisswitch.setSliderPosition(0)
        self.horizontalSlider_axisswitch.setTracking(False)
        self.horizontalSlider_axisswitch.setOrientation(Qt.Horizontal)
        self.horizontalSlider_axisswitch.setInvertedAppearance(False)
        self.horizontalSlider_axisswitch.setInvertedControls(False)
        self.comboBox_analysismode = QComboBox(self.MplWidget)
        self.comboBox_analysismode.setObjectName(u"comboBox_analysismode")
        self.comboBox_analysismode.setGeometry(QRect(810, 35, 171, 31))
        self.comboBox_analysismode.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color: rgba(0,0,0,100);\n"
"")
        self.label_29 = QLabel(self.MplWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(710, 40, 101, 21))
        self.label_29.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_29.setWordWrap(False)
        self.pushButton_source = QPushButton(self.MplWidget)
        self.pushButton_source.setObjectName(u"pushButton_source")
        self.pushButton_source.setGeometry(QRect(1000, 35, 131, 31))
        self.pushButton_source.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_source.setCheckable(False)
        self.pushButton_background = QPushButton(self.MplWidget)
        self.pushButton_background.setObjectName(u"pushButton_background")
        self.pushButton_background.setGeometry(QRect(1150, 35, 131, 31))
        self.pushButton_background.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_background.setCheckable(False)
        self.pushButton_zoom = QPushButton(self.MplWidget)
        self.pushButton_zoom.setObjectName(u"pushButton_zoom")
        self.pushButton_zoom.setGeometry(QRect(1500, 150, 41, 41))
        self.pushButton_zoom.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: white;\n"
"	font: 8pt \"MS Shell Dlg 2\";\n"
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
        self.pushButton_zoom.setCheckable(False)
        self.pushButton_home = QPushButton(self.MplWidget)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setGeometry(QRect(1500, 100, 41, 41))
        self.pushButton_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: white;\n"
"	font: 8pt \"MS Shell Dlg 2\";\n"
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
        self.pushButton_home.setCheckable(False)
        self.pushButton_reset = QPushButton(self.MplWidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setGeometry(QRect(1300, 35, 131, 31))
        self.pushButton_reset.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_reset.setCheckable(False)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(240, 160, 16, 16))
        self.frame_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 8px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.alarmframe = QFrame(self.frame_2)
        self.alarmframe.setObjectName(u"alarmframe")
        self.alarmframe.setGeometry(QRect(2, 2, 12, 12))
        self.alarmframe.setStyleSheet(u"background-color: red;\n"
"border-radius: 6px;")
        self.alarmframe.setFrameShape(QFrame.StyledPanel)
        self.alarmframe.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(265, 158, 121, 21))
        self.label_22.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_22.setWordWrap(False)
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(1250, 158, 81, 21))
        self.label_23.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_23.setWordWrap(False)
        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(1390, 158, 41, 21))
        self.label_24.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_24.setWordWrap(False)
        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(1320, 158, 41, 21))
        self.label_25.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setWordWrap(False)
        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(1400, 158, 41, 21))
        self.label_26.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_26.setWordWrap(False)
        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(1360, 158, 21, 21))
        self.label_30.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_30.setWordWrap(False)
        self.label_31 = QLabel(self.frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(1450, 158, 41, 21))
        self.label_31.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_31.setWordWrap(False)
        self.label_32 = QLabel(self.frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(410, 158, 181, 21))
        self.label_32.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_32.setWordWrap(False)
        self.pushButton_mini = QPushButton(self.frame)
        self.pushButton_mini.setObjectName(u"pushButton_mini")
        self.pushButton_mini.setGeometry(QRect(1670, 10, 20, 20))
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

        self.retranslateUi(specplottingwin)

        QMetaObject.connectSlotsByName(specplottingwin)
    # setupUi

    def retranslateUi(self, specplottingwin):
        specplottingwin.setWindowTitle(QCoreApplication.translate("specplottingwin", u"Form", None))
        self.label.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#f0f0f0;\">spectrum: live-view</span></p><p><br/></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">wavelength axis</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">pixel axis</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">analysis mode</span></p></body></html>", None))
        self.pushButton_source.setText(QCoreApplication.translate("specplottingwin", u"source spectrum", None))
        self.pushButton_background.setText(QCoreApplication.translate("specplottingwin", u"background spectrum", None))
        self.pushButton_zoom.setText(QCoreApplication.translate("specplottingwin", u"zoom", None))
        self.pushButton_home.setText(QCoreApplication.translate("specplottingwin", u"home", None))
        self.pushButton_reset.setText(QCoreApplication.translate("specplottingwin", u"reset", None))
        self.label_22.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">ROI not activated</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">cursor: x =</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">y =</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">---</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">---</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">--</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">--</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("specplottingwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">SATURATION ALERT!!!</span></p></body></html>", None))
        self.pushButton_mini.setText("")
    # retranslateUi


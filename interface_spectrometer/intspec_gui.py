# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'intspec_gui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QWidget)

class Ui_intspecpan(object):
    def setupUi(self, intspecpan):
        if not intspecpan.objectName():
            intspecpan.setObjectName(u"intspecpan")
        intspecpan.resize(427, 288)
        intspecpan.setStyleSheet(u"button->setStyleSheet(\"border-image:url(:/icons/arrow_l.png);\");")
        self.frame = QFrame(intspecpan)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 421, 271))
        self.frame.setStyleSheet(u"background-color: rgb(50, 49, 52);\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(20, 7, 281, 31))
        self.label.setStyleSheet(u"background-color: transparent;")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(19, 50, 391, 111))
        self.frame_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_value = QLabel(self.frame_2)
        self.label_value.setObjectName(u"label_value")
        self.label_value.setGeometry(QRect(0, 0, 331, 71))
        self.label_value.setStyleSheet(u"font: 50pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 150, 200);\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 82, 351, 21))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"background-color: rgb(54, 54, 54);\n"
"border: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0397727 rgba(0, 0, 255, 255), stop:1 rgba(255, 0, 255, 255));\n"
"border: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.progressBar.setMaximum(255)
        self.progressBar.setValue(255)
        self.progressBar.setTextVisible(False)
        self.label_unit = QLabel(self.frame_2)
        self.label_unit.setObjectName(u"label_unit")
        self.label_unit.setGeometry(QRect(340, 35, 41, 35))
        self.label_unit.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 150, 200);\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_unit.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.pushButton_getmin = QPushButton(self.frame)
        self.pushButton_getmin.setObjectName(u"pushButton_getmin")
        self.pushButton_getmin.setGeometry(QRect(20, 200, 71, 23))
        self.pushButton_getmin.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(180, 200, 21, 23))
        self.label_19.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_wlmin = QLineEdit(self.frame)
        self.lineEdit_wlmin.setObjectName(u"lineEdit_wlmin")
        self.lineEdit_wlmin.setEnabled(False)
        self.lineEdit_wlmin.setGeometry(QRect(140, 200, 41, 23))
        self.lineEdit_wlmin.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_wlmin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(180, 230, 21, 23))
        self.label_20.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_wlmax = QLineEdit(self.frame)
        self.lineEdit_wlmax.setObjectName(u"lineEdit_wlmax")
        self.lineEdit_wlmax.setEnabled(False)
        self.lineEdit_wlmax.setGeometry(QRect(140, 230, 41, 23))
        self.lineEdit_wlmax.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_wlmax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_getmax = QPushButton(self.frame)
        self.pushButton_getmax.setObjectName(u"pushButton_getmax")
        self.pushButton_getmax.setGeometry(QRect(20, 230, 71, 23))
        self.pushButton_getmax.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}")
        self.pushButton_fullrange = QPushButton(self.frame)
        self.pushButton_fullrange.setObjectName(u"pushButton_fullrange")
        self.pushButton_fullrange.setGeometry(QRect(220, 230, 191, 23))
        self.pushButton_fullrange.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(155, 0, 0);\n"
"	color: white;\n"
"}")
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(100, 200, 41, 23))
        self.label_21.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(100, 230, 41, 23))
        self.label_22.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(230, 200, 61, 21))
        self.label_27.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_27.setWordWrap(False)
        self.horizontalSlider_mode = QSlider(self.frame)
        self.horizontalSlider_mode.setObjectName(u"horizontalSlider_mode")
        self.horizontalSlider_mode.setGeometry(QRect(300, 200, 31, 22))
        self.horizontalSlider_mode.setStyleSheet(u"QSlider{\n"
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
        self.horizontalSlider_mode.setMinimum(0)
        self.horizontalSlider_mode.setMaximum(1)
        self.horizontalSlider_mode.setValue(0)
        self.horizontalSlider_mode.setSliderPosition(0)
        self.horizontalSlider_mode.setOrientation(Qt.Horizontal)
        self.horizontalSlider_mode.setInvertedAppearance(False)
        self.horizontalSlider_mode.setInvertedControls(False)
        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(340, 200, 61, 21))
        self.label_28.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_28.setWordWrap(False)
        self.label_devname = QLabel(self.frame)
        self.label_devname.setObjectName(u"label_devname")
        self.label_devname.setGeometry(QRect(130, 170, 281, 21))
        self.label_devname.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 150, 200);\n"
"")
        self.label_devname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 170, 101, 21))
        self.label_2.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.frame_2.raise_()
        self.label.raise_()
        self.pushButton_getmin.raise_()
        self.label_19.raise_()
        self.lineEdit_wlmin.raise_()
        self.label_20.raise_()
        self.lineEdit_wlmax.raise_()
        self.pushButton_getmax.raise_()
        self.pushButton_fullrange.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_27.raise_()
        self.horizontalSlider_mode.raise_()
        self.label_28.raise_()
        self.label_devname.raise_()
        self.label_2.raise_()

        self.retranslateUi(intspecpan)

        QMetaObject.connectSlotsByName(intspecpan)
    # setupUi

    def retranslateUi(self, intspecpan):
        intspecpan.setWindowTitle(QCoreApplication.translate("intspecpan", u"Form", None))
        self.label.setText(QCoreApplication.translate("intspecpan", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#f0f0f0;\">Integrated intensity</span></p><p><br/></p></body></html>", None))
        self.label_value.setText(QCoreApplication.translate("intspecpan", u"<html><head/><body><p>123456</p></body></html>", None))
        self.label_unit.setText(QCoreApplication.translate("intspecpan", u"<html><head/><body><p><span style=\" font-size:18pt;\">bit</span></p></body></html>", None))
        self.pushButton_getmin.setText(QCoreApplication.translate("intspecpan", u"get min.", None))
        self.label_19.setText(QCoreApplication.translate("intspecpan", u"<html><head/><body><p><span style=\" color:#ffffff;\">nm</span></p></body></html>", None))
        self.lineEdit_wlmin.setText(QCoreApplication.translate("intspecpan", u"400", None))
        self.label_20.setText(QCoreApplication.translate("intspecpan", u"<html><head/><body><p><span style=\" color:#ffffff;\">nm</span></p></body></html>", None))
        self.lineEdit_wlmax.setText(QCoreApplication.translate("intspecpan", u"400", None))
        self.pushButton_getmax.setText(QCoreApplication.translate("intspecpan", u"get max.", None))
        self.pushButton_fullrange.setText(QCoreApplication.translate("intspecpan", u"reset to full range", None))
        self.label_21.setText(QCoreApplication.translate("intspecpan", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">\u03bb </span><span style=\" font-size:10pt; font-weight:600; color:#ffffff; vertical-align:sub;\">min </span><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">=</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("intspecpan", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">\u03bb </span><span style=\" font-size:10pt; font-weight:600; color:#ffffff; vertical-align:sub;\">max </span><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">=</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("intspecpan", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">integrated</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("intspecpan", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#bebebe;\">averaged</span></p></body></html>", None))
        self.label_devname.setText(QCoreApplication.translate("intspecpan", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("intspecpan", u"Device name:", None))
    # retranslateUi


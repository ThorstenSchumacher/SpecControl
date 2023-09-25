# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wlanalyse_gui.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_wlanapan(object):
    def setupUi(self, wlanapan):
        if not wlanapan.objectName():
            wlanapan.setObjectName(u"wlanapan")
        wlanapan.resize(427, 198)
        wlanapan.setStyleSheet(u"button->setStyleSheet(\"border-image:url(:/icons/arrow_l.png);\");")
        self.frame = QFrame(wlanapan)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 421, 181))
        self.frame.setStyleSheet(u"background-color: rgb(50, 49, 52);\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(20, 7, 281, 31))
        self.label.setStyleSheet(u"background-color: transparent;")
        self.pushButton_getwl = QPushButton(self.frame)
        self.pushButton_getwl.setObjectName(u"pushButton_getwl")
        self.pushButton_getwl.setGeometry(QRect(20, 110, 131, 23))
        self.pushButton_getwl.setStyleSheet(u"QPushButton {\n"
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
        self.label_19.setGeometry(QRect(110, 140, 21, 23))
        self.label_19.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.lineEdit_wl = QLineEdit(self.frame)
        self.lineEdit_wl.setObjectName(u"lineEdit_wl")
        self.lineEdit_wl.setEnabled(False)
        self.lineEdit_wl.setGeometry(QRect(70, 140, 41, 23))
        self.lineEdit_wl.setStyleSheet(u"QLineEdit { \n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
" }")
        self.lineEdit_wl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(50, 140, 41, 23))
        self.label_21.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.label_devname = QLabel(self.frame)
        self.label_devname.setObjectName(u"label_devname")
        self.label_devname.setGeometry(QRect(20, 75, 141, 21))
        self.label_devname.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 150, 200);\n"
"")
        self.label_devname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 101, 21))
        self.label_2.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(wlanapan)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(170, 60, 240, 111))
        self.frame_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_value = QLabel(self.frame_2)
        self.label_value.setObjectName(u"label_value")
        self.label_value.setGeometry(QRect(10, 10, 161, 60))
        self.label_value.setStyleSheet(u"font: 50pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 150, 200);\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 82, 200, 21))
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
        self.label_unit.setGeometry(QRect(180, 35, 41, 35))
        self.label_unit.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 150, 200);\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_unit.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.retranslateUi(wlanapan)

        QMetaObject.connectSlotsByName(wlanapan)
    # setupUi

    def retranslateUi(self, wlanapan):
        wlanapan.setWindowTitle(QCoreApplication.translate("wlanapan", u"Form", None))
        self.label.setText(QCoreApplication.translate("wlanapan", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#f0f0f0;\">Wavelength intensity</span></p><p><br/></p></body></html>", None))
        self.pushButton_getwl.setText(QCoreApplication.translate("wlanapan", u"get wavelength", None))
        self.label_19.setText(QCoreApplication.translate("wlanapan", u"<html><head/><body><p><span style=\" color:#ffffff;\">nm</span></p></body></html>", None))
        self.lineEdit_wl.setText(QCoreApplication.translate("wlanapan", u"400", None))
        self.label_21.setText(QCoreApplication.translate("wlanapan", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">\u03bb =</span></p></body></html>", None))
        self.label_devname.setText(QCoreApplication.translate("wlanapan", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("wlanapan", u"Device name:", None))
        self.label_value.setText(QCoreApplication.translate("wlanapan", u"1023", None))
        self.label_unit.setText(QCoreApplication.translate("wlanapan", u"<html><head/><body><p><span style=\" font-size:18pt;\">bit</span></p></body></html>", None))
    # retranslateUi


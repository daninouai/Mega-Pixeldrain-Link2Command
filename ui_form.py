# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(430, 448)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(430, 448))
        Widget.setMaximumSize(QSize(430, 448))
        icon = QIcon()
        icon.addFile(u"icons/icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"background: white;\n"
"color:black;")
        self.input_pixeldrain = QLineEdit(Widget)
        self.input_pixeldrain.setObjectName(u"input_pixeldrain")
        self.input_pixeldrain.setGeometry(QRect(20, 200, 291, 31))
        font = QFont()
        font.setPointSize(10)
        self.input_pixeldrain.setFont(font)
        self.label_pixeldrain = QLabel(Widget)
        self.label_pixeldrain.setObjectName(u"label_pixeldrain")
        self.label_pixeldrain.setGeometry(QRect(20, 170, 81, 21))
        self.label_pixeldrain.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_pixeldrain.setFont(font1)
        self.input_mega = QLineEdit(Widget)
        self.input_mega.setObjectName(u"input_mega")
        self.input_mega.setGeometry(QRect(20, 130, 291, 31))
        self.input_mega.setFont(font)
        self.label_mega = QLabel(Widget)
        self.label_mega.setObjectName(u"label_mega")
        self.label_mega.setGeometry(QRect(20, 100, 101, 21))
        self.label_mega.setMaximumSize(QSize(16777215, 16777215))
        self.label_mega.setFont(font1)
        self.output_command = QTextEdit(Widget)
        self.output_command.setObjectName(u"output_command")
        self.output_command.setGeometry(QRect(20, 250, 391, 181))
        self.output_command.setFont(font1)
        self.output_command.setReadOnly(True)
        self.get_pixeldrain = QPushButton(Widget)
        self.get_pixeldrain.setObjectName(u"get_pixeldrain")
        self.get_pixeldrain.setGeometry(QRect(320, 200, 91, 31))
        self.get_mega = QPushButton(Widget)
        self.get_mega.setObjectName(u"get_mega")
        self.get_mega.setGeometry(QRect(320, 130, 91, 31))
        self.logo_pixeldrain = QLabel(Widget)
        self.logo_pixeldrain.setObjectName(u"logo_pixeldrain")
        self.logo_pixeldrain.setGeometry(QRect(20, 40, 251, 41))
        self.logo_pixeldrain.setPixmap(QPixmap(u"icons/pixeldrain.png"))
        self.logo_pixeldrain.setScaledContents(True)
        self.logo_pixeldrain.setWordWrap(False)
        self.logo_mega = QLabel(Widget)
        self.logo_mega.setObjectName(u"logo_mega")
        self.logo_mega.setGeometry(QRect(290, 40, 121, 41))
        self.logo_mega.setPixmap(QPixmap(u"icons/mega.png"))
        self.logo_mega.setScaledContents(True)
        self.logo_mega.setWordWrap(False)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Mega Pixeldrain Link2Command", None))
        self.input_pixeldrain.setText("")
        self.label_pixeldrain.setText(QCoreApplication.translate("Widget", u"Pixeldrain", None))
        self.input_mega.setText("")
        self.label_mega.setText(QCoreApplication.translate("Widget", u"MEGA", None))
        self.get_pixeldrain.setText(QCoreApplication.translate("Widget", u"Get", None))
        self.get_mega.setText(QCoreApplication.translate("Widget", u"Get", None))
        self.logo_pixeldrain.setText("")
        self.logo_mega.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import ui.icons_rc

class Ui_dlgAbout(object):
    def setupUi(self, dlgAbout):
        if not dlgAbout.objectName():
            dlgAbout.setObjectName(u"dlgAbout")
        dlgAbout.resize(390, 487)
        icon = QIcon()
        icon.addFile(u":/Main/runner_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        dlgAbout.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(dlgAbout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label = QLabel(dlgAbout)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/Main/runner_blue.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lblApplicationTitle = QLabel(dlgAbout)
        self.lblApplicationTitle.setObjectName(u"lblApplicationTitle")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblApplicationTitle.setFont(font)
        self.lblApplicationTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblApplicationTitle)

        self.lblInformation = QLabel(dlgAbout)
        self.lblInformation.setObjectName(u"lblInformation")
        font1 = QFont()
        font1.setPointSize(12)
        self.lblInformation.setFont(font1)
        self.lblInformation.setWordWrap(True)

        self.verticalLayout.addWidget(self.lblInformation)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.butAboutClose = QPushButton(dlgAbout)
        self.butAboutClose.setObjectName(u"butAboutClose")

        self.horizontalLayout.addWidget(self.butAboutClose)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(dlgAbout)

        QMetaObject.connectSlotsByName(dlgAbout)
    # setupUi

    def retranslateUi(self, dlgAbout):
        dlgAbout.setWindowTitle(QCoreApplication.translate("dlgAbout", u"Spurpoint Messaging: About", None))
        self.label.setText("")
        self.lblApplicationTitle.setText(QCoreApplication.translate("dlgAbout", u"Title", None))
        self.lblInformation.setText(QCoreApplication.translate("dlgAbout", u"About Information", None))
        self.butAboutClose.setText(QCoreApplication.translate("dlgAbout", u"Close", None))
    # retranslateUi


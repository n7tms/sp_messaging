# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sp_aprs.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 424)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionPurge_Selected_Messages = QAction(MainWindow)
        self.actionPurge_Selected_Messages.setObjectName(u"actionPurge_Selected_Messages")
        self.actionPurge_ALL_Messages = QAction(MainWindow)
        self.actionPurge_ALL_Messages.setObjectName(u"actionPurge_ALL_Messages")
        self.actionEnter_APRS_API_Key = QAction(MainWindow)
        self.actionEnter_APRS_API_Key.setObjectName(u"actionEnter_APRS_API_Key")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(400, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.butClose = QPushButton(self.groupBox_2)
        self.butClose.setObjectName(u"butClose")

        self.gridLayout.addWidget(self.butClose, 0, 4, 1, 1)

        self.txtCallsign = QLineEdit(self.groupBox_2)
        self.txtCallsign.setObjectName(u"txtCallsign")

        self.gridLayout.addWidget(self.txtCallsign, 0, 0, 1, 1)

        self.butFetch = QPushButton(self.groupBox_2)
        self.butFetch.setObjectName(u"butFetch")

        self.gridLayout.addWidget(self.butFetch, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.butShowAll = QPushButton(self.groupBox_2)
        self.butShowAll.setObjectName(u"butShowAll")

        self.gridLayout.addWidget(self.butShowAll, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.tblMessages = QTableWidget(self.groupBox)
        self.tblMessages.setObjectName(u"tblMessages")

        self.verticalLayout.addWidget(self.tblMessages)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 824, 27))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuMessages = QMenu(self.menubar)
        self.menuMessages.setObjectName(u"menuMessages")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtCallsign, self.butFetch)
        QWidget.setTabOrder(self.butFetch, self.butShowAll)
        QWidget.setTabOrder(self.butShowAll, self.butClose)
        QWidget.setTabOrder(self.butClose, self.tblMessages)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMessages.menuAction())
        self.menuFile.addAction(self.actionDocumentation)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuMessages.addAction(self.actionPurge_Selected_Messages)
        self.menuMessages.addAction(self.actionPurge_ALL_Messages)
        self.menuMessages.addSeparator()
        self.menuMessages.addAction(self.actionEnter_APRS_API_Key)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Spurpoint Messaging", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionPurge_Selected_Messages.setText(QCoreApplication.translate("MainWindow", u"Purge ACK'd Messages", None))
        self.actionPurge_ALL_Messages.setText(QCoreApplication.translate("MainWindow", u"Purge ALL Messages", None))
        self.actionEnter_APRS_API_Key.setText(QCoreApplication.translate("MainWindow", u"Enter APRS API Key", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"APRS Message Handler", None))
        self.groupBox_2.setTitle("")
        self.butClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.txtCallsign.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Call Sign", None))
        self.butFetch.setText(QCoreApplication.translate("MainWindow", u"Fetch Messages", None))
        self.butShowAll.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuMessages.setTitle(QCoreApplication.translate("MainWindow", u"Messages", None))
    # retranslateUi


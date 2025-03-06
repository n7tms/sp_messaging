##############################################################################
# SpurPoint Messaging
#
# sp_messaging.py
# 
# The stand-alone version of Spurpoint's APRS messaging module.
#
#
# Creator: Todd Smith
# Start Date: 2025-03-06
# Version 1.1
#
##############################################################################

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QMessageBox, QSplashScreen, QTableWidgetItem, QAbstractItemView, QTableWidget
from PySide6.QtGui import QPixmap
from database import Database
from ui.sp_aprs_ui import Ui_MainWindow as MainWindowUI
import sys



class MainWindow(QMainWindow):
    def __init__(self, cmdline_dbfile = None):
        super().__init__()
        self.ui = MainWindowUI()
        self.ui.setupUi(self)
        self.db_name = None
        self.remote = False

        # self.settingsmgr = SettingsManager()
        # self.settingsmgr.load_settings()
        self._db_version = '1'
        self.setWindowTitle("Spurpoint Messaging 1.1")

        # Splash Screen ============================================
        # pixmap = QPixmap(u":/Main/spurpoint_logo.png")
        # splash = QSplashScreen(pixmap)
        # splash.show()

        # for i in range(1, 2):
        #     time.sleep(1)  # Simulate loading tasks
        #     splash.showMessage(f"Loading... {i * 10}%")
        #     QApplication.processEvents()
        # if not self.is_active_internet():
        #     self.ui.butVolunteersAPRS.setVisible(False)

        self.ui.actionExit.triggered.connect(self.mnuFileExit_clicked)
        self.ui.actionAbout.triggered.connect(self.mnuFileAbout_clicked)
        self.ui.actionDocumentation.triggered.connect(self.menuFileDoc_clicked)

        self.ui.actionPurge_ALL_Messages.triggered.connect(self.mnuMsgPurgeAll_clicked)
        self.ui.actionPurge_Selected_Messages.triggered.connect(self.mnuMsgPurgeSelected_clicked)
        self.ui.actionEnter_APRS_API_Key.triggered.connect(self.mnuMsgAPIKey_clicked)


    def mnuFileAbout_clicked(self):
        pass


    def menuFileDoc_clicked(self):
        pass


    def mnuMsgPurgeAll_clicked(self):
        pass


    def mnuMsgPurgeSelected_clicked(self):
        pass


    def mnuMsgAPIKey_clicked(self):
        pass


    def mnuFileExit_clicked(self):
        """A menu option to kick-off the exit process.
        
        This calls a companion method that closes the database and
        any open dialog boxes and terminates the application.
        
        For now, it just exits the application.
        """

        # TODO: create a method that handles the graceful shutdown
        QApplication.processEvents()
        QApplication.quit()




def main():

    app = QApplication(sys.argv)

    # TODO: implement a way for the user to select a style
    # app.setStyle("Windows")
    app.setStyle("windowsvista")

    window = MainWindow()
    # window.setWindowFlags(Qt.WindowType.Window)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()    
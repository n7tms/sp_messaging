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

from PySide6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox, QSplashScreen, QTableWidgetItem, QAbstractItemView, QTableWidget, QFrame
from PySide6.QtGui import QPixmap, Qt, QCursor
from database import Database
from ui.sp_aprs_ui import Ui_MainWindow as MainWindowUI
from about import AboutDialog
from settings import SettingsManager
from datetime import datetime
import requests
import sys



class MainWindow(QMainWindow):
    def __init__(self, cmdline_dbfile = None):
        super().__init__()
        self.ui = MainWindowUI()
        self.ui.setupUi(self)
        self.db_name = None
        self.remote = False
        self.showall = False

        # self.settingsmgr = SettingsManager()
        # self.settingsmgr.load_settings()
        self._db_version = '1'
        self.setWindowTitle("Spurpoint Messaging 1.1")
        self.online = True

        # Splash Screen ============================================
        pixmap = QPixmap(u":/Main/spurpoint_logo.png")
        splash = QSplashScreen(pixmap)
        splash.show()

        # for i in range(1, 2):
            # time.sleep(1)  # Simulate loading tasks
            # splash.showMessage(f"Loading... {i * 10}%")
        QApplication.processEvents()
        if not self.is_active_internet():
            result = QMessageBox.critical(self,
                                          "SP Messaging: Internet Required",
                                          "SP Messaging was unable to access the Internet.\nInternet is required to retrieve messages.\n\nOpen anyway?",
                                          QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                self.online = False

        splash.finish(self)
        # End Splash Screen ============================================


        self.ui.actionExit.triggered.connect(self.mnuFileExit_clicked)
        self.ui.actionAbout.triggered.connect(self.mnuFileAbout_clicked)
        self.ui.actionDocumentation.triggered.connect(self.menuFileDoc_clicked)

        self.ui.tblMessages.itemChanged.connect(self.checkbox_click)

        self.ui.actionPurge_ALL_Messages.triggered.connect(self.mnuMsgPurgeAll_clicked)
        self.ui.actionPurge_Selected_Messages.triggered.connect(self.mnuMsgPurgeSelected_clicked)
        self.ui.actionEnter_APRS_API_Key.triggered.connect(self.mnuMsgAPIKey_clicked)

        self.ui.butClose.clicked.connect(self.mnuFileExit_clicked)
        self.ui.butShowAll.clicked.connect(self.butShowAll_click)

        self.ui.statusbar.setFixedHeight(30)


        self.ui.butFetch.clicked.connect(self.butFetch_click)
        if not self.online:
            self.ui.butFetch.setEnabled(False)

        self.setStyleSheet(SettingsManager.WIDGETSTYLES)

        self.db = Database()
        self.populate_fields()


    def is_active_internet(self, node: str="https://www.google.com") -> bool:
        try:
            response = requests.get(node, timeout=3)
            return response.status_code == 200
        except requests.RequestException:
            return False


    def populate_fields(self):
        """Read the data from the APRSmessages database table and fill this form"""

        # prevent changes to the checkboxes while populating the table
        self.refreshing = True

        if self.showall:
            qry = 'select MIdx, Acked as "ACKed", MsgID, MsgTime, MsgSource, MsgMessage as "Message" from APRSMessages order by Acked, MsgTime;'
        else:
            qry = 'select MIdx, Acked as "ACKed", MsgID, MsgTime, MsgSource, MsgMessage as "Message" from APRSMessages where Acked=0 order by MsgTime;'
        rows = self.db.fetch_all(qry)

        # build the table headers from the column names in the database
        # cols = [description[0] for description in self.db.cursor.description]
        cols = ['MIdx', 'ACKed', 'MsgID', 'MsgTime', 'MsgSource', 'Message']
        self.ui.tblMessages.setColumnCount(len(cols))
        self.ui.tblMessages.setRowCount(len(rows))
        self.ui.tblMessages.setHorizontalHeaderLabels(cols)

        # populate the data
        # for each row, fill the data cell by cell
        for r_idx, r_dta in enumerate(rows):
            strikethru = False
            for c_idx, c_name in enumerate(cols):
                value = r_dta.get(c_name,"")

                # if we're in column 1, put a checkbox there instead of the 0 or 1
                if c_idx == 1:
                    checkbox = QTableWidgetItem()
                    checkbox.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    checkbox.setFlags(checkbox.flags() | Qt.ItemIsUserCheckable)
                    checkbox.setCheckState(Qt.Unchecked if value == 0 else Qt.Checked)
                    self.ui.tblMessages.setItem(r_idx,c_idx,checkbox)

                else:
                    self.ui.tblMessages.setItem(r_idx,c_idx,QTableWidgetItem(str(value)))
            
        self.ui.tblMessages.resizeColumnsToContents()
        self.ui.tblMessages.hideColumn(0)   # hides the MIdx field/column

        self.ui.statusbar.showMessage(f"")

        self.refreshing = False


    def butShowAll_click(self):
        if self.showall:
            self.showall = False
            self.ui.butShowAll.setText("Show All")

        else:
            self.showall = True
            self.ui.butShowAll.setText("Hide ACK'd")
        
        self.populate_fields()



    def butFetch_click(self):
        """Poll the aprs.fi website for any new messages."""
        # Validate the user input
        callsign = self.ui.txtCallsign.text().strip()
        if not callsign:
            QMessageBox.information(self, "Spurpoint Messaging: Missing Data", "A call sign is required.",
                                    QMessageBox.Ok, QMessageBox.Ok)
            return

        aprs_api_key = None
        # Fetch API key
        qry = "select value from Preferences where key = 'APRSAPIKey';"
        rows = self.db.fetch_many(1,qry)
        if len(rows) == 1:
            aprs_api_key = rows[0]['value'] 
        if not aprs_api_key:
            QMessageBox.warning(self, "Spurpoint Messaging: Configuration Error", "APRS API key is missing.",
                                QMessageBox.Ok, QMessageBox.Ok)
            return

        # Prepare API URL
        api_url = f"https://api.aprs.fi/api/get?what=msg&dst={callsign}&apikey={aprs_api_key}&format=json"

        try:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            # Fetch messages from the API
            response = requests.get(api_url)
            response.raise_for_status()
            json_output = response.json()

            # Extract messages
            messages = json_output.get('entries', [])
            retrieved_count = len(messages)

            # Prepare data for insertion
            new_messages = []
            for msg in messages:
                msg_id = msg['messageid']
                # Check if the message already exists in the database
                qry = "SELECT MIdx FROM APRSMessages WHERE MsgID = ?;"
                if not self.db.fetch_all(qry, [msg_id]):
                    dt_obj = datetime.fromtimestamp(int(msg['time']))
                    msg_time = dt_obj.strftime("%Y-%m-%d %H:%M")
                    new_messages.append((msg_id, msg_time, msg['srccall'], msg['message'], 0))

            # Insert new messages into the database
            new_count = len(new_messages)
            if new_messages:
                insert_qry = """
                    INSERT INTO APRSMessages (MsgID, MsgTime, MsgSource, MsgMessage, Acked)
                    VALUES (?, ?, ?, ?, ?);
                """
                self.db.execute_many(insert_qry, new_messages)

            # Update the UI
            self.populate_fields()
            self.ui.statusbar.showMessage(f"Retrieved: {retrieved_count}; New: {new_count}")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Spurpoint: Network Error", f"Failed to fetch messages: {e}",
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Spurpoint: Error", f"An error occurred: {e}",
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

        QApplication.restoreOverrideCursor()

    def checkbox_click(self, item: QTableWidgetItem):
        """The user checked the box in the Acked column"""

        # make sure the user clicked in the checkbox and not somewhere else on the row
        # and make sure we're not just refreshing the table
        if item.column() == 1 and not self.refreshing:
            # this is probably irrelevant because we're not going to show the "checked" ones anyway
            status = 1 if item.checkState() == Qt.Checked else 0
            
            # figure out what the MIdx of this row is (it's in column 0)
            mid_item = self.ui.tblMessages.item(item.row(),0)
            mid = int(mid_item.text())

            # change this message to acknowledged in the database
            qry = 'update APRSMessages set Acked=? where MIdx=?;'
            params = [status,mid]
            self.db.execute_query(qry,params)

            # get the messageid and let the user know what happened
            msg_id_item = self.ui.tblMessages.item(item.row(),2)
            msg_id = msg_id_item.text()

            self.populate_fields()
            self.ui.statusbar.showMessage(f"MsgID {msg_id} acknowledged.")


    def mnuFileAbout_clicked(self):
        """Your basic everyday about box
        """

        form = AboutDialog()
        form.exec()


    def menuFileDoc_clicked(self):
        pass


    def mnuMsgPurgeAll_clicked(self):
        """Allow the user to purge from the database ALL messages"""

        result = QMessageBox.question(self,
                                      "Spurpoint Messaging: Purge?",
                                      "This will delete ALL messages from the database.\nThis action cannot be undone.\n\nAre you sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            qry = "delete from APRSMessages;"
            self.db.execute_query(qry)

            self.populate_fields()


    def mnuMsgPurgeSelected_clicked(self):
        """Allow the user to purge from the database the acknowledged messages"""

        result = QMessageBox.question(self,
                                      "Spurpoint Messaging: Purge?",
                                      "This will delete acknowledge messages from the database.\nThis action cannot be undone.\n\nAre you sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            qry = "delete from APRSMessages where Acked=1;"
            self.db.execute_query(qry)

            self.populate_fields()


    def mnuMsgAPIKey_clicked(self):
        """Allow the user to add or change the APRS API Key."""

        # get the current API key if there is one
        aprs_api_key = None
        qry = "select value from Preferences where key = 'APRSAPIKey';"
        rows = self.db.fetch_many(1,qry)
        if len(rows) == 1:
            aprs_api_key = rows[0]['value']

        result, ok = QInputDialog.getText(self,
                                      "Spurpoint Messaging: APRS API",
                                      "Enter the APRS API Key:",
                                      text=aprs_api_key)
        if ok and result:
            if aprs_api_key:
                qry = "update Preferences set value=? where key = 'APRSAPIKey';"
            else:
                qry = "insert into Preferences (key, value) values ('APRSAPIKey', ?);"
            values = [result]
            self.db.execute_query(qry,values)
        


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
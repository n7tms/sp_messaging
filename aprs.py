##############################################################################
# SpurPoint
#
# aprs.py
# 
# A UI to fetch and manage APRS messages.
# Note: This method requires an Internet connection.
# 
# Creator: Todd Smith
# Start Date: 2025-01-23
#
##############################################################################

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QTableWidget
from PySide6.QtGui import Qt
from ui.aprs_mgt_ui import Ui_dlgAPRS as APRSMgtUI
from database import Database
import stylesheet
import requests
from datetime import datetime
from settings import SettingsManager


class APRSMgt(QDialog):
    """A dialog box to fetch and manage APRS messages

    Amateur radio operators have the ability to send "text" messages
    via a protocol APRS. APRS is similar to GPS, but uses amateur
    radio frequencies and radios.
    Volunteers who are properly licensed may send APRS message.
    This class retrieves those messages and allows the user to 
    manage them.
    """

    def __init__(self, parent=None):
        """Instantiate the APRS management class object
        
        Attributes
        ----------
        parent (obj): the QApplication or QDialog calling this dialog box
        """

        super().__init__(parent)
        self.ui = APRSMgtUI()
        self.ui.setupUi(self)

        self.ui.butFetch.clicked.connect(self.butFetch_click)
        self.ui.butClose.clicked.connect(self.butClose_click)
        self.ui.txtCallsign.returnPressed.connect(self.butFetch_click)
        self.ui.lblStatus.setText("")

        self.ui.tblMessages.itemChanged.connect(self.checkbox_click)

        self.ui.lblAttribution.setText("Data Source: aprs.fi  ")


        # allow the table to be sorted by clicking on the headers
        self.ui.tblMessages.setSortingEnabled(True)

        # do not allow the user to edit the table data directly
        # self.ui.tblMessages.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # when clicking in a cell, the entire row is selected
        self.ui.tblMessages.setSelectionBehavior(QTableWidget.SelectRows)

        self.db = Database()

        # refreshing is used as a flag to prevent checkbox updates while populating the table
        self.refreshing = None
        self.populate_fields()

        # set this window's style
        self.setStyleSheet(stylesheet.mgtwindow)

        self.setmgr = SettingsManager()


    def populate_fields(self):
        """Read the data from the APRSmessages database table and fill this form"""

        # prevent changes to the checkboxes while populating the table
        self.refreshing = True

        qry = 'select MIdx, Acked as "ACKed", MsgID, MsgTime, MsgSource, MsgMessage as "Message" from APRSMessages where Acked=0;'
        rows = self.db.fetch_all(qry)

        # build the table headers from the column names in the database
        # cols = [description[0] for description in self.db.cursor.description]
        cols = ['MIdx', 'ACKed', 'MsgID', 'MsgTime', 'MsgSource', 'MsgMessage']
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

        self.ui.lblStatus.setText(f"")

        self.refreshing = False


    def butFetch_click(self):
        """Poll the aprs.fi website for any new messages."""
        # Validate the user input
        callsign = self.ui.txtCallsign.text().strip()
        if not callsign:
            QMessageBox.information(self, "Spurpoint: Missing Data", "A call sign is required.",
                                    QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            return

        # Fetch API key
        aprs_api_key = self.setmgr.get_preference(key="APRSAPIKey")
        if not aprs_api_key:
            QMessageBox.warning(self, "Spurpoint: Configuration Error", "APRS API key is missing.",
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            return

        # Prepare API URL
        api_url = f"https://api.aprs.fi/api/get?what=msg&dst={callsign}&apikey={aprs_api_key}&format=json"

        try:
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
            self.ui.lblStatus.setText(f"Retrieved: {retrieved_count}; New: {new_count}")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Spurpoint: Network Error", f"Failed to fetch messages: {e}",
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Spurpoint: Error", f"An error occurred: {e}",
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)


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
            self.ui.lblStatus.setText(f"MsgID {msg_id} acknowledged.")

    
    def butClose_click(self):
        """The user clicked close. So close the window"""
        self.accept()
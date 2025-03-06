##############################################################################
# SpurPoint
#
# about.py
# 
# The about-this-application dialog box
# 
# Creator: Todd Smith
# Start Date: 2025-01-10
#
##############################################################################

from PySide6.QtWidgets import QDialog
from ui.about_ui import Ui_dlgAbout
from settings import SettingsManager

class AboutDialog(QDialog):  
    """A very basic About dialog box"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dlgAbout() 
        self.ui.setupUi(self)

        self.ui.lblApplicationTitle.setText("Spurpoint Messaging")
        about_text = """Version 1.1
An APRS Messaging Application
        
Retrieve APRS messages from APRS.fi via an API
        
Copyright (c) Todd Smith N7TMS 2025
        """
        self.ui.lblInformation.setText(about_text)

        self.ui.butAboutClose.clicked.connect(self.butAboutClose_click)

        # set this window's style
        self.setStyleSheet(SettingsManager.WIDGETSTYLES)

    
    def butAboutClose_click(self):
        self.accept()
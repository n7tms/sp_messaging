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

from PySide6.QtWidgets import QDialog, QTableWidgetItem
from ui.about_ui import Ui_dlgAbout
import stylesheet

class AboutDialog(QDialog):  
    """A very basic About dialog box"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dlgAbout() 
        self.ui.setupUi(self)

        self.ui.lblApplicationTitle.setText("Spurpoint")
        about_text = """Version 4.2
A runner tracker program.
        
Manually make entries into a database when runners pass checkpoints.
Keep track of runners by course and checkpoint.
Search for runners to find their last location.
        
Copyright (c) Todd Smith N7TMS 2025
        """
        self.ui.lblInformation.setText(about_text)

        self.ui.butAboutClose.clicked.connect(self.butAboutClose_click)

        # set this window's style
        self.setStyleSheet(stylesheet.mgtwindow)

    
    def butAboutClose_click(self):
        self.accept()
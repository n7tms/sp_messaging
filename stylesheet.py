##############################################################################
# SpurPoint
#
# stylesheet.py
# 
# Much of the look and feel of the PySide widgets are customizable, similar
# to the way CSS works with HTML. This file are the styles used throughout
# the application. 
#
# In some future world, many of these settings (colors) would be customizable
# by the user and read from a settings or preferences file.
# 
# Creator: Todd Smith
# Start Date: 2025-01-15
#
##############################################################################

from PySide6.QtWidgets import QWidget
from settings import SettingsManager

setmgr = SettingsManager()
STYLESHEET  = setmgr.get_preference("color_preferences")

def apply_style_button(widget: QWidget):
    pass

def apply_style_text(widget: QWidget):
    pass

def apply_style_label(widget: QWidget):
    pass

def apply_style_dialog(widget: QWidget):
    pass

mainwindow = """
            QMainWindow {
                /* background-color: #8fefcf; */
                background-color: #FBF9F7;
                border: 2px solid #2C3E50;
                border-radius: 8px;
            }
            QMenu {
                border: 1px solid black; /* Adds a border to the menus */
                background-color: white; /* Ensures the menu items are visible */
            }
            QMenu::item {
                padding: 5px; /* Adds padding for better appearance */
            }
            QMenu::item:selected {
                background-color: #F7D117; /* Highlight for selected menu items */
            }        """

mgtwindow = """
            QDialogWindow {
                background-color: #FBF9F7;
                border: 2px solid black;
                border-radius: 8px;
            }
            QMenu {
                border: 1px solid black; /* Adds a border to the menus */
                background-color: #FBF9F7; /* Ensures the menu items are visible */
            }
            QMenu::item {
                padding: 5px; /* Adds padding for better appearance */
            }
            QMenu::item:selected {
                background-color: lightgray; /* Highlight for selected menu items */
            }

            QPushButton {
                background-color: #2C3E50;  /* deep blue */
                color: #FBF9F7;             /* snowy white */
                border: 1px solid #373435;  /* dark gray */
                border-radius: 5px;       
                padding: 8px 16px;        
                font-weight: bold;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #415162;
                color: #FBF9F7;
            }

            QPushButton:pressed {
                background-color: #F7921E;  /* carrot orange */
                color: #2C3E50;             /* deep blue */
                border: 1px solid #003f73; /* Darker border */
                padding-top: 11px;         /* Slight push effect */
                padding-bottom: 5px;       /* Adjust padding for press effect */
            }
            QPushButton:disabled {
                background: #cccccc;       /* Light grey background */
                color: #777777;            /* Muted text */
                border: 1px solid #aaaaaa; /* Grey border */
            }

            QLineEdit {
                background-color: #FBF9F7;   /* White background */
                border: 1px solid #2C3E50;  /* Light grey border */
                border-radius: 5px;         /* Rounded corners */
                padding: 4px 8px;           /* Padding for text */
                font-size: 14px;            /* Font size */
            }

            QLineEdit:focus {
                border: 2px solid #F7921E;  /* orange border on focus */
                background-color: #FBF9F7;  /* snowy white background on focus */
            }

            QLineEdit:disabled {
                background-color: #f5f5f5;  /* Light grey for disabled */
                color: #a0a0a0;             /* Muted text color */
            }        

            QTextEdit {
                background-color: #FBF9F7;   /* White background */
                border: 1px solid #2C3E50;  /* Light grey border */
                border-radius: 5px;         /* Rounded corners */
                padding: 4px 8px;           /* Padding for text */
                font-size: 14px;            /* Font size */
            }

            QTextEdit:focus {
                border: 2px solid #F7921E;  /* orange border on focus */
                background-color: #FBF9F7;  /* snowy white background on focus */
            }

            QTextEdit:disabled {
                background-color: #f5f5f5;  /* Light grey for disabled */
                color: #a0a0a0;             /* Muted text color */
            }        
            
            QTableWidget::item:selected {
                background: yellow;
                color: black;              /* black text */
            }
            """



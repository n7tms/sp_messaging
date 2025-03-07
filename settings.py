##############################################################################
# SpurPoint
#
# settings.py
# 
# A class to manage all of the settings, including the recent menu
# 
# Creator: Todd Smith
# Start Date: 2025-01-13
#
##############################################################################

import json
import os
from PySide6.QtWidgets import QMessageBox

class SettingsManager:
    """A class to manage the settings file"""

    def __init__(self, file_path: str='sp_messaging.set'):
        """Instantiate the Settings Manager
        
        If a file path is not specified, we'll create one with some default settings.

        The preferences are kept in memory in the self.settings variable in JSON format.
        When changes are made, the variable is written to a file.
        
        Parameters:
        file_path (str): the path to the settings file, default='SpurPoint.set'
        """

        self.file_path = file_path 
        self.settings = {
            "preferences": {
                "color_scheme": "light",  # Or "dark" depending on the current theme
                "units": "imperial",  # Can be "imperial" or "metric"
                "APRSAPIKey": "",
                "DatabasePath": "",
                "LocalTime": True,
                "UTCTime": False,
                "DateTimeFormat": "yyyy-MM-dd hh:mm:ss",
                }
            }
        

        self.load_settings()


    def load_settings(self):
        """Load the preferences from the settings file
        
        If, for whatever reason, the file cannot be read, SpurPoint uses the
        defaults we already established when the class was instantiated."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    self.settings = json.load(f)
            except json.JSONDecodeError:
                print("The settings file is corrupted. Loading defaults.")
                QMessageBox.information(None,"SpurPoint: Settings Error", "Settings file is corrupted. Loading defaults.",QMessageBox.StandardButton.Ok)


    def save_settings(self):
        """Write the contents of the self.settings variable to a file"""

        with open(self.file_path, "w") as f:
            json.dump(self.settings, f, indent=4)

        self.load_settings()


    def get_recent_files(self) -> list:
        """Retrieve the list of recent files from the settings variable
        
        returns:
        (list): of recent files
        """

        return self.settings.get("recent_files", [])



    def update_preference(self, key: str, value: any):
        """Update a preference value
        
        Parameters:
        key (str): the key or name of the setting
        value (any): the value of that setting
        """

        preferences = self.settings.setdefault("preferences", {})
        preferences[key] = value
        self.save_settings()


    def get_preference(self, key: str) -> any:
        """Retrieve a preference from the settings
        
        Parameters:
        key (str): the key to the setting we want the value for
        """

        return self.settings.get("preferences", {}).get(key)
    

    WIDGETSTYLES = """
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
                text-transform: uppercase;
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
                background: #F7921E;
                color: black;              /* black text */
            }
            QStatusBar {
                background: #e0e0e0; /* Light gray background */
                border: 1px solid gray; /* Border for visibility */
                padding: 5px; /* Adds spacing inside */
                font-size: 12px;
            }
            QMenuBar {
                background-color: #FBF9F7; /* Snowy white background */
                color: #2C3E50; /* Deep blue text */
                /* border: 1px solid #373435; /* Dark gray border */
                padding: 3px; /* Adds spacing inside */
            }

            QMenuBar::item {
                background-color: transparent; /* No background on menu items */
                padding: 1px 10px; /* Padding for better appearance */
            }

            QMenuBar::item:selected {
                background-color: #F7921E; /* Carrot orange for selected item */
                color: black; /* Black text for visibility */
            }

            QMenu {
                background-color: #FBF9F7; /* Snowy white background */
                border: 1px solid #373435; /* Dark gray border */
            }

            QMenu::item {
                background-color: transparent; /* Transparent background for items */
                padding: 5px 10px; /* Padding for better item separation */
            }

            QMenu::item:selected {
                background-color: #F7921E; /* Carrot orange for selected item */
                color: black; /* Black text when selected */
            }

            QMenu::item:disabled {
                background-color: #f5f5f5; /* Light grey background for disabled */
                color: #a0a0a0; /* Muted text color for disabled items */
            }

            QMenu::separator {
                background-color: #2C3E50; /* Deep blue separator line */
                height: 1px; /* Thickness of the separator */
                margin: 5px 0; /* Adds space around the separator */
            }
            #groupBoxTitle {
                border: none; /* Removes the border */
                padding: 20px 1px 1px 1px;
            }


            """

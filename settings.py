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

    def __init__(self, file_path: str='spurpoint.set'):
        """Instantiate the Settings Manager
        
        If a file path is not specified, we'll create one with some default settings.

        The preferences are kept in memory in the self.settings variable in JSON format.
        When changes are made, the variable is written to a file.
        
        Parameters:
        file_path (str): the path to the settings file, default='SpurPoint.set'
        """

        self.file_path = file_path 
        self.settings = {
            "recent_files": [],
            "preferences": {
                "color_scheme": "light",  # Or "dark" depending on the current theme
                "units": "imperial",  # Can be "imperial" or "metric"
                "APRSAPIKey": "",
                "DatabasePath": "",
                "BackupPath": "",
                "NumRecentFiles": 5,
                "BackupOnExit": False,
                "UnitsImperial": True,
                "UnitsMetric": False,
                "LocalTime": True,
                "UTCTime": False,
                "LatLongAbsolute": True,
                "LatLongRelative": False,
                "DateTimeFormat": "yyyy-MM-dd hh:mm:ss",
                "ServerIP": "127.0.0.1",
                "ServerPort": 38873,
                "ImageServerIP": "127.0.0.1",
                "ImageServerPort": 38874,
                
                # Color preferences for different widgets
                "color_preferences": {
                    "QLabel": {
                        "background-color": "#ffffff",
                        "color": "#ffffff",
                        "border": "1px solid #ffffff"
                    },
                    "QLineEdit": {
                        "background-color": "#ffffff",
                        "color": "#ffffff",
                        "border": "1px solid #ffffff"
                    },
                    "QLineEdit:focus": {
                        "background-color": "#ffffff",
                        "color": "#ffffff",
                        "border": "1px solid #ffffff"
                    },
                    "QPushButton": {
                        "background-color": "#ffffff",
                        "color": "#ffffff",
                        "border": "1px solid #ffffff"
                    },
                    "QPushButton:hover": {
                        "background-color": "#ffffff",
                        "color": "#ffffff",
                        "border": "1px solid #ffffff"
                    },
                    "QPushButton:pressed": {
                        "background-color": "#ffffff",
                        "color": "#ffffff",
                        "border": "1px solid #ffffff"
                    },
                    "QDialog": {
                        "background-color": "#ffffff",
                        "border": "1px solid #ffffff"
                    },
                    "QStatusBar": {
                        "background-color": "#ffffff",
                        "color": "#ffffff"
                    }
                }
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


    def add_recent_file(self, event_name: str, file_path: str):
        """This methods adds a file path to the recent files list
        
        Parameters:
        file_path (str): the path to be added to the list
        """

        # get the list of current recent files
        recent_files = self.settings.setdefault("recent_files", [])

        # if this file is already in the list, move it to the top
        found = None
        for en,fp in recent_files:
            if file_path == fp:
                found = [en,fp]
                break
        if found:
            recent_files.remove(found)
        recent_files.insert(0, [event_name,file_path])

        self.settings["recent_files"] = recent_files[:self.get_preference("NumRecentFiles")]
        self.save_settings()

    
    def remove_recent_file(self, file_path: str):
        """This method removes a file path from the recent file list.
        
        It would be used in the case of database file being manually deleted.
        
        Parameters:
        file_path (str): the path of the file to be removed from the list
        """
        
        # get the list of current recent files
        recent_files = self.settings.setdefault("recent_files", [])

        # if this filename is in the list, remove it
        found = None
        for en,fp in recent_files:
            if file_path == fp:
                found = [en,fp]
                break
        if found:
            recent_files.remove(found)



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
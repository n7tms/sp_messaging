# Spurpoint Messaging
## Overview
In an effort to remain compliant with the APRS.fi API usage guidelines, I have removed 
the APRS messaging features from Spurpoint. My intention is to offer Spurpoint Messaging
as a free product.  
  
When it was part of Spurpoint, the reports and messages needed to be manually copied
from the APRS module into the respective Sighting or Messaging module. So, by 
separating the APRS module out, no functionality is lost.  


## Menu
File
 | Documentation
 | About
 | -----------
 | Exit

Messages
 | Enter APRS API Key
 | Purge Selected Messages
 | Purge All Messages


## TODO List
- [ ] create a dialog box for the user to enter the APRS API key
- [ ] store the key in the database
- [ ] add functionality to purge the database of existing messages
- [ ] add functionality to delete selected messages from the database
- [ ] modify the Spurpoint logo to create a similar logo for Messaging
- [ ] modify the Spurpoint website to create a space for the Messaging application
- [ ] Enter in call sign box activates Fetch Messages button
- [ ] force text to all-caps in call sign field
- [ ] Change delete Ack'd to set a purge flag in the field
- [ ] Change purge all to just delete the messages with the purge flag set.
- [ ] 


## TODone List
- [x] modify the migrated Spurpoint About to be a Spurpoint Messaging About
- [x] change the database schema to handle settings and the APRS messages
- [x] hard code the css
- [x] change the APRS dialog to a Main Window



### PyInstaller (One File)
>>> pyinstaller --onefile --windowed --add-data "ui/icons.qrc;." spurpoint.py  
>>> pyinstaller --onefile --windowed --add-data "ui/icons.qrc;." main.py  
(*Replace the ; with : on linux.*)  

### PyInstaller (for packaging)
>>> pyinstaller --windowed --add-data "ui/icons.qrc;." spurpoint.py
(*Replace the ; with : on linux.*)  


### pyside6-deploy
>>> pyside6-deploy main.py
>>> pyside6-deploy -c pysidedeploy.spec
# TFT35Translate
## WARNING: This repository is not fully functional and may be depricated in favor of a WebSocket version to directly translate Klipper's "RepRap-ish" gcode to the display
A small python script to use the touchscreen mode of the BTT TFT35 E3 with Klipper via Raspberry Pi GPIO pins and Moonraker API Requests.
## Prerequisites 
Run sudo raspi-config

under interface options, select the serial port

disable login shell, enable serial hardware


## Installation
First, move into the home directory by executing this command:

cd ~/

Clone the repository using this command:

Git Clone  https://github.com/wil-sys/TFT35Translate.git

Move into the programs directory using this command:

cd TFT35Translate

Edit the "config.py" to be accurate to your printer using this command:

sudo nano config.py

When youre done, press Control X, Y, then enter to save and exit the document 

Give permissions and Execute the install script

chmod +x TFT35Install.sh

./TFT35Install.sh

Reboot your system, then you're done!

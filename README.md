# TFT35Translate
A small python script to use the touchscreen mode of the BTT TFT35 E3 with Klipper via Raspberry Pi GPIO pins and Moonraker API Requests.

## Installation
Clone the repository using this command:
Git Clone  https://github.com/wil-sys/TFT35Translate.git

Add service file
sudo nano /etc/systemd/system/TFT35Translate.service

Add the following to the file

[Unit]

Description=TFT35 -> Moonraker translation service by Wil-Sys

After=multi-user.target

[Service]

Type=simple

Restart=always

ExecStart=/usr/bin/python3 /home/"$USER"/TFT35Translate/TFT35.py

WantedBy=multi-user.target


Press Control + X, then Y, and finally enter

Move into the directoty using 

cd TFT35Translate

Execute install script

./TFT35install.sh

Reboot your system, then you're done!

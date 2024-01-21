# TFT35Translate
A small python script to use the touchscreen mode of the BTT TFT35 E3 with Klipper via Raspberry Pi GPIO pins and Moonraker API Requests.

## Installation
Clone the repository using this command:
Git Clone  https://github.com/wil-sys/TFT35Translate.git

Add service file
sudo nano /etc/systemd/system/TFT35Translate.service

Add the following to the file

[Unit]
Description=TFT35Translate service by wil-sys

After=network.target


[Service]

Type=simple

ExecStart=/bin/bash /home/"$USER"/TFT35Translate/Start.sh

ExecStop=/bin/bash /home/"$USER"/TFT35Translate/Stop.sh

Restart=always

RestartSec=5

TimeoutSec=60

RuntimeMaxSec=infinity

PIDFile=/tmp/name_script.pid

[Install]

WantedBy=multi-user.target

Press Control + X, then Y, and finally enter

Move into the directoty using 

cd TFT35Translate

Execute install script

./TFT35install.sh

Reboot your system, then you're done!

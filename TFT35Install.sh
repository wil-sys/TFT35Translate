echo TFT35Translate install script by Wil-Sys https://github.com/wil-sys
echo TFT35Translate installing python dependancies...
sudo apt install python3
sudo python3 -m /home/"$USER"/TFT35Translate/venv
sudo /home/"$USER"/TFT35Translate/venv/bin/pip install pyserial
sudo /home/"$USER"/TFT35Translate/venv/bin/pip install requests
sudo adduser "$USER" dialout
echo TFT35Translate Starting service...
sudo systemctl daemon-reload
sudo systemctl enable TFT35Translate.service
sudo systemctl start TFT35Translate.service
echo TFT35Translate install finished!
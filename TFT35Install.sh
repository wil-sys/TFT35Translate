echo TFT35Translate install script by Wil-Sys https://github.com/wil-sys
echo TFT35Translate installing python dependancies...
sudo pip3 install pyserial
pip install requests
sudo adduser "$USER" dialout
echo TFT35Translate Adding python script as service...
cat <<EOF >/etc/systemd/system/TFT35Translate.service
[Unit]
Description=TFT35 -> Moonraker translation service by Wil-Sys
After=multi-user.target[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/"$USER"/TFT35Translate/TFT35.py
WantedBy=multi-user.target
EOF
echo TFT35Translate Starting service...
sudo systemctl daemon-reload
sudo systemctl enable TFT35Translate.service
sudo systemctl start TFT35Translate.service
echo TFT35Translate install finished!
echo TFT35Translate install script by Wil-Sys https://github.com/wil-sys
echo TFT35Translate installing python dependancies...
sudo apt install python3
sudo python3 -m /home/"$USER"/TFT35Translate/venv
sudo /home/"$USER"/TFT35Translate/venv/bin/pip install pyserial
sudo /home/"$USER"/TFT35Translate/venv/bin/pip install requests
sudo adduser "$USER" dialout
echo TFT35Translate adding service files...
touch Start.sh
cat << EOF > Start.sh
#!/bin/bash
/usr/bin/python /home/"$USER:/TFT35Translate/TFT35.py
EOF
sudo chmod a+x Start.sh
touch Stop.sh
cat << EOF > Stop.sh
#!/bin/bash
for KILLPID in 'ps ax | grep "TFT35" | awk "{print $1;}"'; do
kill -9 $KILLPID;
done
EOF
sudo chmod a+x Stop.sh
echo TFT35Translate Starting service...
sudo systemctl enable /etc/systemd/system/TFT35Translate.service
sudo systemctl daemon-reload
sudo TFT35Translate.service start
echo TFT35Translate install finished!
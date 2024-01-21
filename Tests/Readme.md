Test programs to ensure your serial interface is working

SerialLoopback Test:
Put a jumper across GPIO 14 and GPIO 15 and then execute the program

SerialAdapter Test:
Attach a serial to USB adapter's TX to GPIO 15 and it's RX to GPIO 14, set the baud rate to 115200, and ensure you are using a program that supports writing to serial interfaces (PuTTY will not work)
Execute the program, and follow it's instructions

If either of these Tests fail:
Execute "Sudo raspi-config" and under "Interface options" disable serial port shell messages, and enable serial port hardware
If you are on a Raspberry Pi 3 model B, B+, 4, or Zero W the required PL011 UART controller is used for the bluetooth modem by default, for this program to work you must disable bluetooth
To disable bluetooth:
Add the following line to the end of your boot/boot.txt 
dtoverlay=disable-bt
Execute the following command on the terminal
sudo systemctl disable hciuart
Then run Sudo reboot  and retry the test

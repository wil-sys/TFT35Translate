import serial

RS232 = serial.Serial('/dev/serial0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

print("TFT35Translate Serial Adapter test by Wil-Sys")
UserInput = input("Connect your serial adapter's TX to GPIO 15, and the adapter's RX to GPIO 14 | Once you have done that, enter 'Y' to continue... ")
while True:
  if UserInput == "Y":
    RS232.write("TFT35Translate Serial Adapter test, if you can see this, type 'Y'")
    BytesIn = RS232.inWaiting()
    if BytesIn > 0:
      print("TFT35Translate Serial adapter test completed!")

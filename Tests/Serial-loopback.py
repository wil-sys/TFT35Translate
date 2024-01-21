import serial
import time

Retrys = 5
Increment = 0
Successes= 0
RS232 = serial.Serial('/dev/serial0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

print("TFT35Translate Serial Loopback test script by Wil-Sys")
while True:
  if Increment < Retrys:
    print("Sending Test Message...")
    RS232.Write("TFT35Translate-LoopbackTest")
    time.sleep(0.1)
    print("Receiving by 1024 bytes...")
    Recv = RS232.Read(1024)
    if Recv == "TFT35Translate-LoopbackTest":
      print("Loopback Succeeded! | Attempt number " + str(Increment) + "of " + str(Retrys))
      Successes += 1
      Increment += 1
      time.sleep(1)
    else:
      print("Loopback Test Failed! | Attempt number " + str(Increment) + "of " + str(Retrys))
      Increment += 1
      time.sleep(1)
  else:
    print("Loopback test concluded. | out of " + str(Retrys) + " Attempts, " + str(Successes) + " Completed Successfully")



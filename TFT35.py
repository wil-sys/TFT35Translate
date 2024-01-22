import serial
import requests
import json

def read_data_into_var():
  TEMP1 = RS232.read(128)
  print("TEMP1:" + str(TEMP1))
  SerialData = str(TEMP1)
  RS232.reset_output_buffer()

RS232 = serial.Serial('/dev/serial0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
Success = 0
SerialData = ""
MoonrakerURL = input("Please enter your host IP address")
while True:
    BytesIn = RS232.inWaiting()
    if BytesIn > 0:
      Success = 0
      read_data_into_var
      print(SerialData)
      if (SerialData) == "M105":
        r = requests.get(MoonrakerURL + "/api/printer")
        status = json.loads(r.json())
        print(status)
        RS232.write("ok T:" + str((status)["temperature"]["tool0"]["actual"]) + " / " + str((status)["temperature"]["tool0"]["target"]) + " B:" + str((status)["temperature"]["bed"]["actual"]) + " / " + str((status)["temperature"]["bed"]["target"]) + "@:0 B@:0")
      else:
          while (Success) == 0 :
           r = requests.post((MoonrakerURL), data= "/printer/gcode/script?script=" + (SerialData))
           r = requests.get(MoonrakerURL)
           if r.text == "ok":
            print("ok")
            RS232.write("ok")
            Success = 1
    else:
      print("NO SERIAL DATA!")
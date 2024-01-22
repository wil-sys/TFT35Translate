import serial
import requests
import json
import time

def read_data_into_var():
  TEMP1 = RS232.read(128)
  print("TEMP1:" + TEMP1.decode("uft-8"))
  SerialData = TEMP1.decode("utf-8")
  RS232.reset_input_buffer()

MoonrakerURL = "http://192.168.2.46:7125"
RS232 = serial.Serial('/dev/serial0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
Success = 0
SerialData = ""
while True:
    BytesIn = RS232.inWaiting()
    if BytesIn > 0:
      Success = 0
      read_data_into_var()
      print(SerialData)
      if (SerialData) == "M105":
         print("Received M105")
         r = requests.get(MoonrakerURL + "/api/printer")
         status = json.loads(r.json())
         print(status)
         RS232.write("ok T:" + str((status)["temperature"]["tool0"]["actual"]) + " / " + str((status)["temperature"]["tool0"]["target"]) + " B:" + str((status)["temperature"]["bed"]["actual"]) + " / " + str((status)["temperature"]["bed"]["target"]) + "@:0 B@:0")
      else:
          while Success == 0:
             print("Sending Data")
             r = requests.post(MoonrakerURL + "/printer/gcode/script", params={"script": SerialData})
             r = requests.get(MoonrakerURL)
             if r.status_code == 200:
               print("ok")
               RS232.write("ok")
               Success = 1
    else:
        print("NO SERIAL DATA!")
time.sleep(0.1)
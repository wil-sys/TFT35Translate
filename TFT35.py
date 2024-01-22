import serial
import requests
import json
import time

MoonrakerURL = "http://192.168.2.46:7125"
RS232 = serial.Serial('/dev/serial0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
Success = 0
SerialData = ""

def read_data_into_var():
    SerialData = RS232.readline().decode("utf-8").strip()
    RS232.reset_input_buffer()
    return SerialData

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
         response = "ok T:{}/{} B:{}/{} @:0 B@:0".format(
                status["temperature"]["tool0"]["actual"],
                status["temperature"]["tool0"]["target"],
                status["temperature"]["bed"]["actual"],
                status["temperature"]["bed"]["target"]
            )
         RS232.write(response.encode('utf-8'))
      else:
          while Success == 0:
             print("Sending Data")
             r = requests.post(MoonrakerURL + "/printer/gcode/script", params={"script": SerialData})
             r = requests.get(MoonrakerURL)
             if r.status_code == 200:
               print("ok")
               TEMP2 = bytes("ok", 'utf-8')
               RS232.write(TEMP2)
               Success = 1
time.sleep(0.1)
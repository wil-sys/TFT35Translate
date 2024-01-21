import serial
import requests
import json 

def read_data_into_var():
  TEMP1 = pmd.read(128)
  print("TEMP1:" + str(TEMP1))
  SerialData = str(TEMP1)
  RS232.reset_output_buffer()

RS232= serial.Serial('/dev/serial0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
MoonrakerURL = "127.0.0.1"
Success = 0
SerialData = ""

while True:
    if RS232.inWaiting() > 1:
      read_data_into_var
      print(SerialData)
      if (SerialData) == "M105":
        r = requests.get(MoonrakerURL + "/api/printer")
        status = json.loads(r.json())
        print(status)
        RS232.Write("ok T:" + str((status)["temperature"]["tool0"]["actual"]) + " / " + str((status)["temperature"]["tool0"]["target"]) + " B:" + str((status)["temperature"]["bed"]["actual"]) + " / " + str((status)["temperature"]["bed"]["target"]) + "@:0 B@:0")
      else:
          while (Success) == 0 :
           r = requests.post((MoonrakerURL), data= "/printer/gcode/script?script=" + (SerialData))
           r = requests.get(MoonrakerURL)
           if r.text == "ok":
            print("ok")
            RS232.Write("ok")
            Success = 1
    else:
      Print(NO SERIAL DATA!)
Success = 0
      
      
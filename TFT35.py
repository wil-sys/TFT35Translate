import serial
import requests
import json
import time
import config

RS232 = serial.Serial('/dev/serial0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
Success = 0
SerialData = ""
Startup= 0

while Startup == 0:
    r = requests.get(config.MoonrakerURL + "/server/info")
    StartupStatus = r.json()
    StartupConnected = StartupStatus["result"]["klippy_connected"]
    if str(StartupConnected) == "True":
        Startup = 1
        #PUT DEFAULT TFT35 INIT GCODES HERE

while True:
    time.sleep(0.1)
    BytesIn = RS232.inWaiting()
    if BytesIn > 0:
      Success = 0
      SerialData = RS232.readline().decode("utf-8").strip()
      RS232.reset_input_buffer()
      print(SerialData)
      if SerialData == "M105":
         print("Received M105")
         r = requests.get(config.MoonrakerURL + "/api/printer")
         status = r.json()
         print(status)
         response = "ok T:{:.2f}/{:.2f} B:{:.2f}/{:.2f} @:0 B@:0".format(
                status["temperature"]["tool0"]["actual"],
                status["temperature"]["tool0"]["target"],
                status["temperature"]["bed"]["actual"],
                status["temperature"]["bed"]["target"]
            )
         RS232.write((response + '\n').encode('utf-8'))
         print(response)
         print((response.encode('utf-8')))
      elif SerialData == "M503":
         print("Received M503")
         M92 = "M92 X{:.2f} Y{:.2f} Z{:.2f} E{:.2f}".format(
            config.StepsPerMM["X"],
            config.StepsPerMM["Y"],
            config.StepsPerMM["Z"],
            config.StepsPerMM["E"]
         )
         M203 = "M203 X{:.2f} Y{:.2f} Z{:.2f} E{:.2f}".format(
            config.MaxFeedrate["X"],
            config.MaxFeedrate["Y"],
            config.MaxFeedrate["Z"],
            config.MaxFeedrate["E"]
         )
         M201 = "M201 X{:.2f} Y{:.2f} Z{:.2f} E{:.2f}".format(
            config.MaxAcceleration["X"],
            config.MaxAcceleration["Y"],
            config.MaxAcceleration["Z"],
            config.MaxAcceleration["E"]
         )
         M206 = "M206 X{:.2f} Y{:.2f} Z{:.2f}".format(
            config.HomeOffsets["X"],
            config.HomeOffsets["Y"],
            config.HomeOffsets["Z"]
         )
         M666 = "M666 X{:.2f} Y{:.2f} Z{:.2f}".format(
            config.EndstopOffsets["X"],
            config.EndstopOffsets["Y"],
            config.EndstopOffsets["Z"]
         )
         print(M92)
         print(M203)
         print(M201)
         print(M206)
         print(M666)
         RS232.write((M92 + "\n").encode('utf-8'))
         RS232.write((M203 + "\n").encode('utf-8'))
         RS232.write((M201 + "\n").encode('utf-8'))
         RS232.write((M206 + "\n").encode('utf-8'))
         RS232.write((M666 + "\n").encode('utf-8'))
         Print("Sent M503 Response")
      else:
          while Success == 0:
             print("Sending Data")
             r = requests.post(config.MoonrakerURL + "/printer/gcode/script", data={"script": SerialData})
             r = requests.get(config.MoonrakerURL)
             if r.status_code == 200:
               print("ok")
               TEMP2 = bytes("ok\n", 'utf-8')
               RS232.write(TEMP2)
               Success = 1

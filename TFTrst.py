from gpiozero import LED
import time

RSTpin = LED(18,active_high=False)
def init():
    RSTpin = LED(18,active_high=False)
    RSTpin.off()

def ResetTFT():
    RSTpin.on()
    time.sleep(0.1)
    RSTpin.off()

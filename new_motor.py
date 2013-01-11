"""import sys
sys.path.append("../..")
import time

import arduino

ard = arduino.Arduino()
m0 = arduino.Motor(ard,5)
dir_m0=arduino.DigitalOutput(ard,4)
ard.run()  # Start the Arduino communication thread

while True:
    m0.setSpeed(127)
    dir_m0.setValue(0)"""

import sys
sys.path.append("../..")
import time

import arduino

ard = arduino.Arduino()
m0 = arduino.Motor(ard, 0, 4, 5)
ard.run()  # Start the Arduino communication thread

while True:
    m0.setSpeed(10)
    #time.sleep(1)
    #m0.setSpeed(0)
    #time.sleep(1)
    #m0.setSpeed(-127)
    #time.sleep(1)
    #m0.setSpeed(0)
    #time.sleep(1)

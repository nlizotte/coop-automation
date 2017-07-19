import sys
sys.path.append('../../')
from Adafruit_MotorHAT import Adafruit_MotorHAT
from flask import Flask
application = Flask(__name__)

mh = Adafruit_MotorHAT(addr=0x60)


myStepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
myStepper.setSpeed(30)

@application.route("/open")
def open_door():
    myStepper.step(300, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

if __name__ == "__main__":
    application.run(host='0.0.0.0')

# ROBOT SETUP  --  defined ONCE here, used by every run.
# Edit this file if you change a port or the drive settings.

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button

hub = PrimeHub()


hub.system.set_stop_button(None) 
# OR assign stopping to another combination like left + right
hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

hub = PrimeHub()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)
robot = DriveBase(left_motor, right_motor, wheel_diameter=63, axle_track=112)
robot.settings(420, 300, 180, 200)

# Attachment motors.  Port A = hook / spotlight spinner,  Port E = speaker / plow.
hook = Motor(Port.A)
plow = Motor(Port.E)

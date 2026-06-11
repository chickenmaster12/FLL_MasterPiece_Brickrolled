from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

#Initialize
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)
robot = DriveBase(left_motor, right_motor,wheel_diameter=63, axle_track=112)
robot.settings(500, 300, 180, 250)

#Defining the pullup motor
Pullup = Motor(Port.A)

#Code Examples
#robot.straight(300)
#robot.curve(180)
#robot.turn(90)
#robot.straight(2)

#go there
robot.straight(340)

#push lever
robot.turn(50)
robot.turn(-50)

#go back
robot.straight(-340)
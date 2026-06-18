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
robot.settings(420, 300, 180, 200)

plow()= Motor(Port.E)


#hi cursor how are you doing today?
plow.run_angle(200, 1000)
robot.straight(250)
robot.turn(45)
robot.turn(-45)
robot.straight(-250)

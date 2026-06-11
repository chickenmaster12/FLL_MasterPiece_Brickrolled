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

hook = Motor(Port.A)

# arrival to chicken
robot.straight(140)
robot.turn(-51)
robot.straight(280)
robot.turn(-3)

# doing the mission
hook.run_angle(1000,7000)
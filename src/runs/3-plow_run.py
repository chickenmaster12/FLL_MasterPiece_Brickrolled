# Run 3: Plow  --  push the plow attachment forward and come back.
#
# This file works BOTH ways:
#   * Upload it ALONE to test just this mission  -> it runs by itself.
#   * Run  python3 build.py  -> it becomes part of main.py with all the runs.
# Edit ONLY the part inside  def run():  -- that's your mission.

# === SETUP (the builder removes this block when merging) ===
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
hub.system.set_stop_button((Button.LEFT, Button.RIGHT))  # free CENTER for our use
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)
robot = DriveBase(left_motor, right_motor, wheel_diameter=63, axle_track=112)
robot.settings(420, 300, 180, 200)
hook = Motor(Port.A)
plow = Motor(Port.E)
# === END SETUP ===


def run():
    
    plow.run_angle(200, 1000)
    robot.straight(250)
    robot.turn(45)
    robot.turn(-45)
    robot.straight(-250)


# === STANDALONE (the builder removes this block when merging) ===
# This makes the file run by itself when you upload just this file.
if __name__ == "__main__":
    run()
# === END STANDALONE ===

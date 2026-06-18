# Run 1: Stage  --  drive to the stage, spin the spotlight and play the speaker.
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
    # drive forward to the stage
    robot.straight(815)
    robot.curve(10, 45)
    robot.straight(11)

    # Stage spin mission. Speaker spins in the background (wait=False) so the
    # spotlight can spin at the same time.
    #   Port A = spotlight spinner (hook),  Port E = speaker (plow).
    spotlight_spinner = hook
    speaker = plow
    speaker.run_angle(200, 220, wait=False)
    spotlight_spinner.run_angle(600, -520)

    # drive back to home base
    robot.straight(-60)
    robot.curve(10, -60)
    robot.straight(-744)


# === STANDALONE (the builder removes this block when merging) ===
# This makes the file run by itself when you upload just this file.
if __name__ == "__main__":
    run()
# === END STANDALONE ===

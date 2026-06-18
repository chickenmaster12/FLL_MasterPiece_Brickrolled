# RUN MENU  --  button-driven selector. You should not need to edit this file.
#
#   CENTER  -> START the armed run; when it finishes, auto-arm the NEXT run
#   LEFT    -> go back one run (redo the previous one)
#   RIGHT   -> skip forward one run without running it
#
#   EMERGENCY STOP while a run is moving:
#       press LEFT + RIGHT together. We move the hub's built-in stop onto that
#       combo (in robot_config.py) so CENTER is free to START runs. The stop
#       kills the program instantly; run it again to come back to the menu.
#       (To power the hub off, hold CENTER for 3 seconds.)
#
# Light:  GREEN = ready,  RED = running,  blinking ORANGE = a run had an error.

from robot_config import hub, robot, Button, Color
from pybricks.tools import wait

# RUNS is provided by the bundled program (the list of run functions, in order).


def show_run(index):
    hub.display.number(index + 1)


def wait_for_button():
    while not hub.buttons.pressed():
        wait(10)
    pressed = hub.buttons.pressed()
    while hub.buttons.pressed():
        wait(10)
    return pressed


def run_menu(RUNS):
    current = 0
    hub.light.on(Color.GREEN)

    while True:
        show_run(current)
        pressed = wait_for_button()

        if Button.LEFT in pressed:
            current = (current - 1) % len(RUNS)

        elif Button.RIGHT in pressed:
            current = (current + 1) % len(RUNS)

        elif Button.CENTER in pressed:
            hub.light.on(Color.RED)
            try:
                RUNS[current]()
            except Exception:
                robot.stop()
                hub.light.blink(Color.ORANGE, [200, 200])
                wait(1500)
            robot.stop()
            hub.light.on(Color.GREEN)
            current = (current + 1) % len(RUNS)

din()
drive_back()ef drive_forward():
    robot.straight(815)
    robot.curve(10, 45)
    robot.straight(11)


def drive_back(): 
    robot.straight(-60)
    robot.curve(10,-60 )
    robot.straight(-744)


def stage_spin():
    spotlight_spinner = Motor(Port.A)
    speaker = Motor(Port.E)
    speaker.run_angle(200, 220, wait=False)
    spotlight_spinner.run_angle(600, -520)

drive_forward()
stage_spin()


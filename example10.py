from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
i = 9
while i >= 0:
    robotArm.grab()
    for x in range(0, i):
        robotArm.moveRight()
    i -= 1
    robotArm.drop()    
    for x in range(0, i):
        robotArm.moveLeft()
    i -= 1
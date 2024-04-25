from RobotArm import RobotArm
from robotArmChallenges import challenges
robotArm = RobotArm(challenges[7],1)

# robotArm._showSolution()
# robotArm.moveLeft()   

robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for move in range(8):
        robotArm.moveRight()
    robotArm.drop()
    if i < 6:
        for move in range(8):
            robotArm.moveLeft()    

# Na jouw code wachten tot het sluiten van de window:

robotArm.wait()
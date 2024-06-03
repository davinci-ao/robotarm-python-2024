from RobotArm import RobotArm
from robotArmChallenges import challenges_basic, challenges_beginner, challenges_intermediate, challenges_advanced
from time import sleep
r = RobotArm(challenges_advanced[5],1)

r.wait()
# robotArm.showSolution()
# r.moveRight()
# r.grab()
# r.moveLeft()
# r.drop()

r.showSolution()

r.moveRight()

# # Na jouw code wachten tot het sluiten van de window:

r.report()

# robotArm.moveRight()
# for i in range(7):
#     robotArm.grab()
#     for move in range(8):
#         robotArm.moveRight()
#     robotArm.drop()
#     if i < 6:
#         for move in range(8):
#             robotArm.moveLeft()
# robotArm.moveLeft()
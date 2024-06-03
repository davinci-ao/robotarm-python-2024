from RobotArm import RobotArm
from robotArmChallenges import challenge_example

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenge_example,0)

# here comes the code to move one box one position
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
# robotArm.help()
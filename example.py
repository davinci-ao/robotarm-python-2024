from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
# robotArm.operate()

robotArm.grab()
for i in range(15):
  robotArm.moveRight()
robotArm.grab()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
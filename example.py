from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.loadLevel('exercise 4') 
for i in range(5):
  robotArm.grab()
  robotArm.moveRight()
  robotArm.moveRight()
  robotArm.drop()
  robotArm.moveLeft()
  robotArm.moveLeft()

robotArm.moveRight()
robotArm.moveRight()

for i in range(5):
  robotArm.grab()
  robotArm.moveLeft()
  robotArm.drop()
  robotArm.moveRight()



# robotArm.grab()
# for i in range(9):
#   robotArm.moveRight()
# robotArm.drop()
# for i in range(5):
#   robotArm.moveLeft()
# robotArm.grab()
# for i in range(5):
#   robotArm.moveRight()
# robotArm.drop()
# for i in range(2):
#   robotArm.moveLeft()
# robotArm.grab()
# for i in range(2):
#   robotArm.moveRight()
# robotArm.drop()

# robotArm.load(',r*?,,y*?,,d*?', '$=150')

# print(robotArm.serializeYard())
  
# robotArm.operate() #test
# Jouw python instructies zet je vanaf hier:
# robotArm.load('test name', ',6?', '?+rw')

# color in colorset translates to random color of other colorset 

# in solution:
# 
# 
#
# rules apply 
#  
# w>2 all whites shifted right 2 positions
# *>3 all colors shifted right 3 positions
# r<1 all reds shifted left 1 position
# b+4 all and only blues to stack 4
# y-3 no yellows to stack 3
# 2=5 all from stack 2 tot stack 5


# robotArm.help() -> help for yard definions syntax in terminal
# robotArm.solution() -> display yard solution


# Na jouw code wachten tot het sluiten van de window:
# robotArm.operate()
robotArm.wait()
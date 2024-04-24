from robotArmSolutions import *

challenges = {
    1:  {'name': 'collect boxes', 'yard' : 'b,,,,b,,,b' , 'solution': ',,,,,,,,,bbb', 'levels':'1:20,2:20/29' },
    2:  {'name':'move stack to right','yard' : 'wwww', 'solution': ',wwww' , 'levels':'1:9,2:9/16'},
    3:  {'name':'move stack exactly to right','yard' : 'bwgrw', 'solution': ',bwgrw','levels':'1:18,2:20/43'},
    4:  {'name':'move all boxes to right','yard' : 'r,b,w,g,g,b,r,w', 'symbols':'','solution': ',r,b,w,g,g,b,r,w'},
    5:  {'name':'split stack in two colors','yard' : ',rwrwrw', 'symbols':'','solution': 'www,,rrr'},
    6:  {'name':'move all stacks to left','yard' : ',6b,,6b,,6b,,6b,,6b', 'symbols':'','solution': '6b,,6b,,6b,,6b,,6b'},
    7:  {'name':'move stack to end','yard' : ',7r', 'symbols':'','solution2': ',,,,,,,,,7r','levels':'1:14,2:25/119'},
    8:  {'name':'move all stacks','yard' : 'b,gg,www,rrrr', 'symbols':'','solution': ',,,,,b,gg,www,rrrr'},
    9:  {'name':'flip all boxes over','yard' : 'g,b,w,r,b', 'symbols':'','solution': ',,,,,b,r,w,b,g'},
    10: {'name':'whites to the right','yard' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-wwwwrgbyrgby', 'solution': hasSolution,'criteria':'w>1'},
    11: {'name':'reds to the end','yard' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-rrrrwgbywgby', 'solution': hasSolution,'criteria':'r:9'},
    12: {'name':'stack distributed to the right','yard' : '???*?,,,,,,,,,','solution': hasSolution, 'criteria':'0}1', 'levels':'1:25,2:17/63'},
    'soorten':     {'yard' : 'x,x,x,x,x,x,,r,g,b', 'symbols':'x-rrrrbbbbgggg', 'solution': hasSolution,'criteria':'r:7,g:8,b:9'},
    'democratie':  {'name':'democratie','yard' : ',x,x,x,x,x,x,x,x,x', 'symbols':'x-rrrryyyybbbb', 'solution': hasDemocratie, 'levels':'1:35,2:35/110,3:35/93'},
}
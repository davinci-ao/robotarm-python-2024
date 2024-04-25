from robotArmSolutions import *

challenges = {
    2:  {'name': 'collect boxes', 'yard' : 'b,,,,b,,,b' , 'solution': ',,,,,,,,,bbb', 'levels':'2:20,3:20/29' },
    3:  {'name':'move stack to right','yard' : 'wwww', 'solution': ',wwww' , 'levels':'2:9,3:9/16'},
    3:  {'name':'move stack exactly to right','yard' : 'bwgrw', 'solution': ',bwgrw','levels':'2:18,3:20/43'},
    4:  {'name':'move all boxes to right','yard' : 'r,b,w,g,g,b,r,w', 'symbols':'','solution': ',r,b,w,g,g,b,r,w'},
    5:  {'name':'split stack in two colors','yard' : ',rwrwrw', 'symbols':'','solution': 'www,,rrr'},
    6:  {'name':'move all stacks to left','yard' : ',6b,,6b,,6b,,6b,,6b', 'symbols':'','solution': '6b,,6b,,6b,,6b,,6b'},
    7:  {'name':'move stack to end','yard' : ',7r', 'symbols':'','solution': ',,,,,,,,,7r','levels':'2:13,3:13/119'},
    8:  {'name':'move all stacks','yard' : 'b,gg,www,rrrr', 'symbols':'','solution': ',,,,,b,gg,www,rrrr'},
    9:  {'name':'flip all boxes over','yard' : 'g,b,w,r,b', 'symbols':'','solution': ',,,,,b,r,w,b,g'},
    10: {'name':'whites to the right','yard' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-wwwwrgbyrgby', 'solution': hasSolution,'criteria':'w>1'},
    12: {'name':'reds to the end','yard' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-rrrrwgbywgby', 'solution': hasSolution,'criteria':'r:9'},
    13: {'name':'stack distributed to the right','yard' : '???*?,,,,,,,,,','solution': hasSolution, 'criteria':'0}1', 'levels':'2:25,3:17/63'},
    'soorten':     {'yard' : 'x,x,x,x,x,x,,r,g,b', 'symbols':'x-rrrrbbbbgggg', 'solution': hasSolution,'criteria':'r:7,g:8,b:9'},
    'democratie':  {'name':'democratie','yard' : ',x,x,x,x,x,x,x,x,x', 'symbols':'x-rrrryyyybbbb', 'solution': hasDemocratie, 'levels':'2:35,3:35/110,3:35/93'},
}
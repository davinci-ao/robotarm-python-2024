from robotArmSolutions import *

challenges = {
    2:  {'name': 'collect boxes', 'start' : 'b,,,,b,,,b' , 'solution': ',,,,,,,,,bbb', 'levels':'2:20,3:20/29' },
    3:  {'name':'move stack to right','start' : 'wwww', 'solution': ',wwww' , 'levels':'2:9,3:9/16'},
    3:  {'name':'move stack exactly to right','start' : 'bwgrw', 'solution': ',bwgrw','levels':'2:18,3:20/43'},
    4:  {'name':'move all boxes to right','start' : 'r,b,w,g,g,b,r,w', 'solution': ',r,b,w,g,g,b,r,w'},
    5:  {'name':'split stack in two colors','start' : ',rwrwrw', 'solution': 'www,,rrr'},
    6:  {'name':'move all stacks to left','start' : ',6b,,6b,,6b,,6b,,6b', 'solution': '6b,,6b,,6b,,6b,,6b'},
    7:  {'name':'move stack to the end','start' : ',7r', 'solution': ',,,,,,,,,7r','levels':'2:13,3:13/119'}, #
    8:  {'name':'move all stacks','start' : 'b,gg,www,rrrr', 'solution': ',,,,,b,gg,www,rrrr'},
    9:  {'name':'flip all boxes over','start' : 'g,b,w,r,b', 'solution': ',,,,,b,r,w,b,g'},
    10: {'name':'whites to the right','start' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-wwwwrgbyrgby', 'solution': hasSolution,'criteria':'w>1'},
    12: {'name':'reds to the end','start' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-rrrrwgbywgby', 'solution': hasSolution,'criteria':'r:9'},
    13: {'name':'stack distributed to the right','start' : '???*?,,,,,,,,,','solution': hasSolution, 'criteria':'0}1', 'levels':'2:25,3:17/63'},
    'soorten':     {'start' : 'x,x,x,x,x,x,,r,g,b', 'symbols':'x-rrrrbbbbgggg', 'solution': hasSolution,'criteria':'r:7,g:8,b:9'},
    'democratie':  {'name':'democratie','start' : ',x,x,x,x,x,x,x,x,x', 'symbols':'x-rrrryyyybbbb', 'solution': hasDemocratie, 'levels':'2:35,3:35/110,3:35/93'},
}
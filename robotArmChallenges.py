from robotArmSolutions import *

challenge_example = {'start': 'r', 'solution': ',r', 'name': 'move box', 'levels':'2:8,3:7/3', 
         'info':'move box to spot 1'}

challenges_basic =  {
    1 : {'start': ',,l', 'solution': 'l', 'name': 'box to start', 'levels':'2:10,3:10/6', 
         'info':'move box to spot 0'},
    2 : {'start': ',r,b', 'solution': ',b,r', 'name': 'swap boxes', 'levels': '2:18,3:18/14',
         'info':'swap de spots of the boxes'},
    3 : {'start': 'dy', 'solution': 'yd', 'name': 'swap boxes in stack', 'levels': '2:22,3:22/18', 
         'info':'swap de the boxes within the stack'},
    4 : {'start' : 'b,,,,b,,,b' , 'solution': ',,,,,,,,,bbb', 'name': 'collect boxes', 'levels':'2:20,3:20/29', 
         'info':'move all boxes to the last spot'},
    5 : {'start': ',x', 'solution': hasSolution, 'criteria':'r:0,y:2', 'name': 'sort 1 box', 'symbols':'x-ry', 'levels': '2:12,3:11/5','example':exampleSolution, 
         'info':'red to spot 0, yellow to spot 2'},
}

challenges_beginner = {
    1 : {'start' : '4w', 'solution': ',4w', 'name': 'move stack to right', 'levels': '2:10,3:9/15', 'info':'move stack one spot to the right'},
    2 : {'start': ',6x', 'solution': hasSolution, 'criteria':'b:0,g:2', 'name': 'sort 6 boxes', 'symbols':'x-bbbbbggggg', 'levels':'2:16,3:18/30', 
         'info':'blue boxes to spot 0, green boxes to spot 2'},
    3 : {'start' : '5y', 'solution': ',,,,5y', 'name': 'move stack to spot 4', 'levels': '2:11,3:12/46', 'info':'move the whole stack to spot 4'},
    4 : {'name':'split stack in two colors','start' : ',rwrwrw', 'solution': 'www,,rrr','levels':'2:14,3:15/24','info':'move white boxes to spot 0 en red boxes to spot 2'},
    5 : {'name':'stack to end','start' : ',7r', 'solution': ',,,,,,,,,7r','levels':'2:13,3:13/119',
         'info': 'move all boxes of the stack to the last spot'}, 
}

challenges_intermediate = {
    1 : {'name':'move all boxes to right','start' : 'r,b,w,g,g,b,r,w,y', 'solution': ',r,b,w,g,g,b,r,w,y','levels':'2:13,3:13/51','info':'move all boxes one spot to the right'},
    2 : {'name':'move all stacks to left','start' : ',6b,,6b,,6b,,6b,,6b', 'solution': '6b,,6b,,6b,,6b,,6b','levels':'2:13,3:14/128','info':'move all stacks one spot to the left'},
    3 : {'name':'whites to the right','start' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-wwwwwwrgbrgbrgb', 'solution': hasSolution,'criteria':'w>1','example':exampleSolution,'scans':'5:9','levels':'2:17,3:17/55','info':'move all white boxes one spot to the right'},
    4 : {'name':'move stack exactly to right','start' : 'bwgrw', 'solution': ',bwgrw','levels':'2:18,3:20/43',
         'info':'move the stack one space to the right, with all the boxes in the same order'},
    5 : {'name':'flip all boxes over','start' : 'g,b,w,r,b', 'solution': ',,,,,b,r,w,b,g','levels':'2:17,3:11/55','info':'Use robotArm.showSolution() to display desired solution'},
}

challenges_advanced = {
    1 : {'name':'move all stacks','start' : 'b,2g,3w,4r', 'solution': ',,,,,b,2g,3w,4r','levels':'2:15,3:15/112'},
    2 : {'name':'reds to the end','start' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-rrrrwgbywgby', 'solution': hasSolution,'criteria':'r:9','example':exampleSolution},
    3 : {'name':'stack distributed to the right','start' : '???*?,,,,,,,,,','solution': hasSolution, 'criteria':'0}1','example':exampleSolution ,'levels':'2:25,3:17/63'},
    4 : {'name':'sort in stacks: rgb','start' : 'x,x,x,x,x,x,,r,g,b', 'symbols':'x-rrrrbbbbgggg', 'solution': hasSolution,'criteria':'r:7,g:8,b:9','example':exampleSolution},
    5 : {'name':'democratie','start' : ',x,x,x,x,x,x,x,x,x', 'symbols':'x-rrrrryyyyybbbbb', 'solution': hasDemocratie, 'example':getDemocratieSolution,'levels':'2:35,3:35/110','info':'collect all boxes of most common color on spot 0. If equally counted collect boxes of the first color found'},
}

challenges_special = {
'''
halloween
sinterklaas
winter
kerstmis
carnaval
pasen
lente
politiek (vlag omkeren)
'''

}

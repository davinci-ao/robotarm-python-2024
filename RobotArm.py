import pygame # install in terminal with: pip install pygame
from SpriteSheet import SpriteSheet
import os
import sys
import random
import string
import inspect
from math import ceil, floor

# RobotArm class ################################################
#
#   An object of this class...
#
#   lets you load and display a yard with stacks of colored boxes
#   you can load a predefined level at the creation
#   lets you program the movement of boxes and scan their colors
#   lets you inspect the yard for debugging purposes
#
#   supported colors are: white, green, red, blue and yellow
#
# ######## methods for public use:
#   moveRight()
#     moves the robotarm one stack position to the right
#     returns True if succeeded, returns False if not possible
#
#   moveLeft()
#     moves the robotarm one stack position to the left
#     returns True if succeeded, returns False if not possible
#
#   grab()
#     lets the robotarm grab a box from the stack if there is one
#     returns True if succeeded, returns False if not possible
#
#   drop()
#     lets the robotarm drop its box to the stack if not full
#     returns True if succeeded, returns False if not possible
#
#   scan()
#      returns the color of the box at the robotarm
#
#   wait(operator)
#       waits for the the program window to be closed
#       operator is an optional function with a parameter: events {list of events}
#       the operator must/can handle each event in events
#
#   operate()
#       make the robotarm operate on keyboard-keys: LEFT, RIGHT and DOWN
#
# ######## creating and loading levels ########
#
#   loadLevel(levelName)
#     loads a predefined level for levelName {string}
#     returns True if succeeded, returns False if failed
#
#   loadMyLevel(yard, levelName)
#     loads a self made yard with a self made levelName {string}
#     where yard is a list of stacks each stack is a list of colors
#       box colors example of a yard: [['r','g'],['r','b'],[],['g']]
#     returns True if succeeded, returns False if errors found, but sanitized
#
# ###########################################################

class RobotArm:
  version = '2.4'
# 2.1: incluses warnings for actions like hitting the borders
# 2.2: includes flaw terminal warnings for pointless actions
# 2.3: may grab once without warning from empty stack that was randomly sized
# 2.3.1: added handling key UP en DOWN for speeding up and down, while running animations
# 2.4: 

  _colors = [
    {"name": 'w', 'code': (255,255,255), 'c': 'w'},
    {"name": 'r', 'code': (255,0,0), 'c': 'r'},
    {"name": 'g', 'code': (0,150,0), 'c': 'g'},
    {"name": 'b', 'code': (0,0,255), 'c': 'b'},
    {"name": 'y', 'code': (255,255,0), 'c': 'y'},
    {"name": 'p', 'code': (128,0,128), 'c': 'p'},
    {"name": 'o', 'code': (255,128,0), 'c': 'o'},
    {"name": 'd', 'code': (10,10,10), 'c': 'd'},
  ]
  _colorSet = [color['name'] for color in _colors]
  _defaultlevels = [
    {'name': 'exercise 1',  'yard' : ',r', 'symbols' : '#=8+2,$=4','solution': 'r' },
    {'name': 'exercise 2',  'yard' : 'b,,,,b,,,b' , 'symbols' : '#=20,$=29', 'solution': ',,,,,,,,,bbb'  },
    {'name': 'exercise 3',  'yard' : 'wwww', 'symbols':'#=9,$=16','solution': ',wwww'},
    {'name': 'exercise 4',  'yard' : 'bwgrw', 'symbols':'#=50,$=100','solution': ',bwgrw'},
    {'name': 'exercise 6',  'yard' : ',rwrwrw', 'symbols':'','solution': 'www,,rrr'},
    {'name': 'exercise 5',  'yard' : 'r,b,w,g,g,b,r,w', 'symbols':'','solution': ',r,b,w,g,g,b,r,w'},
    {'name': 'exercise 7',  'yard' : ',6b,,6b,,6b,,6b,,6b', 'symbols':'','solution': '6b,,6b,,6b,,6b,,6b'},
    {'name': 'exercise 8',  'yard' : ',7r', 'symbols':'','solution': ',,,,,,,,,7r'},
    {'name': 'exercise 9',  'yard' : 'b,gg,www,rrrr', 'symbols':'','solution': ',,,,,b,gg,www,rrrr'},
    {'name': 'exercise 10', 'yard' : 'g,b,w,r,b', 'symbols':'','solution': ',,,,,b,r,w,b,g'},

    {'name': 'exercise 11', 'yard' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-wwwwrgbyrgby'},
    {'name': 'exercise 12', 'yard' : 'x,x,x,x,x,x,x,x,x,', 'symbols': 'x-rrrrwgbywgby'},
    {'name': 'exercise 13', 'yard' : 'g,g,g,b,w,g,r,r,b,g'},
    {'name': 'exercise 14', 'yard' : ',g,w,gw,rw,ww,b,bbb,bgg,r'},
    {'name': 'exercise 15', 'yard' : ',b,,b,w,,r,g,g,g'},
    {'name': 'soorten',     'yard' : 'x,x,x,x,x,x,,r,g,b', 'symbols':'x-rrrrbbbbgggg'},
    {'name': 'democratie',  'yard' : ',x,x,x,x,x,x,x,x,x', 'symbols':'x-rrrryyyybbbb'},
    ]
  _speeds = [{'fps': 100,'step': 1},{'fps': 150,'step': 2},{'fps': 250,'step': 4},{'fps': 400,'step': 5},{'fps': 500,'step': 10},{'fps': 500,'step': 20}]
  EMPTY = ''
  _backgroundColor = (200,200,200)
  _penColor = (0,0,0)
  _maxStacks = 10
  _maxLayers = 7
  _boxHeight = 29
  _boxWidth = 29
  _penWidth = 1
  _boxMargin = 2
  _armTopHeight = 15
  _bottomMargin = 2
  _idleAnimationTime = 300
  _screenMargin = 3
  _eventSleepTime = 300
  _eventActiveCycles = 100
  _steps = 0 # amount of actions done
  _iconImage = 'robotarm.ico'
  _hazardSprite = 'caution-icon-hi.png'
  _hazardFont = 'FreeSansBold.ttf'
  _previousAction = ''
  _accuWidth = 15
  _accuCapacity = False
  _accuPadding = 5
  _accuColors = ((100,'g'),(50, 'y'),(25, 'o'),(10, 'r'))
  _actionFlaws = [
    ['left','right'],
    ['right','left'],
    ['drop','grab'],
    ['grab','drop'],
    ['scan','scan'],
    ['drop','scan'],
  ]
  reportFlaws = False
  _knownEmpty = []

  def count_lines_of_code(self):
    current_frame = inspect.currentframe()
    while current_frame.f_back:
        current_frame = current_frame.f_back
    caller_filename = inspect.getframeinfo(current_frame).filename
    with open(caller_filename, 'r') as f:
      lines = f.readlines()
    num_lines = 0
    for line in lines:
      line = line.strip()
      if line and not line.startswith("#") and not line.startswith("print(") and not line.startswith("input("):
        num_lines += 1
    print(f'codelines:{num_lines}')
    return num_lines

  def _setScreen(self):
    self._screenWidth = self._stackX(self._maxStacks) + self._screenMargin 
    self._screenHeight = self._layerY(-1) + self._bottomMargin + 2 * self._screenMargin
    self._screen = pygame.display.set_mode((self._screenWidth + self._accuWidth, self._screenHeight))

  def __init__(self, levelName = ''):
    self._color = self.EMPTY
    self._stack = 0
    self._yardBottom = self._armTopHeight + (self._maxLayers + 1) * self._boxSpaceHeight() + self._penWidth
    self._armHeight = self._armTopHeight
    self._armX = 0
    self.speed = 1
    self._yard = []

    pygame.init()
    self._clock = pygame.time.Clock()

    self._setScreen()

    assetsDir = os.path.dirname(os.path.realpath(__file__)) + '/'    # force assets to be found in directory of robotarm.py
    try:
      programIcon = pygame.image.load(assetsDir + self._iconImage)
      pygame.display.set_icon(programIcon)
      self._testImage = programIcon
    except:
      print(f' ********* icon image: {self._iconImage} not found *********')

    try:
      ss = SpriteSheet(assetsDir + self._hazardSprite)
      self._hazardSign = ss.load_strip((0,0,64,64), 4, self._backgroundColor)
    except:
      print(f' ********* hazard sprite: {self._hazardSprite} not found *********')
      exit()

    try:
      self._font = pygame.font.Font(assetsDir + self._hazardFont, 24)
    except:
      print(f' ********* font: {self._hazardFont} not found *********')
      exit()

    # Load level at creation
    if levelName != '':
      self.loadLevel(levelName)

########### ANIMATION METHODS ###########

  def _getColorCode(self, name):
    for c in self._colors:
      if c['name'] == name:
        return c['code']
    return False
  
  def _getColorByName(self, name):
    for c in self._colors:
      if c['name'] == name:
        return c
    return self.colors[-1]

  def _checkSpeed(self):
    speedInvalid = False
    if type(self.speed) is not int:
      speedInvalid = True
    if not (self.speed in range(len(self._speeds))):
      speedInvalid = True
    if speedInvalid:
      self.speed = 0 # reset speed to zero
      print('speed must be an integer between 0 and ' + str(len(self._speeds)-1))

  def _drawBoxAtPosition(self, x, y, color):
    pygame.draw.rect(self._screen, color, (x, y, self._boxWidth, self._boxHeight))
    pygame.draw.rect(self._screen, self._penColor, (x, y, self._boxWidth, self._boxHeight), self._penWidth)

  def _boxSpaceWidth(self):
    return (self._boxWidth + 2 * self._boxMargin) + self._penWidth

  def _stackX(self, stack):
    return self._screenMargin + self._boxMargin + stack * self._boxSpaceWidth() + self._penWidth

  def _boxSpaceHeight(self):
    return (self._boxHeight - self._penWidth)

  def _layerY(self,layer):
    return self._yardBottom - (layer + 1) * self._boxSpaceHeight() - self._screenMargin

  def _drawBox(self, stack, layer):
    x = self._stackX(stack) 
    y = self._layerY(layer)
    color = self._getColorCode(self._yard[stack][layer])
    self._drawBoxAtPosition(x,y,color)

  def _drawStack(self, stack):
    for l in range(len(self._yard[stack])):
      self._drawBox(stack,l)
    x = self._stackX(stack) - self._boxMargin - self._penWidth
    y = self._layerY(-1) + self._bottomMargin

    pygame.draw.lines(self._screen, self._penColor, False, [(x, y - 5), (x, y), (x + self._boxSpaceWidth(), y), (x + self._boxSpaceWidth(), y - 5)])

  def _drawArm(self):
    xm = self._armX + int(self._boxSpaceWidth()/2) - self._boxMargin
    pygame.draw.line(self._screen, self._penColor, (xm, 2), (xm, self._armHeight - 2))
    pygame.draw.lines(self._screen, self._penColor, False, [
      (self._armX - self._boxMargin,                  self._armHeight + 2), 
      (self._armX - self._boxMargin,                  self._armHeight - 2),
      (self._armX + self._boxWidth + self._penWidth,  self._armHeight - 2),
      (self._armX + self._boxWidth + self._penWidth , self._armHeight + 2)])
    if self._color > '':
      self._drawBoxAtPosition(self._armX,self._armHeight,self._getColorCode(self._color))

  def _drawAccu(self):
    if self._accuCapacity ==  False: return
    # pygame.draw.rect(self._screen, (0,150,0), (self._screenWidth, 0, self._accuWidth, self._screenHeight))
    _stepsDone  = self._steps if self._steps < self._accuCapacity else self._accuCapacity
    _accuOver = (self._accuCapacity - _stepsDone) / self._accuCapacity
    _accuDone = _stepsDone / self._accuCapacity
    _accuPerc = ceil(_accuOver * 100)

    pygame.draw.rect(self._screen, (0,0,0), (self._screenWidth, 0, self._accuWidth, self._screenHeight))
    _x0 = self._screenWidth + self._accuPadding
    _y0 = 0 + self._accuPadding
    _w0 = self._accuWidth - 2 * self._accuPadding
    _h0 = self._screenHeight  - 2 * self._accuPadding

    _x = _x0
    _y = self._accuPadding+ ceil(_h0 * _accuDone)
    _h = floor(_h0 * _accuOver)
    color = 'g'
    for percColor in self._accuColors:
      if _accuPerc < percColor[0]:
        color = percColor[1]
  
    pygame.draw.rect(self._screen, self._getColorCode(color), (_x0, _y, _w0, _h))
    pass

  def _drawState(self):
    steps = ' ['+ str(self._steps)+']' if self._steps > 0 else ''
    pygame.display.set_caption('Robotarm: ' + self._levelName + steps)
    self._screen.fill(self._backgroundColor)
    for c in range(len(self._yard)):
      self._drawStack(c)
    self._drawArm()
    self._drawAccu()

  def _message(self, message = 'problem!', gravity = 1):
    xm = self._armX + int(self._boxSpaceWidth()/2) - self._boxMargin - 31
    ym = 0

    text = self._font.render(message, True, (200,50,50), self._backgroundColor)
    for l in range(12):
      self._drawState()
      if gravity == 1: self._screen.blit(self._hazardSign[l % 4],(xm,ym))
      if l%2 == 0 or l >= 6:
        self._screen.blit(text, ((self._screenWidth//2) - text.get_rect().width//2,60))
      pygame.display.update()
      pygame.time.delay(100)

    self._drawState()
    pygame.display.update()

  def _animateHazard(self, message = 'problem!'):
    self._message(message, 1)

  def _animateFlaw(self, message = 'inefficiency!'):
    self._message(message, 0)

  def _animate(self, *args):
    self._checkSpeed()
    self._armX = self._stackX(self._stack)

    if (args[0] == 'down'):
      self._armHeight = self._armTopHeight
      targetLayer = len(self._yard[self._stack])
      if self._color == '':
        targetLayer -= 1
      targetHeight = self._layerY(targetLayer)
    elif (args[0] == 'left'):
      targetX = self._stackX(self._stack - 1)
    elif (args[0] == 'right'):
      targetX = self._stackX(self._stack + 1)

    ready = False
    while not ready:
      if (args[0] == 'idle'):
        ready = True
      elif (args[0] == 'down'):
        ready = self._armHeight == targetHeight
      elif (args[0] == 'up'):
        ready = self._armHeight == self._armTopHeight
      elif (args[0] == 'left') or (args[0] == 'right'):
        ready = self._armX == targetX

      for event in pygame.event.get():
        self.checkCloseEvent(event)
        self.handleSpeedEvent(event)

      self._drawState()
      pygame.display.update()

      self._clock.tick(self._speeds[self.speed]['fps'])

      if (args[0] == 'down'):
        self._armHeight += self._speeds[self.speed]['step']
        if self._armHeight > targetHeight:
          self._armHeight = targetHeight
      elif (args[0] == 'up'):
        self._armHeight -= self._speeds[self.speed]['step']
        if self._armHeight < self._armTopHeight:
          self._armHeight = self._armTopHeight
      elif (args[0] == 'left'):
        self._armX -= self._speeds[self.speed]['step']
        if self._armX < targetX:
          self._armX = targetX
      elif (args[0] == 'right'):
        self._armX += self._speeds[self.speed]['step']
        if self._armX > targetX:
          self._armX = targetX
      elif (args[0] == 'idle'):
        pygame.time.delay(self._idleAnimationTime)

  def _hasStepsLeft(self):
    return self._accuCapacity == False or (self._accuCapacity - self._steps) > 0

  def _canStep(self)->bool:
    if self._hasStepsLeft():
      self._steps += 1
      return True    

    if self._accuEmpty == False:
        print('accu empty, steps to do:')
        self._accuEmpty = True
    sys.stdout.write('.')
    sys.stdout.flush()
    return False


  def _efficiencyCheck(self, action):
    for flaw in self._actionFlaws:
      if (self._previousAction == flaw[0] and action == flaw[1]):
        flawText = f'{flaw[1]} after {flaw[0]}? why?'
        print(f'action flaw: {flawText}' )
        if self.reportFlaws: self._animateFlaw(flawText)
    self._previousAction = action

  ########### ROBOTARM MANIPULATION ###########
  def moveRight(self):
    if not self._canStep(): return
    self._efficiencyCheck('right')
    success = False
    if self._stack < self._maxStacks - 1:
      self._animate('right')
      self._stack += 1
      success = True
    else:
      self._animateHazard('hit right border!')
    return success

  def moveLeft(self):
    if not self._canStep(): return
    self._efficiencyCheck('left')
    success = False
    if self._stack > 0:
      self._animate('left')
      self._stack -= 1
      success = True
    else:
      self._animateHazard('hit left border!')
    return success

  def grab(self):
    if not self._canStep(): return
    self._efficiencyCheck('grab')
    success = False
    if self._color == self.EMPTY:
      self._animate('down')
      if len(self._yard[self._stack]) > 0:
        self._color = self._yard[self._stack][-1]
        self._yard[self._stack].pop(-1)
        success = True
      else:
        if self._knownEmpty[self._stack]:
          self._animateHazard('nothing to grab!')
        else:
          self._knownEmpty[self._stack] = True
      self._animate('up')
    else:
      self._animateHazard('robot arm occupied!')
    return success

  def drop(self):
    if not self._canStep(): return
    self._efficiencyCheck('drop')
    success = False
    if self._color != self.EMPTY:
      if len(self._yard[self._stack]) < self._maxLayers:
        self._animate('down')
        self._yard[self._stack].append(self._color)
        self._color = self.EMPTY
        self._animate('up')
        success = True
      else:
        self._animateHazard('stack full!')
    else:
      self._animateHazard('no box to drop!')
    self._watchSolution()
    return success

  def scan(self):
    if not self._canStep(): return
    self._efficiencyCheck('scan')
    return self._color

########### LEVEL & YARD lOADING & CREATION ###########

  def _checkSolution(self):
    serializedYard = self.serializeYard()
    if self._solution:
      if self._solution == serializedYard:
        return True
      else:
        return False
    
    # check if all rules do apply, if so solution is reached
    
    # stdColorSet = ''.join(self._colorSet)
    # _rules = self._rules.split(',')
    # ok = True
    # for rule in _rules:
    #   rule = rule.strip()
    #   if rule[0] in stdColorSet:
    #     if rule[1] == '>' and rule[2] in string.digits:
    #       tryYard = self.yardInitial + []
    #       dist = int(rule[2])
    #       color = rule[0]
    #       for stackIndex in range(self._maxStacks-1,-1,-1):
    #         newStackIndex = stackIndex + dist 
    #         if newStackIndex < self._maxStacks: 
    #           stack = tryYard[stackIndex]
    #           for boxIndex in range(len(stack)-1,-1,-1):
    #             if stack[boxIndex] == color:
    #               stack.pop(boxIndex)
    #               tryYard[newStackIndex].append(color)
    #       for stack in tryYard:
    #         if stack

    # return ok
  
  def _watchSolution(self):
    if self._checkSolution():
      print(f'Solution reached in {self._steps} steps')
      
  def _checkCodeMax(self,codeMax):
    if codeMax != False:
      lines = self.count_lines_of_code()
      exceeded = lines - codeMax
      if exceeded > 0:
        print(f'*****************************************************')
        print(f'* Progam contains: {  lines:3} lines of code                *')           
        print(f'* Maximum allowed lines of:{codeMax:3} has been exceeded!   *')
        print(f'*****************************************************')

  def loadMyLevel(self, yard, levelName = 'unknown', accu = False, codeMax = False, solution = '' ,rules = ''):
    self._checkCodeMax(codeMax)
    if solution:
      solution += (self._maxStacks - solution.count(',')) * ','
    self._solution = solution
    self._rules = rules
    self._steps = 0
    self._yard = yard # sanitized yard
    self._yardInitial = yard + []
    while len(self._yard) < self._maxStacks:
      self._yard.append([])
    self._levelName = levelName
    self._accuCapacity = accu
    self._accuEmpty = False
    self._animate('idle')

    return True

  def constructYard(self, yard = 'r', symbols = '' ):
    colorSymbols = string.ascii_lowercase + '?'
    amountSymbols = string.ascii_uppercase + '*'
    stdColorSet = ''.join(self._colorSet)
     # determine symbols in the yard
    symbols = symbols.split(',')
    _accu = False
    _codeMax = False
    _symbols = {}
    _symbols['?'] = {'colors' : list('rgbw'), 'proces': '?'} # default random color symbol
    _symbols['*'] = {'value' : 4, 'proces': '?'} # default random amount symbol
    for symbol in symbols:
      if len(symbol) < 3: continue

      if symbol[0] in amountSymbols and symbol[2] in string.digits:
        _symbols[symbol[0]] = {'value' : int(symbol[2]), 'proces': symbol[1]}

      if symbol[0] in colorSymbols:
        # get valid colorset
        colorset = ''
        for c in symbol[2:]:
          if c in stdColorSet:
            colorset += c
        if colorset == '': colorset = stdColorSet
        _symbols[symbol[0]] = {'value': False, 'colors' : list(colorset), 'proces': symbol[1], 'reset': list(colorset)}
      if symbol[0] == '$':
        try:
          _accu = int(symbol[2:])
        except: pass
      if symbol[0] == '#':
        try:
          _codeMax = int(symbol[2:])
        except: pass      
    stacks = yard.split(',')

    _yard = []
    for stack in stacks:
      _stack = []
      amountBoxes = 1
      color = False
      for char in _symbols:
        if _symbols[char]['proces'] == '|':
          _symbols[char]['colors'] = _symbols[char]['reset'] + [] # every stack a new color set
      for char in stack:
        if char in colorSymbols:
          for _ in range(amountBoxes):
            if char in _symbols:
              if _symbols[char]['proces'] == '?':
                color = random.choice(_symbols[char]['colors'])
              elif _symbols[char]['proces'] in ['-','|']:
                color = random.choice(_symbols[char]['colors'])
                _symbols[char]['colors'].remove(color)
                if len(_symbols[char]['colors']) == 0:
                  _symbols[char]['colors'].append('d')
              elif _symbols[char]['proces'] == '>':
                color = _symbols[char]['colors'][_symbols[char]['value']]
                _symbols[char]['value'] = (_symbols[char]['value']+1) % len(_symbols[char]['colors'])
              elif _symbols[char]['proces'] == '<':
                color = _symbols[char]['colors'][_symbols[char]['value']]
                _symbols[char]['value'] = (_symbols[char]['value']-1+len(_symbols[char]['colors'])) % len(_symbols[char]['colors'])
              elif _symbols[char]['proces'] == '=':
                if _symbols[char]['value'] == False:
                  _symbols[char]['value'] = random.randint(0,len(_symbols[char]['colors'])-1)
                color = _symbols[char]['colors'][_symbols[char]['value']]
            elif char in stdColorSet:
              color = char
            if color not in stdColorSet:
              color = self.colorSet[-1] # pick deault last of colors
            if len(_stack) < self._maxLayers:
              _stack.append(color)
          amountBoxes = 1
        elif char in string.digits:
          amountBoxes = int(char)
        elif char in amountSymbols and char in _symbols:
          if _symbols[char]['proces'] == '?':
            amountBoxes = random.randint(0,_symbols[char]['value'])
          else:
            amountBoxes = _symbols[char]['value']
            if _symbols[char]['proces'] == '+':
              _symbols[char]['value'] += 1
            if _symbols[char]['proces'] == '-':
              _symbols[char]['value'] -= 1
              if _symbols[char]['value'] < 0: 
                _symbols[char]['value'] = 0
      _yard.append(_stack)

    while len(_yard) < self._maxStacks:
      _yard.append([])
    return _yard, _accu, _codeMax
  
  def load (self, yard: str = 'r', symbols: str = '', solution: str = '', rules: str = ''):
    _yard, _accu, _codeMax = self.constructYard(yard, symbols)
    
    success = self.loadMyLevel(_yard,'self made', _accu, _codeMax, solution, rules)
    self._knownEmpty = [True for stack in range(self._maxStacks)]
    return success

  def loadLevel(self, levelName):
    success = False
    for level in self._defaultlevels:
      if levelName == level['name']:
        if type(level['yard']) is str:
          _yard, _accu, _codeMax = self.constructYard(level['yard'], level.get('symbols',''))
          _solution = level.get('solution','')
          _rules = level.get('rules','')
          self.loadMyLevel(_yard, levelName, _accu, _codeMax, _solution, _rules)
          self._knownEmpty = [True for stack in range(self._maxStacks)]
          success = True
    if not success:
      self.loadMyLevel([])
    return success

  # def _requiredColorsFound(self, yard, requiredColors):
  #   colors = []
  #   for stack in yard:
  #     for color in stack:
  #       colors.append(color)
  #   for color in requiredColors:
  #     if colors.count(color) == 0:
  #       return False
  #   return True

  # def _createRandomYard(self, maxStacks, minBoxes, maxBoxes, colors, maxColors, requiredColors, startStacks, endStacks):
  #   yard = [] + startStacks
  #   while len(yard) == 0 or not self._requiredColorsFound(yard, requiredColors):
  #     yard = [] + startStacks
  #     for l in range(maxStacks):
  #       random.seed()
  #       stack = []
  #       height = random.randint(minBoxes, maxBoxes)
  #       for b in range(height):
  #         color = colors[random.randint(0,len(colors)-1)]
  #         stack.append(color)
  #       yard.append(stack)
  #   for stack in endStacks:
  #     if len(yard) < 10:
  #       yard.append(stack)
  #   return yard

  # def _randomColors(self, requiredColors, maxColors):
  #   colors = []
  #   for color in requiredColors:
  #     if not color in colors:
  #       colors.append(color)
  #   while len(colors) < maxColors:
  #     color = self._colors[random.randint(0,len(self._colors)-1)]['name']
  #     if not color in colors:
  #       colors.append(color)
  #   return colors

  # def loadRandomLevel(self, requirements = {}):
  #   maxStacks = requirements['maxStacks'] if 'maxStacks' in requirements else 6
  #   maxStacks = self._maxStacks if maxStacks > self._maxStacks else maxStacks
  #   minBoxes = requirements['minBoxes'] if 'minBoxes' in requirements else 1
  #   maxBoxes = requirements['maxBoxes'] if 'maxBoxes' in requirements else 3
  #   maxBoxes = self._maxLayers if maxBoxes > self._maxLayers else maxBoxes
  #   requiredColors = requirements['requiredColors'] if 'requiredColors' in requirements else []
  #   levelName = requirements['levelName'] if 'levelName' in requirements else 'random level'
  #   maxColors = requirements['maxColors'] if 'maxColors' in requirements else 4
  #   startStacks = requirements['startStacks'] if 'startStacks' in requirements else []
  #   endStacks = requirements['endStacks'] if 'endStacks' in requirements else []

  #   colors = self._randomColors(requiredColors, maxColors)
  #   myYard = self._createRandomYard(maxStacks, minBoxes, maxBoxes, colors, maxColors, requiredColors, startStacks, endStacks)
  #   self.loadMyLevel(myYard, levelName)
  #   self._knownEmpty = [True for stack in range(self._maxStacks)]
  #   if minBoxes != maxBoxes:
  #     for stack in range(len(startStacks), len(startStacks) + maxStacks):
  #       self._knownEmpty[stack] = False

  # def randomLevel(self, stacks, layers):
  #   self.loadRandomLevel({'maxStacks': stacks, 'maxBoxes': layers})

  def serializeYard(self):
    _yard = ''
    for stack in self._yard:
      _yard += ''.join(stack)+','
    return _yard

########### EVENT HANDLING ###########

  def checkCloseEvent(self,event):
    if event.type == pygame.QUIT:
      sys.exit()

  def handleSpeedEvent(self,event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          if self.speed < 5:
            self.speed += 1
        elif event.key == pygame.K_DOWN:
          if self.speed > 0:
            self.speed -= 1

  def _defaultHandler(self, events):
    for event in events:
      self.checkCloseEvent(event)

  def wait(self, handler = False):
    cycle = 0
    while True:
      events = pygame.event.get()               # get latest events
      if callable(handler):
        handler(events)
      self._defaultHandler(events)
      if len(events) > 0:                       # events happened?
        cycle = 0                               # stay awake and alert

      cycle += 1                                # prepare for sleep

      if cycle > self._eventActiveCycles:       # after 30 cycles
        pygame.time.delay(self._eventSleepTime) # go asleep for 300 milliseconds, give the processor some rest
        cycle = 0                               # wake up for events during sleep

  def _operator(self, instructions):
    for instruction in instructions:
      if instruction.type == pygame.KEYDOWN:
          if instruction.key == pygame.K_LEFT:
            self.moveLeft()
          if instruction.key == pygame.K_RIGHT:
            self.moveRight()
          if instruction.key == pygame.K_DOWN:
            if self._color == '':
              self.grab()
            else:
              self.drop()

  def operate(self):
    self.wait(self._operator)

  def help(self):
    print('help')

  

if __name__ == "__main__":
  print('tested module RobotArm')

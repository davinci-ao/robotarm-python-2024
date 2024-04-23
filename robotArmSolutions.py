def hasDemocratie(yardStart, yardNow, criteria=''):
  char_count = {}
  _yard = yardStart.split(',')
  for index in range(len(_yard)):
     _yard[index] = list(_yard[index])

  # Count occurrences of each character
  for _stack in _yard:
    for char in _stack:
        char_count[char] = char_count.get(char,0) + 1
 
  # Find the character with the maximum count
  max_count = 0
  winner = None
  for char, count in char_count.items():
      if count > max_count:
          max_count = count
          winner = char

  for indexStack in range(1,len(_yard)):
    _stack = _yard[indexStack]
    if len(_stack) > 0 and _stack[0] == winner:
        _stack.pop(0)
        _yard[0].append(winner)

  solution = ''
  for stack in _yard:
    solution += ''.join(stack)+','
  return yardNow == solution[:-1]

def hasColorNotAt(yardStart, yardNow, spec):
  color = spec[0]
  try:
    indexNow = int(spec[2:])
  except: 
     return False

  _yardNow = yardNow.split(',')   
  if 0 <= indexNow < len(_yardNow) and _yardNow[indexNow].count(color) == 0:
    return True

  return False

def hasColorCollectedAt(yardStart, yardNow, spec):
  color = spec[0]
  try:
    indexNow = int(spec[2:])
  except: 
     return False

  totalCounted = yardStart.count(color)
  _yardNow = yardNow.split(',')   
  if 0 <= indexNow < len(_yardNow) and _yardNow[indexNow].count(color) == totalCounted:
    return True
     
  return False

def hasColorMoved(yardStart, yardNow, spec):
  color = spec[0]
  try:
    shift = int(spec[2])
  except: 
     return False
  if spec[1] == '<':
     shift = -1 * shift

  _yardStart = yardStart.split(',')
  _yardNow = yardNow.split(',')
  _length = len(_yardStart)
  for index in range(_length):
     _countStart = _yardStart[index].count(color)
     newIndex = index + shift
     if 0 <= newIndex < _length:
        _countNow = _yardNow[newIndex].count(color)
        if _countStart != _countNow:
           return False
  return True

def hasDistributedFromAt(yardStart, yardNow, spec):
  try:
    source = int(spec[0])
    dest = int(spec[2])
  except:
     return False
  if spec[1] == '}':
    delta = 1
  elif spec[1] == '{':
    delta = -1

  _yardStart = yardStart.split(',')
  _yardNow = yardNow.split(',')

  for index in range(len(_yardStart[source])-1,-1,-1):
    color = _yardStart[source][index]
    if 0 <= dest < len(_yardNow):
      if len(_yardNow[dest]) == 0 or color != _yardNow[dest][-1]:
        return False
    dest += delta

  return True

def hasSolution(yardStart, yardNow, criteria):
  if type(criteria) != str: return False

  _specs = criteria.split(',')
  checked = False
  for _spec in _specs:
    if _spec[1] == ':': 
      if not hasColorCollectedAt(yardStart, yardNow,_spec): 
        return False
      checked = True
    elif _spec[1] in ['}','{']: 
      if not hasDistributedFromAt(yardStart, yardNow,_spec): 
        return False
      checked = True
    elif _spec[1] in ['>','<']: 
      if not hasColorMoved(yardStart, yardNow,_spec): 
        return False
      checked = True
    elif _spec[1] == '-': 
      if not hasColorNotAt(yardStart, yardNow,_spec): 
        return False
      checked = True

  return checked

# result = hasSolution('','','0}1')
# print(result)

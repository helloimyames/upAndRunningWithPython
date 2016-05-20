f = 0
print f

def someFunction():
  global f
  f = "def"
  print f

someFunction()
print f

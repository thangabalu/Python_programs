COMMON_VARIABLE = "triangle"

def square(name):
  print "this is square"
  return "Hello "+ name+ "\n"

def triangle(name):
  print "this is triangle"
  return "Hello " + name + "\n"

def common_function(func):
    print "Do the common stuffs here"
    return func("four sides")

if __name__ == "__main__":
  if COMMON_VARIABLE == "square":
    print common_function(square)
  else:  
    print common_function(triangle)

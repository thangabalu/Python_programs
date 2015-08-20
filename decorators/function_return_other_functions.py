def compose_greet_function(name,age):
  def get_message():
    print "one"
    return "Hello there {}, Age is {}".format(name,age)
  return get_message

if __name__ == "__main__":
  greet = compose_greet_function("balu", 20)
  print "I came to main"
  print greet()

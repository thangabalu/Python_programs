def my_generator():
  print "hello"
  yield 'a'
  yield 'b'
  yield 'c'


if __name__ =="__main__":
  for i in my_generator():
    print i

def main(val):
  while True:
    val = yield val
    print "value -{}".format(val)


if __name__ == "__main__":
  m = main(1)
  print m.send(None)
  for number in xrange(1,10):
    print m.send(number)
   

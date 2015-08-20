def generator_function():
  for i in xrange(1,11):
    yield i

def main():
  for i in generator_function():
    print i


if __name__ == "__main__":
  main()


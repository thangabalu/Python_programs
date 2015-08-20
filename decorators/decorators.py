def greet(name):
  def get_message():
    return "Hello "

  result = get_message() + name
  return result


if __name__ == "__main__":
  print greet("raghu")

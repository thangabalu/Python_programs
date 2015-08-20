def get_text(name):
  return "hello {} this is your name".format(name)

def p_decorate(func):
  def func_wrapper(name):
    return "<p>{}</p>".format(func(name))
  return func_wrapper


if __name__ == "__main__":
  my_get_text = p_decorate(get_text)
  print my_get_text("Balu")

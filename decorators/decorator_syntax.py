def p_decorate(func):
  def func_wrapper(name):
    return "<p>{}</p>".format(func(name))
  return func_wrapper

@p_decorate
def get_text(name):
  return "hello {} this is your name".format(name)

if __name__ == "__main__":
  print get_text("Balu")

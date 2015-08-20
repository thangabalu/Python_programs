def p_decorate(func):
  print "two"
  def func_wrapper(name):
    return "<p>{}</p>".format(func(name))
  return func_wrapper

def strong_decorate(func):
  print "one"
  def func_wrapper(name):
    return "<strong>{}</strong>".format(func(name))
  return func_wrapper


def div_decorate(func):
  print "three"
  def func_wrapper(name):
    return "<div>{}</div>".format(func(name))
  return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
  return "hello {} this is your name".format(name)

if __name__ == "__main__":
  #get_text = div_decorate(p_decorate(strong_decorate(get_text)))
  #print get_text("balu")
  print get_text("balu")

from functools import wraps

def tags(tag_name):
  def tags_decorator(func):
    @wraps(func)
    def func_wrapper(name):
      return "{0}{1}{0}".format(tag_name, func(name))
    return func_wrapper
  return tags_decorator

@tags("<div>")
@tags("<p>")
@tags("<strong>")
def get_text(name):
  """some doc string"""
  return "hello {}".format(name)

if __name__ == "__main__":
  print get_text("balu")
  print get_text.__name__
  print get_text.__doc__
  print get_text.__module__

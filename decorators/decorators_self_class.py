def p_decorate(func):
  def func_wrapper(self):
    return "<p>{}</p>".format(func(self))
  return func_wrapper

class Person(object):
  def __init__(self):
    self.name = "balu"
    self.family= "thiru"
  
  @p_decorate
  def get_fullname(self):
      return self.name+" "+self.family

if __name__ == "__main__":
  my_person = Person()
  print my_person.get_fullname()


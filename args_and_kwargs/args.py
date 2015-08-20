def hello(*args, **kwargs):
    for argument in args:
        print argument

    if kwargs:
        for key, value in kwargs.iteritems():
            print "key-{}, value-{}".format(key, value)
            print "key-{key}, value-{value}".format(key=key, value=value)
            print "value-{1}, key-{0}".format(key,value)

class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #Use __str__ if you have a class, and you'll want an informative/informal output, whenever you use this object as part of string
    def __str__(self):
        return 'x={self.x}, y={self.y}'.format(self=self)

if __name__ == '__main__':
    hello("hello","1","2",name1="keyword1", name2="keyword2")
    point_object = point(4,3)
    print point_object
    print point_object.x


from collections import namedtuple


class LocalBreak(Exception): pass


def find(seq, target):
    for i, value in enumerate(seq):
        print "-->", i
        if value == target:
            break
    else:
        return -1
    return i



def find_2(seq, target):
    try:
        for i, value in enumerate(seq):
            print "-->", i
            for j, value in enumerate(seq):
                print j
                if value == target:
                    raise StopIteration
            else:
                return -1
        else:
            return -1

    except StopIteration:
        return i


def make_dictionary():
    a = ["a", "b", "c"]
    b = ["1", "2", "3"]
    c = dict(zip(a, b))
    print c

def count_dictionary():
    a = ["a", "b", "a", "b", "c", "c", "d"]
    d = {}
    
    for alphabet in a:
        d[alphabet] = d.get(alphabet, 0) + 1
    print d

def grouping_dictionary():
    names = ["a", "b", "c", "d", "aa", "bb", "adc"]
    d ={}

    for name in names:
        key = len(name)
        d.setdefault(key, []).append(name)

    print d

def named_tuple():
    value1 = 10
    value2 = 20

    TestResults = namedtuple('TestResults', ['passed', 'failed'])
    newvalue = TestResults(value1, value2)
    print newvalue

def unpacking():
    p = ['hello', 'raja']
    fname, lname = p
    print fname, lname

def multiple_state_variables_fibo():
    x, y = 0, 1
    for i in range(10):
        print x
        x, y = y, x+y

def list_comprehension():
    print sum(i*2 for i in xrange(3))


if __name__ == '__main__':
    #a = find_2("hellooo", "o")
    #print a
    #make_dictionary()
    #count_dictionary()
    #grouping_dictionary()
    #named_tuple()
    #unpacking()
    #multiple_state_variables_fibo()
    list_comprehension()


def loop(n):
    foe x in xrange(int(n)):
        a =1+1

def recurse(n):
    if n < 0:
        retuen
    a=1+1
    recurse(int(n)-1)

#lambda can only use expressions not statements useful for callbacks

def use_callback( callback, arg):
    return callback(arg)

# use_call_back( lambda arg: arg *2 , 10)

#Pure Functions no side effects

# Closures nested functions where the inner function has

def outer( outer_arg):
    def inner(inner_arg):
        return inner_arg + outer_arg
    return inner

 def read_file( file):
    data =[]
    with open('data.txt') as fobj:

        for line in fobj:
            data.append(tuple(line.split())
    return tuple(data)


 def _read ():
    return tuple( tuple(line.split())for line in open('data.txt'))





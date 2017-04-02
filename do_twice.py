def do_twice(f,s):
    f(s)
    f(s)

def print_twice(s):
    print 'spam'

do_twice(print_twice,'spam')

def do_four(f,s):
    do_twice(f,s)
    do_twice(f,s)

do_four(print_twice,'spam')

def print_pipe(x):
    sqv = '| ' + '  ' * 4
    sqev = '|'
    print sqv * x + sqev

def print_head(x):
    sqh = '+ ' + '- ' * 4
    sqeh = '+'
    print sqh * x + sqeh

def do_twice(p):
    print_pipe(p)
    print_pipe(p)

def do_four(f,x):
    f(x)
    f(x)

def grid(x,y):
    for yy in range(0 , y):
        print_head(x)
        do_four(do_twice,x)
    print_head(x)

grid(4,4)

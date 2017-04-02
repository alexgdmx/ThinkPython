def grid(x,y):
    for yy in range(0 , y):
        sqh = '+ '+'- '*4
        sqeh = '+'
        sqv = '| '+'  '*4
        sqev = '|'
        print sqh*x+sqeh
        print sqv*x+sqev
        print sqv*x+sqev
        print sqv*x+sqev
        print sqv*x+sqev
    print sqh*x+sqeh

grid(9,9)

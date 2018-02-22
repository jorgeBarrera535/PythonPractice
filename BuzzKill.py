def buzzkill(num1,num2) :
    fun = False
    if (num1 % num2 == 0):
        fun = True
    return fun
    
    
    
for x in range(1,100):
    
    if (x % 3 == 0 and x  % 5 == 0) :
        print "fizzbuzz"
    elif (buzzkill(x,3)) :
        print "fizz"
    elif (x % 5 == 0) :
        print "buzz"
    else:
        print x

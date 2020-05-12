def parzyste():
    a=2;
    while 1:
        yield a

def dosk():
    suma=0
    licz=0
    i = 6
    while True:
        for o in range(1,i):
            if i%o==0: 
                suma+=o
                licz=suma
        if suma == i: yield licz
        else: 
            i=i+1
            suma=0

def fib():
    a,b = 0,1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b


#p = [i for i in range(1,100000000000)]
a = parzyste()
#for i in range(0,10):
#    print(next(a))


f = fib()
#for i in range(0,1000000000000000000000):
#    print(next(f))
print(next(f)) #0
print(next(f)) #1
print(next(f)) #1
print(next(f)) #2

d = dosk()
print(next(d))
print(next(d))
print(next(d))

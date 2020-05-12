def parzyste():
    a=2;
    while 1:
        yield a
        a+=2

def fib():
    a,b = 0,1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b

a = parzyste()
for i in range(0,100):
    print(next(a))

f = fib()
for i in range(0,100):
    print(next(f))
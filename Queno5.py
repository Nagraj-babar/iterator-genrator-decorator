# Create a generator to produce first n terms of Fibonacci series
def fib(N):
    a=0
    b=1
    yield a
    yield b
    while True:
        a=a+b
        yield a
        b=b+a
        yield b
num=int(input('Enter a number: '))
it=iter(fib(num))
c=1
while c<=num:
 print(next(it))
 c+=1
    


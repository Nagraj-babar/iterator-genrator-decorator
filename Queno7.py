# Create an endless iterator using generator method to produce terms of Fibonacci series
def fib():
    a=0
    b=1
    yield a
    yield b
    while True:
     a=a+b
     yield a
     b=b+a
     yield b
it=iter(fib())
while True:
 print(next(it))

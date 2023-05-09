# Create a generator to produce squares of first N natural numbers
def f1(a):
    b=0
    while a>=b:
        yield b**2
        b=b+1
it=f1(10)
while it!=0:
    try:
     print(next(it))
    except StopIteration:
       print('All elements are accessed')
       break

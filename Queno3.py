# Create a generator to produce first n even natural numbers
def f1(a):
    b=0
    while a>=b:
        if b%2==0:
            yield b
        b=b+1
it=f1(10)
while it!=0:
    try:
     print(next(it))
    except StopIteration:
       print('All Element are accessed')
       break
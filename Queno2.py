# Create a generator to produce first n odd natural numbers
def f1(a):
    b=0
    while a>=b:
        if b%2!=0:
            yield b
        b=b+1
it=f1(10)
while it!=1:
    try:
     print(next(it))
    except StopIteration:
       print('all element are accessed')
       break


# Create an endless iterator using generator method to produce Prime numbers
def prime():
    a=2
    while True:
     for e in range(2,a):
        if a%e==0:
            break
     else:
         yield a
     a+=1
it=iter(prime())
i=0
while True:
   print(next(it))
   i+=1


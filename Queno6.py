 # Create a generator to produce first n prime numbers
def prime(N):
    while True:
        N+=1
        for e in range(2,N):
            if N%e==0:
                break
        else:
            return N
def getnum(num):
    n=1
    count=1
    while count<=num:
        n=prime(n)
        yield n
        count+=1
num1=int(input("Enter a number: "))
for i in getnum(num1):
    print(i)
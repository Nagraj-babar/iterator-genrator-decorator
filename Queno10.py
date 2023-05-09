'''Define a function which calculates HCF of two numbers. Define and apply a
decorator to check whether two given numbers are co-prime or not.'''
def decor_HCF(FUN_HCF):
    def coprime(a,b):
        l3=[]
        l4=[]
        y=range(2,a+1)
        u=range(2,b+1)
        for i in y:
            if a%i==0:
                l3.append(i)
        for o in u:
            if b%o==0:
                l4.append(o)
        s3=set(l3)
        s4=set(l4)
        co_prime=[int(p) for p in s3.intersection(s4)]
        if len(co_prime)>=1:
                FUN_HCF(a,b)
        else:
              print('This two numbers are co-prime')
    return coprime
@decor_HCF
def HCF(a,b):
    l1=[]
    l2=[]
    r=range(2,a+1)
    g=range(2,b+1)
    for e in r:
        if a%e==0:
            l1.append(e)   
    for t in g:
        if b%t==0:
            l2.append(t)
    s1=set(l1)
    s2=set(l2)
    hcl=s1.intersection(s2)
    MAXhcl=max(hcl)
    print(MAXhcl)
HCF(60,40)

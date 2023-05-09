# Use iter and next method to access all the elements of a given set using while loop
s1={1,2,3,4,5}
i=0
it=iter(s1)
while i<=len(s1):
      a=next(it)
      print(a)
      i+=1
     
    

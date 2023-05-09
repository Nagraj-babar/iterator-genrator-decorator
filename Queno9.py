'''Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides.'''
def decor_Triangel(fun_Triangel):
    def decor_triangel(a,b,c):
        if a+b>=c and b+c>=a and a+c>=b:
            fun_Triangel(a,b,c)
        else:
            print('Triangel is not valid')   
    return decor_triangel
@decor_Triangel
def Triangel(a,b,c):
    perimeter= a+b+c
    print(perimeter)
d=int(input("Enter a length of a to b: "))
e=int(input('Enter a legnth of b to c: '))
f=int(input('Enter a lenght of c to a: '))
Triangel(d,e,f)

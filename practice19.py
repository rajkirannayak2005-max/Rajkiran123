#write a program using function to find greatest of three number
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number"))
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
result=greatest(a,b,c)
print("greatest number is",result)    
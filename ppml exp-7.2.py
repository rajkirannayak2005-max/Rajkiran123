#write a function to check wheather it is odd or even
n=int(input("enter a number:"))
def check(n):
 if n%2==0:
    return "even"
 else:
   return "odd"
result=check(n) 
print("the number is:",result)
 
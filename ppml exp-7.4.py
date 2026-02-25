#write a program to check number is prime or not
n=int(input("enter the number:"))
def prime(n):
    if n<=1:
        return "false"
    else:
        return n%n==0 and n%1==0
result=prime(n)
print("the number is prime",result)    
       
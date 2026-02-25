#write a function to find the factorial of a number
n=int(input("enter a number:"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
result=factorial(n) 
print("factorial of number is:",result)     
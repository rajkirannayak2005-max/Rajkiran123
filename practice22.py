#write a recursive function to calculate the sum of first n natural number
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
    
number=int(input("enter a number:"))
result=sum(number)
print("sum of natural number is:",result)    
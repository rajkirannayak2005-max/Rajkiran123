#write a program to find the square of a number using function
def square(n):
    s=n*n
    return s
number=int(input("enter the number:"))
result=square(number)
print("square of number is:",result)
#write a function to calculate simple interest
p=float(input("enter principal:"))
r=float(input("enter rate:"))
t=float(input("enter time in year:"))
def simple_interest(p,r,t):
    return (p*t*r)/100
print("simple interest is :", simple_interest(p,t,r))
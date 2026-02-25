#write a function to calculate that accepts a list &returns the sum of its elements
l = []

n = int(input("How many elements? "))

for i in range(n):
    element = int(input("Enter element: "))
    l.append(element)

print("List is:", l)
def sum_list(l):
    total=0
    

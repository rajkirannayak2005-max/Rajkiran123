#write a program to separte even and odd elements from list
even_number = []
odd_number = []

numbers = [2,3,4,5,6,7,8,9,20]

for num in numbers:
    if num % 2 == 0:
        even_number.append(num)
    else:
        odd_number.append(num)

print("\nEven numbers:", even_number)
print("Odd numbers:", odd_number)

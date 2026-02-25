#write a program to input eight numbers from the user and display alll the unique numbers 
# Program to input eight numbers and display unique numbers

numbers = []

# Taking 8 numbers as input
for i in range(8):
    num = int(input("Enter number: "))
    numbers.append(num)

# Convert list to set to get unique numbers
unique_numbers = set(numbers)

# Display unique numbers
print("Unique numbers are:", unique_numbers)

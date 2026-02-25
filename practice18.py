s1 = float(input("Enter the mark in s1: "))
s2 = float(input("Enter the mark in s2: "))
s3 = float(input("Enter the mark in s3: "))

total_marks = 300

# Calculate overall percentage
p = ((s1 + s2 + s3) / total_marks) * 100

# Check pass condition (minimum 33 in each subject)
if s1 >= 33 and s2 >= 33 and s3 >= 33:
    if p >= 40:
        print("Pass in all subjects")
    else:
        print("Failed due to low overall percentage")
else:
    print("Failed in one or more subjects")

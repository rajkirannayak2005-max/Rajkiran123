#create an empty dictionary allow 4 freinds enter their favourite language
# Create an empty dictionary
friends = {}

# Taking input from 4 friends
for i in range(4):
    name = input("Enter friend's name: ")
    language = input("Enter their favourite language: ")
    friends[name] = language

# Display the dictionary
print("Friends and their favourite languages are:")
print(friends)

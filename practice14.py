#write a program to create a dictionary ofhindi word with values as their english translation .provide user with an option to look it up
# Create a dictionary of Hindi words with English meanings

dictionary = {
    "pani": "water",
    "kitaab": "book",
    "ghar": "house",
    "dost": "friend",
    "roti": "bread"
}

# Take input from user
word = input("Enter a Hindi word to find its English meaning: ")

# Check if word exists in dictionary
if word in dictionary:
    print("The English meaning is:", dictionary[word])
else:
    print("Sorry! Word not found in dictionary.")

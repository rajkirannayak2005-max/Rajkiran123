#write a program to count vowels in a string
text=input("enter a string:")
def count_vowels(text):
    count=0
    vowels="aeiouAEIOU"
    for char in text:
        if char in vowels:
            count+=1
            return count
result=count_vowels(text)
print("number of vowels are:",result)            

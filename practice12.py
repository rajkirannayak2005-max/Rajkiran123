#write a program to fill a letter templet below with name and date
name=input("enter your name:")
date=input("enter date:")
letter='''Dear {name},
                 you are selected!
                 {date}'''

print(letter.format(date=date , name=name))
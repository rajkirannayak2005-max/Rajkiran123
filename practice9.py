#write a program to find common element between two list
#l1=[1,2,3,4,5,6,7,8,9,10]
#l2=[1,2,3,4,5]
#com=list(set(l1) & set(l2))
#print(com)

l1=[1,2,3,4,5]
l2=[1,2,3]
com=[]

for i in l1:
    if i in l2:
        com.append(i)

print("common element",com)        
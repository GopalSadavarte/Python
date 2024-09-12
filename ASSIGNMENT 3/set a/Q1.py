#1. Write a Python program to find maximum and the minimum value in a set. 
set1=set()
size = int(input("Enter size of set:"))
for i in range(0,size):
    ob=input("Enter {} set element:".format(i+1))
    set1.add(ob)
print("The set is :",end='\n')
for i in set1:
    print(i,end='\t')
print(end='\n')
print("The minimum value is :",min(set1))
print("The maximum value is :",max(set1))
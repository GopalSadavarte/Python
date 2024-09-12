#. Write a python script which accepts 5 integer values and prints “DUPLICATES” if any of the 
# values entered are duplicates otherwise it prints “ALL UNIQUE”. Example: Let 5 integers are (32, 
# 45, 90, 45, 6) then output “DUPLICATES” to be printed. 


numbers = input("Enter 5 integers which separate by commas:").split(',')
numbers.sort()
flag=0
for i  in range(0,len(numbers)):
    if(i+1 != len(numbers)):
        if(numbers[i] == numbers[i+1]):
            flag=1
            break

if(flag==0):
    print("All Unique!!")
else:
    print("Duplicate!!")
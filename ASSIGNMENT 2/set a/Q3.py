#Write a Python program to remove the characters which have odd index values of a given string. 
string =[*input("Enter a string:")]
print(string)
for i in range(0,len(string)-1):
    if(i % 2 != 0):
       string.remove(string[i])
  
str1=''     
for i in string:
    str1=str1.__add__(i)
    
print(str1)
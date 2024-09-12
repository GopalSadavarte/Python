# 2. Write a Python program to get a single string from two given strings, separated by a space and 
# swap the first two characters of each string. 
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xycabz' 

str1=input("Enter first string:")
str2=input("Enter second string:")

str3=str2[0:2]+str1[2:]+str1[0:2]+str2[2:]
print(str3)
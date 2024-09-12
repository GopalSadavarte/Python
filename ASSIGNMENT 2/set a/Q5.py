#5. Write a Python program to get a string from a given string where all occurrences of its first char 
# have been changed to '$', except the first char itself. Sample String: 'restart' Expected Result : 
# 'resta$t' 

string = input("Enter a string:")
first = string[0]
string = string.replace(first,'$')
string = string.replace('$',first,1)
print(string)
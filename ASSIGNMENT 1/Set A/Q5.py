# Write a program to check whether a input number is palindrome or not. 
num = temp = input("Enter a number:")
if num[::-1]==temp:
    print("The string ",temp," is palindrome!")
else:
    print("The string ",temp," not a palindrome!")

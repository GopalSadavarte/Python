# Write a program to calculate sum of first and last digit of a number. 
num = input("Enter a number:")
# numL=[*num]
# sum=int(numL.pop())+int(numL.pop(0))
# print("The sum of first and last digit are ",sum)

sum = int(num[-1])+int(num[0])
print("The sum of first and last digit are ",sum)
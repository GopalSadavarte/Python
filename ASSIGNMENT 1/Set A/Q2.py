# Write python script to check whether a input number is Armstrong number or not
num = int(input("Enter a number:"))
temp = num
sum=0
length= len(str(num))
while int(num)>0:
    d=int(num%10)
    sum+=d**length
    num/=10

if temp == sum:
    print("The ",temp," is Armstrong!")
else:
    print("The ",temp," not a Armstrong!")
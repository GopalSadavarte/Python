#Write python script to check whether a input number is perfect number of not. 
num=int(input("Enter a number:"))
sum=0
for i in range(1,int(num/2)+1):
    if int(num%i) == 0:
        sum+=i
if(sum==num):
    print("The number ",num," is perfect!")
else:
    print("The number ",num," not a perfect!")
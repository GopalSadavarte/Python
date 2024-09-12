#Write python script to calculate sum of digits of a given input number. 
# num = int(input("Enter a number:"))
# sum=0
# while num>0:
#     d=int(num%10)
#     sum+=d
#     num/=10
# print("Sum is ",sum)

num=[*input("Enter a number:")]
# j=0
# for i in num:
#     num[j]=int(i)
#     j+=1
# print(sum(num))
sum=0 
for i in num: sum+=int(i)
print("The Sum is ",sum)
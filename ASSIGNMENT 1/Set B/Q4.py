# Write a program which accept an integer value ‘n’ and display all prime numbers till ‘n’. 
num = int(input("Enter a number:"))
for i in range(2,num+1):
    f=0
    for j in range(2,i):
        if int(i%j)==0:
            f=1
            break
    if f==0:
        print(i) 
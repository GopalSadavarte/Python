''' Write python script to accept two numbers as range and display multiplication table of all numbers within 
that range. '''
num1=int(input("Enter start number:"))
num2=int(input("Enter End number:"))
for i in range(num1,num2+1):
    for j in range(1,11):
        print(i*j,end='\n')
    print()
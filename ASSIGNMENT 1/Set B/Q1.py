#Write a program to accept a number and count number of even, odd, zero digits within that number. 
num = input("Enter a number:")
evenCount=oddCount=zeroCount=0
for i in num:
    d=int(i)
    if d==0:
        zeroCount+=1
    elif int(d%2)==0:
        evenCount+=1
    else:
        oddCount+=1
print("Total Even digits:",evenCount,end='\n')
print("Total Odd digits:",oddCount,end='\n')
print("Total Zero digits:",zeroCount,end='\n')

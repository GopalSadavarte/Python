#3. Write a python program to count vowels and consonants in a string. 
vowels = ('a','e','i','o','u','A','E','I','O','U')
string = input("Enter a string:")
vCount=cCount=0

for i in string:
    if(vowels.__contains__(i)):
        vCount+=1
    else:
        cCount+=1


print("Total vowels are:",vCount)
print("Total consonants are:",cCount)
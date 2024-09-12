#5. Write a python program to count repeated characters in a string. 
# Sample string: 'thequickbrownfoxjumpsoverthelazydog' 
# Expected output: 
# o 4 
# e 3 
# u 2 
# h 2 
# r 2 
# t 2

string = input("Enter a string:")
dic={}

for i in string:
    if(dic.__contains__(i)):
        dic.update({i:dic[i]+1})
    else:
        dic.__setitem__(i,1)
        
for i in dic:
    if(dic[i] > 1):
        print(i," of ",dic[i])
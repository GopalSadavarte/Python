#2. Write a python script to count the number of characters (character frequency) in a string. Sample 
# String : google.com'. Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 

string = input("Enter a string:")
dic={}

for i in string:
    if(dic.__contains__(i)):    
        dic.update({i:dic[i]+1})
    else:
        dic.__setitem__(i,1)
    
for i in dic:
    print(i ,'of ',dic[i])
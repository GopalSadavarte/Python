#3. Write a Python program to count the occurrences of each word in a given sentence. 

sentence = input("Enter a sentence:").split(' ')
occ={}

for i in sentence:
    if(occ.__contains__(i)):
        occ.update({i:occ[i]+1})
    else:
        occ.__setitem__(i,1)
        
for i in occ:
    print(i,"of ",occ[i])
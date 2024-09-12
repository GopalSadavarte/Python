# 1. Write a binary search function which searches an item in a sorted list. The function should return 
# the index of element to be searched in the list. 

def binarySearch(li:list,start,end,item):
    if(start <= end):
        mid=int((start+end)/2)
        if(li[mid]==item):
            return mid
        elif(li[mid]>item):
           return binarySearch(li,0,mid-1,item)
        elif(li[mid]<item):
           return binarySearch(li,mid+1,end,item)
    else:
        return False
    
lis=[]
size = int(input("Enter size of list:"))
for i in range(0,size):
    ob=input("Enter {} list element:".format(i+1))
    lis.append(ob)

lis.sort()
search = input("Enter element for search:")
if(res:=binarySearch(lis,0,lis.__len__()-1,search)):
    print("The list is:",end='\n')
    for i in lis:
        print(i,end='\t')
    print(end='\n')
    print("The element {} are found in {} index position..".format(search,res))
else:
    print("Element not found!")
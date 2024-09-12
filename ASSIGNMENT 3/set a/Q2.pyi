# 2. Write a Python program to add an item in a tuple. 

# the tuple with collection of sets
tu=({1,2,3},{1,2,3,4,5},{6,7,8,9})
# the tuple with collection of integers
t2=(23,32,43,43,42)

lis=list(tu)
lis.append(23)
tu=tuple(lis)
print(tu)

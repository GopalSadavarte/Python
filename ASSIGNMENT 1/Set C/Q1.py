'''. Write a python script to generate the following pattern upto n lines 
      1 
    1 2 1 
  1 2 3 2 1 
1 2 3 4 3 2 1 
'''
r=int(input("Enter a number for range:"))
for i in range(1,r+1):
    print(' '*(r-i))
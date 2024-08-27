#Write a program which accepts an integer value as command line and print “Ok” if value is between 1 to 
#50 (both inclusive) otherwise it prints ”Out of range” 
import sys as s
if (int(s.argv[1])>=1) and (int(s.argv[1])<=50):
    print("Ok")
else:
    print("Out of range!")
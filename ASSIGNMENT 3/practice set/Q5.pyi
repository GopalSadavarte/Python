# 5. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20} 
# Expected Result : {0: 10, 1: 20, 2: 30} 

di={'name':'gopal','address':'nagar','phone':'8956438885'}
print("The original dictionary are:")
for i in di:
    print(i,' :',di[i])

di.__setitem__('BoD','11/06/2004')
print("after adding data the dictionary are:")
for i in di:
    print(i,' :',di[i])
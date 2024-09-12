# 6. Write a Python script to check if a given key already exists in a dictionary. 
di={
    'name':'rakesh',
    'date':'11/03/2000',
    'class':'F.Y.B.B.A.(C.A.)'
}

if(di.__contains__('name')):
    print('exist')
else:
    print('not exist')
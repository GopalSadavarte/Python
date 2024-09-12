# 4. Write a program to implement the concept of queue using list
list1=[]
flag = 0
while (flag == 0):
    print("Choices:",end='\n')
    print("1.create",end='\n')
    print("2.insert",end='\n')
    print("3.delete",end='\n')
    print("4.display",end='\n')
    print("5.Exit",end='\n')
    
    ch=int(input("Enter your choice:"))
    try:
        match ch:
            case 1:
                size = int(input("Enter size of list:"))
                for i in range(0,size):
                    d=input("Enter list item:")
                    list1.append(d)
            case 2:
                new = input("Enter item to insert")
                list1.insert(list1.__len__() ,new)
            case 3:
                list1.remove(list1[0])
            case 4:
                for i in list1:
                    print(i,end='\n')
            case 5:
                print("Exited")
                flag=1
    except IndexError as exc:
        print("index out of range ,please create a list.")
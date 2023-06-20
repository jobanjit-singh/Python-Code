def linearSearch(li1,value):# li1 = [1,3,2],value = 2
    flag = 0 #flag = 1
    for i in li1: #i=2
        if(i==value):
            flag = 1

    if(flag == 1):
        print("Found")
    else:
        print("Not Found")

n = eval(input("Enter the no of element:- "))
# n =3
l = [] #l = [1,3,2]

for i in range(1,n+1): #[1,3,2]
    x = eval(input("Enter the element:- "))
    l.append(x)

value = eval(input("Enter the value which you want to search:- "))
#value = 2
linearSearch(l,value)
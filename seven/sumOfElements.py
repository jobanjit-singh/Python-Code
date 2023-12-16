#sum of elements of list

def sumOfList(l):
    ans = 0 #l=[1,2,3] ans = 6
    #                 i
    for i in l: #[1,2,3]
        ans = ans + i # 3 + 3

    return ans
    

n = eval(input("Enter the number of element:- ")) #n = 4

l = []

for i in range(1,n+1): #[1,2,3,4]
    x = eval(input("Enter element:- "))
    l.append(x)

var = sumOfList(l)
print("The sum of list is",var)
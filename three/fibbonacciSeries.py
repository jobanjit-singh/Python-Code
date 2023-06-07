# 0 1 1 2 3 5 user number 6
# a b c
#   a b c
num = eval(input("Enter the number:- ")) #num = 3

a = 0
b = 1

if(num == 1):
    print(a)
elif(num == 2):
    print(a)
    print(b)                #output:- 0
                                   #  1
                                   #  1
else:
    print(a)
    print(b)
    #                range(3,4) = [3]
    for i in range(3,num+1): 
        c = a + b
        print(c)
        a = b
        b = c

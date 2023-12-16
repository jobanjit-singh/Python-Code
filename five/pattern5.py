#--*
#-**
#***
n = 3 # n = 3
for i in range(1,n+1): #row [1,2,3] i = 3

    #space
    j = n-1 #j = 2
    while(j >= i): # 2 >= 3
        print(" ",end="")
        j = j - 1
    
    #star
    k = 1
    while(k <= i):
        print("*",end="")
        k = k + 1
    print()
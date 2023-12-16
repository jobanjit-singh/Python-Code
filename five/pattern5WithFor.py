#--*
#-**
#***
#                      i
for i in range(1,4): #[1,2,3]
    #space 
    #                      j
    for j in range(i,3): #[1,2]
        print(" ",end="")
    #star
    for k in range(1,i+1):#[1]
        print("*",end="") #--
    print()

# -
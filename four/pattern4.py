# *
# * *
# * * * 
# * * * *

# * * *
# * *
# *

n = 4
# First Pattern
for i in range(1,n+1): #row
    for j in range(1,i+1):#columns
        print("* ",end="")
    print()

# second Pattern
i = 1 # i = 2
while(i <= n-1): # row 2 <= 3
    j = n-1 # j = 3
    while(j >= i): #columns 3 >= 1
        print("* ",end="")
        j = j - 1
    print()
    i = i + 1

#output :- * * * 
#       
# 
# 
# range(3,0,-1)   
# 
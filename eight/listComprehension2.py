l = [1,2,3,4,5] 
def print1(num): #print1(num=3)
    print("This is num",num)
    return num
l5 = [print1(i) for i in l]
# l5 = [2 for i in l]
#          i
# l = [1,2,3,4,5]
#l5 = [1,2]
[print(i) for i in l]
print(l5)

#output = this is num 1
        # this is num 2
        # this is num 3
l = [1,2,3,4,5]
def print1(num):
    print("This is num",num)
    return num
# for i in l:
#     if(i%2==0):
#         print(i)

l1 = [x for x in l if x%2 == 0]
#            x
# l=[1,2,3,4,5]  = [2,4]

l2 = ["even" for x in l if x%2 == 0]
#            x
# l=[1,2,3,4,5] = [even,even]

l3 = [x if x%2 == 0 else 0 for x in l]
#              x 
# l = [1,2,3,4,5] = [0,2,0,4,0]

l4 = ["even" if i%2 == 0 else "odd" for i in l]
#           i
#l=[1,2,3,4,5] => l4 = [odd,even,odd,even,odd]

l5 = [print(i) for i in l4]
#          i
# l4=[odd,even,odd,even,odd] i= even
# l5=[None,None]
# print(l5) #output = odd
#                   even

print(l4)
print(l5)

# l1 = [2,4]
#        x 
# l = [1,2,3,4,5]
# print(l1)
# print(l2)
# print(l3)
# print(l4)

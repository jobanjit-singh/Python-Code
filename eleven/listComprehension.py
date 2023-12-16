# l = [1,2,3,4,5]
#                 i
# #        [1,2,3,4,5]
# for i in l:
#     print(i)

# newList = [x for x in range(1,11)]
# l = [x for x in range(1,6)]
#                   x
# range(1,11) = 1,2,3,4,5,6,7,8,9,10

#[1,2,3,4,5,6,7,8,9,10]
# evenList = [x for x in range(2,11,2)]
# List1 = ['hlo' for x in range(2,11,2)]
#                           x
# range(2,11,2) = [2,4,6,8,10]

# print(List1)
# # print(type(newList))
# print(l)
# print(evenList)


#                                  i
#range(1,11) = [1,2,3,4,5,6,7,8,9,10]
# l = [i for i in range(1,11) if i%2 == 0]

# for i in range(1,11): i=10
    # if(i%2 == 0):
        # add i into list

# l = [2,4,6,8,10]

# list1 = [var**2 for var in range(1,5)]
# for var in range(1,5):
#      add into list var**2


# print(list1)

#print() is a function built in
# 2 task:- 1.Print value into console
#          2.None 


l = [print(i) for i in range(1,5)]
print(l)

# l = [None,None,None,None]
#                             i 
# for i in range(1,5): [1,2,3,4]
#           print(i)
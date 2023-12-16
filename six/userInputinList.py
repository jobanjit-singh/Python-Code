n = eval(input("Enter the number of element:- ")) #n = 3

#creation of empty list
l = [] # l = [1,14,5]
  #           0, 1,2


#user input
for i in range(1,n+1): # i = 3
    x = eval(input("Enter the element:- ")) # x = 5
    l.append(x)

#printing the whole list
print("The list is:-",l)

print()

#iterate of list
# using index start 0
# using for loop

#iteration using index (While loop)
i = 0 #i=3
while(i < len(l)): # 3 < 3
    print(l[i]) # l[2] = 5
    i = i + 1

# iterate using for loop
#                  i
for i in l: #[1,14,5]
    print(i)

# range(1,5) 1,2,3,4
#                i
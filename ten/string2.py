# string traversing

s = "python"
#traveresing using for loop
#         i
#        "python"
# for i in s:
#     print(i)

#traversing using while loop

#index       "p y t h o n"
#+ve index    0 1 2 3 4 5
#-ve index   -6-5-4-3-2-1

# length = len(s)

l = len(s) # l = 6
var = 0 # var = 5
#      5 < 6 = true
while(var < l):
    print(s[var]) # s[5] = n
    var = var + 1

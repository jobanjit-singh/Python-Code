s = "hello"

#conversion into list
StrList = list(s) 

#['h','e','l','l','o']
#  0   1   2   3   4

i = 0 #i = 2
j = len(StrList)-1 #j = 2

while(i < j): #2 < 2
    temp = StrList[i] # temp = 'h' => StrList[1]
    StrList[i] = StrList[j] # StrList[1] = StrList[3]
    StrList[j] = temp # StrList[3] = 'h'

    i = i+1
    j = j-1

print(StrList)
#['o','l','l','e','h']

# "o-l-l-e-h"

# s = ''.join(StrList)

s = "" # s = "olleh"
#                            i
#          ['o','l','l','e','h']
for i in StrList:
    s = s+i # "olle" = "olle"+'h'
print(type(StrList[0]))
print(type(s))
print(s)


# idle Code:-
# >>> s = "hello"
# >>> l = list(s)
# >>> l
# ['h', 'e', 'l', 'l', 'o']
# >>> l[0] = 'H'
# >>> l
# ['H', 'e', 'l', 'l', 'o']
# >>> s[0] = "H"
# Traceback (most recent call last):
#   File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
#     exec(code, self.locals)
#   File "<pyshell#5>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# >>> 

# check the string is palindrome or not

# oppo
# oppo - reverse same palindrome

# abcd
# dcba - reverse not palindrome

# oppo
#  ij

s = input("Enter the string:- ") # abcd 

i = 0 # i = 0
j = len(s) - 1 #j = 3
flag = 1 #flag = 0

#     0 < 3 true
while(i < j):
    if(s[i] != s[j]): # a != d true
        flag = 0
        break
    else:
        i = i + 1
        j = j - 1

if(flag == 1):
    print("Palindrome")
else:
    print("Not Palindrome")
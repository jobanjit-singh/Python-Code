s = "hello"
# s[0] = "H" not possible because string is immutable

# input = hello
# output = olleh

# h   e  l   l   o
# 0   1  2   3   4

ans = "" #ans = "olleh"


strLenght = len(s)  # strlenght = 5

 
#        range(4,-1,-1)                      i
for i in range(strLenght-1,-1,-1): #[4,3,2,1,0]
    ans = ans + s[i] #s[0]

print(ans)

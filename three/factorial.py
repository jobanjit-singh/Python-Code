# 4 = 4*3*2*1

a = eval(input("Enter the number:- ")) # a = 4
num = a # num = 1
ans = 1  # ans = 24

while(num >= 1):  # 2 >= 1 true
    ans = ans * num # ans = ans * num 24 * 1 = 24
    num = num - 1 # 1-1 = 0

print("The Factorial of",a,"is",ans)
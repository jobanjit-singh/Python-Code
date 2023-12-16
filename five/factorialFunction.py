def facto(a):
    ans = 1
    for i in range(1,a+1):
        ans = ans * i
    return ans

n = eval(input("Enter the value of n:- "))

ans = facto(n)

print("The factorial of",n,"is",ans)
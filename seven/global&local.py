# global and local variables 

def print1():
    print("Execution inside function")
    # a = "python variable a inside print1"
    # a = "python1"
    global a
    a = a + "str" #a = "python"+"str"
    print(a)
    # var = 2

a = "Python"
print1()

print("Execution outside the function")
print(a)
print(var)
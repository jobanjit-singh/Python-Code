# write a code to print even numbers from 1 to 100
# a = 1 # 1 
a = eval(input("Enter the number from where you want to start:- "))
stoprange = eval(input("Enter the stopping value:- "))
while(a<=stoprange): #true
    if(a % 2 == 0): #false
        print(a)
    a = a + 1

# a = 0 #4 
# while(a<=100): #true
#     print(a) # 0 2 
#     a = a + 2 # a = 2+2
# find the grade of student marks

a = eval(input("Enter the marks:- ")) #39

#    false
if(a >= 80 and a <= 100): #false
    print("The user Grade is A")
    print("Congratulations")
    # false
elif(a >= 60 and a < 80): #false
    print("The user grade is B")
    # true         true
elif(a >= 40 and a < 60): #true
    print("The user grade is C")
    # true
else:
    print("the user is fail")
# elif(a < 40 and a>0):
#     print("The user is fail")
#     print("Try again")
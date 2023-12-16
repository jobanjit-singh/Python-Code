# Conditional Statements
# if statement done
# if else statement done
# if elif statement done
# nested if else

#-----------------------------------
#if else statement

# if(a>10){

# }

# a = 10
# if a > 18: # false
#     print("you are eligible for voting")
# else:
#     print("You are not eligible for voting")

# print("Thanks for checking")

# check the number is positive or not
# n = eval(input("Enter the value of n:- ")) # 0
# if n > 0: # false
#     print("The Number is positive")
# elif n == 0: # true
#     print("The number is zero")
# else:
#     print("Number is -ve")

# print("Done")

#------------------------------------------------
# Nested if else statement
# Grading System

marks = eval(input("Enter your marks:- "))

if marks > 80:
    if marks <= 100:
        print("Grade A")
        print("congratulations")
    else:
        print("Pagal samjhe ho kya")
elif marks >= 60 and marks <= 80:
    print("Grade B")
    print("Congratulations")
elif marks >= 40 and marks <= 60:
    print("Grade C")
    print("Perform Better")
else:
    if marks == 0:
        print("padhle kuch bhai")
    elif marks < 40:
        print("Sorry! you are fail")
        print("Try again")

print("ABC College Result portal")


# format function is used to handle complex strings
# 1. place holder = {}
# 2. format function


#single placeholder
# str = "this is {}"
# print(str.format("placeholder"))

# print("this is {}".format("Placeholder"))

# s = "the cost is {cost:.2f} ruppees"
# print(s.format(cost=30))

#multiple placeholder

# s = "{}, Good {}"
# print(s.format("Hi","Evening"))

# s = "{0}, Good {1}"
# print(s.format("hi","morning"))
# index         0       1 

# s = "{1}, Good {0}"
# print(s.format("hi","morning"))
# index         0       1 


# s = "{}, Good Morning{} How are you?"
# print(s.format("hi"))

# s = "{}, Good {}{},How are you?"
# print(s.format("Hi","Morning","\t"))

#s = "{}jobanjit singh{}" # "jobanjit Singh"
# print(s.format("\"","\""))

# printf("Hello world %d",i)

v = "Geeks"
print(f"{v}for{v}")

# print("Hello World! %.2f"%(30.23423))

# print("The %s is %d"%("cost",40))


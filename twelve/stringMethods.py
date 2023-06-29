# #python Methods 

# >>> s = "python"
# >>> s[0] = "P"
# Traceback (most recent call last):
#   File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
#     exec(code, self.locals)
#   File "<pyshell#1>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# >>> s
# 'python'
# >>> s = ""
# >>> s
# ''
# >>> s
# ''
# >>> s
# ''
# >>> s = "python"
# >>> s
# 'python'
# >>> s.capitalize()
# 'Python'
# >>> s
# 'python'
# >>> s1 = s.capitalize()
# >>> s1
# 'Python'
# >>> s = s.capitalize()
# >>> s
# 'Python'
# >>> s = "PYTHON"
# >>> s.casefold()
# 'python'
# >>> s
# 'PYTHON'
# >>> s.center()
# Traceback (most recent call last):
#   File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
#     exec(code, self.locals)
#   File "<pyshell#18>", line 1, in <module>
# TypeError: center expected at least 1 argument, got 0
# >>> s.center(20)
# '       PYTHON       '
# >>> s.count("O")
# 1
# >>> s.count("A")
# 0
# >>> s.encode()
# b'PYTHON'
# >>> s.encode(encoding="ascii")
# b'PYTHON'
# >>> s.encode(encoding="ascii",errors="ignore")
# b'PYTHON'
# >>> s.endswith("N")
# True
# >>> s
# 'PYTHON'
# >>> s = "abc@gmail.com"
# >>> s.endswith("@gmail.com")
# True
# >>> s.find("@")
# 3
# >>> s.find("@gmail")
# 3
# >>> s.find("y")
# -1
# >>> txt = "the price is {price:.2f}"
# >>> txt
# 'the price is {price:.2f}'
# >>> txt.format(price=49)
# 'the price is 49.00'
# >>> txt = "the price is {price:.5f}"
# >>> txt.format(price=49)
# 'the price is 49.00000'
# >>> 
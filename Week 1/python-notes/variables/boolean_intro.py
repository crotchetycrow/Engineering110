# Boolean

t = True
f = False

# Booleans from methods

hi = "Hello World!"

print(hi.startswith("Hell"))
a = "HelloWorld"
print(a.isalpha())
l = "hello world!"
print(l.islower())
n = "43110"
print(n.isnumeric())


# Boolean casting

print(int(t), type(int(t)))
print(int(f), type(int(f)))

print(f'0 is treated as {bool(0)}')
print(f'1 is treated as {bool(1)}')
print(f'2 is treated as {bool(2)}')
print(f'-1 is treated as {bool(-1)}')
print(f'1.5 is treated as {bool(1.5)}')
print(f'str is treated as {bool("String")}')
print(f'str 0 is treated as {bool("0")}')

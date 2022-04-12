s1 = "Double quotes"
s2 = 'Single quotes'

print(s1 + s2)
print(f'{s1} {s2}')
print(f'I wrote this in {s1} and this in {s2}')

# String Indexing

s = "Hello World!"

c = s[1]

print(c)

# String Slicing

slices = s[6:9]

print(slices+c)

slices2 = s[:8]
slices3 = s[3:]
slices4 = s[10:1:-1]
reverseSlice = s[::-1]
print(slices2, slices3, slices4)
print(reverseSlice)

print(len(s))

# String Method

print(s.lower(), s.upper())
# print(dir(s))
print(s.replace('e', 'ooo').upper())

a = "here is"
b = "a string"
d = "in parts"

e = f'{a} {b} {d}'

print(e.capitalize())

number = 10
fruits = "apples"

to_print = f'There are {number} {fruits}.'

print(to_print)

# Input
name = input("What is your name?\n")
age = int(input("How old are you?\n"))

print(f'Hello {name}, you are {age} years old', type(age))

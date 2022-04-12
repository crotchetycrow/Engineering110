n = 0
#
# while n < 101:
#     if n % 3 == 0 and n % 5 != 0:
#         print("fizz")
#     elif n % 5 == 0 and n % 3 != 0:
#         print("buzz")
#     elif n % 3 == 0 and n % 5 == 0:
#         print("fizzbuzz")
#     else:
#         print(n)
#     n += 1

# print(["FizzBuzz" if (num % 5 == 0 and num % 3 == 0) else "Fizz" if (num % 3 == 0) else "Buzz" if (num % 5 == 0) else num for num in range(1,101)])

[print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i) for i in range(1, 100)]

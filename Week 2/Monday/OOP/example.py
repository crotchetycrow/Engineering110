user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and 117 > int(age) > 0 and int(age[0]) != 0:
        if int(age) == 69:
            print("Nice.")
        user_prompt = False
    else:
        print("Incorrect input. Please provide an accurate age between 1 and 117. Do not include letters or "
              "begin your input with a 0")

print(f"Your age is {age}")

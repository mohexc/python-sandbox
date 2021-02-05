# # COMPARISON OPERATOR

# # CONDITIONAL OPERATOR

# temperature = 35
# if temperature > 30:
#     print("It 's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It 's nice")
# else:
#     print("It 's cold")
# print("Done")

# #TERNARY OPERATOR

# age = 22
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# # LOGICAL OPERATOR

# height_income = False
# good_credit = True
# student = False
# # if height_income and good_credit:
# # if height_income or good_credit:
# if not student:
#     print("Eligible")
# else:
#     print("Not eligible")

# # SHORT CIRCUIT
# height_income = True
# good_credit = True
# student = True

# if height_income and good_credit and not student:
#     print("Eligible")

# # CHANINING COMPARISON
# age = 22

# if age  19 >= age < 65:
#     print("Eligible")

# ? FOR LOOP
# for number in range(3):
#     print("Attempt", number + 1, (number+1) * ".")

# for number in range(1, 4):
#     print("Attempt", number, number * ".")

# for number in range(1, 10, 2):  #start end step
#     print("Attempt", number, number * ".")

# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...

# ? FOR ELSE
# successful = False
# for number in range(3):
#     print("Attempt", number + 1)
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 time and failed")


# ? NENSTED LOOPS
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)
# (3, 0)
# (3, 1)
# (3, 2)
# (4, 0)
# (4, 1)
# (4, 2)

# ? ITERABLES

# ? WHILE LOOPS
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


# ? INFINITE LOOPS

cmd = ""
while True:
    command = input(">")
    print("ECHO", cmd)
    if command.lower() == "quit":
        break

# quiz

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even number")

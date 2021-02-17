from timeit import timeit
from os import times

# ? exception

# ? Handling Exception


try:
    age = int(input('Age:'))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("Execution continues.")

# ? Handling Different Exceptions
try:
    age = int(input('Age:'))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print('Age cannot be 0.')
else:
    print("Execution continues.")

try:
    age = int(input('Age:'))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("Execution continues.")

# ? Cleaning Up
try:
    file = open("app.py")
    age = int(input('Age:'))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("Execution continues.")
finally:
    file.close()

# ? The with statement
try:
    with open("app.py") as file, open("another.txt") as traget:
        print("File opend")
    age = int(input('Age:'))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("Execution continues.")

# ? Raising Exception


def calculate_xfactore(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactore(-1)
except ValueError as error:
    print(error)

# ? Cost of Raising Exceptions

code1 = """
def calculate_xfactor(age) : 
    if age <=0:
        raise ValueError("Age cannot be 0 or less")
    return 10/ age

try: 
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
code2 = """
def calculate_xfactor(age) : 
    if age <=0:
        raise ValueError("Age cannot be 0 or less")
    return 10/ age

xfactor = calculate_xfactor(-1)
if xfactor = None: 
    pass
"""

print("first code =", timeit(code1, number=10000))
print("second code =", timeit(code2, number=10000))

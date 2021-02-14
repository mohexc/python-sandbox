# ? DEFINING
def greet():
    print("Hi there")
    print("Welcome aboard")


greet()

# ? ARGUMENTS


def greet2(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet2("Mosh", "Hamadani")

# ?  TYPES OF FUNCTIONS

# ? KEYWORD ARGUMENTS

# ? DEFAULT ARGUMENTS


def increment(number, by=1):
    return number + by


print(increment(2))

# ? XARGS


def multipy(*numbers):
    print(numbers)


multipy(2, 3, 4, 5)

# ? XXARGS


def save_user(**user):
    print(user)


save_user(id=1, name="john", age=22)

# ? SCOPE
message = "a"


def greet3(name):
    global message
    message = "b"


greet3("Mosh")
print(message)

# ? DEBUGGING

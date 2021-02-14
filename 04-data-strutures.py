# ? LIST
letters = ['a', 'b', 'c', 'd']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")

# ? ACCESSING ITEM
letters[0] = "A"
print(letters[0])
print(letters[0:3])
print(numbers[::2])
print(numbers[::-1])

# ? LIST UNPACKING
numbers = [1, 2, 3]
first, second, third = numbers

numbers2 = [1, 2, 3, 4, 5]
first1, *other, last = numbers2
# fist1 = 1
# other = [2,3,4]
# last = 5

# ? LOOPING OVER LIST
for index, letter in enumerate(letters):
    print(index, letters)

# ? ADDING OR REMOVING ITEM
# adding
letters.append('d')
letters.insert(0, "-")
# remove
letters.pop()
letters.pop(0)
letters.remove('b')

# ? FINDING ITEMS
letter.index('a')

# ? LAMBDA FUNCTION
#   def sort_item(item) :
#       return item[1]

#  item.sort(key=lambda item: item[1])
#  print(items)

# ? MAP FUNCTION
items = [
    ("Product1", 10),
    ("Product2", 11),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))
print(prices)

# ? FILTER FUNCTION
filtered = list(filter(lambda item: item[1] >= 10, items))

# ? LIST COMPREHENSIONS
filtered = [item for item in items if item[1] >= 10]
prices = [item[1] for item in items]

# ? ZIP FUNCTION
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))

# ? QUEUES


# ? TUPLES
point = (1, 2)
point = 1,
point = ()
point = (1, 2) * 3  # --> (1, 2, 1, 2, 1, 2)
point = tuple("Programming ")

# ? SWAPPING VARIABLE

# ? ARRAY

# ? SETS
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 5}
print(first | second)  # {1,2,3,4,5}
print(first & second)  # {1}
print(first - second)  # {2,3,4}
print(first ^ second)  # {2, 3, 4, 5}
#  uniques = [1,2,3,4]

# ? DICTIONARIES
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point.get('a'))  # --> none
del point['x']
for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)

# ? Dictionary Comprehensions

# ? GENERATOR EXPRESSIONS

# ? UNPACKING OPERATOR
values = list(range(5))
value = [*(range(5), *"Hello")]

dic1 = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}

# list = [1,2,3,4],
# tuple(immutable list) = ('physics, 'chemistry', 10007, 2000),
# sets,
# dictionary = {
#   'car': 'honda',
#  'money': 12345
# }

# slice, index, count, remove, pop, reverse, append

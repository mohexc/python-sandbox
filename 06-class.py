#   ? CLASSES
#   Class: blueprint for creating new objects
#   Object: instance of a class

#   Class: Human
#   Objects: John, Mary, Jack

#   ? CREATING CLASSES
# class Point:
#     def draw(self):
#         print('draw')


# point = Point()

# point.draw()

#   ? CONSTRUCTORS
# class Point:
#     def __init__(self, x, y): consstructor
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point {self.x}, {self.y}")


# point = Point(1, 2)

# point.draw()

#   ? CLASS VS INSTANCE ATTRIBUTES
# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point {self.x}, {self.y} {self.default_color}")


# Point.default_color = "yellow"


#   ? CLASS VS INSTANCE Methods
# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point {self.x}, {self.y} {self.default_color}")


# Point.default_color = "yellow"
# point = Point(1, 2)
# pointAnother = Point(4, 5)
# point.draw()
# pointAnother.draw()


#   ? magic method

#   ? compring object

#   ? performing arithmetic operations

#   ? MAKING CUSTOM CONTAINERS

#   ? MAKING CUSTOM CONTAINERS

#   ? PRIVATE MEMBERS

#   ? PROPERTIES
# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         self.tags[tag] = self.tags.get(tag, 0) + 1


# cloud = TagCloud()
# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)

#   ? 12. INHERITANCES
# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print('eat')


# class Mamal(Animal):
#     def walk(self):
#         print('walk')


# class Fish(Animal):
#     def swim(self):
#         print('swim')


# m = Mamal()
# m.eat()
# print(m.age)

#  ? 13. THE OBJECT CLASS

#   ? 14. METHOD OVERRIDING

#   ? 15. MULTI LEVEL INHERITANCE

#   ? 16. MULTIPLE INHERITANCE

#   ? 17. A GOOD EXAPLE OF INHERITANCE
# class InvalidOperationError(Exception):
#     pass


# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open")
#         self.opened = True

#     def close(self):
#         if not self.open:
#             raise InvalidOperationError("Stream is already close")


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):

#   ? 18. ABSTRACT BASE CLASS

#   ? 19. POLYMORPHISM

#   ? 20. DUCK TYPING

#   ? EXTENDING BUILT-IN TYPES

#   ? DATA CLASSES

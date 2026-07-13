# class Myclass:
#     x = 5


# p1 = Myclass()
# print(p1.x)

# del p1

# print(p1.x)


# class Person:
#     pass

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("saba", 36)

# print(p1.name)
# print(p1.age)

# class Person:
#     pass


# p1 = Person()
# p1.name = "saba"
# p1.age = 25

# print(p1.name)
# print(p1.age)


# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age


# p1 = Person("saba")
# p2 = Person("saba", 35)
# print(p1.name, p1.age)
# print(p2.name, p2.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"hello my name is {self.name}, i am {self.age} years old")


# p1 = Person("saba", 23)
# p1.greet()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def printname(self):
#         print(f"hello my name is {self.name}")


# p1 = Person("saba")
# p2 = Person("giorgi")

# p1.printname()
# p2.printname()

# class Person:
#     def __init__(myobject, name, age):
#         myobject.name = name
#         myobject.age = age
#         print(name)

#     def greet(abc):
#         print("hello", abc.name)


# p1 = Person("Emil", 36)
# p1.greet()


class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "hello, " + self.name

    def welcome(self):
        print(self.greet() + "welcome")


p1 = Person("saba")
p1.welcome()

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


# class Person():
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return "hello, " + self.name

#     def welcome(self):
#         print(self.greet() + "welcome")


# p1 = Person("saba")
# p1.welcome()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def printname(self):
#         print(self.name)


# p1 = Person("saba")

# p1.printname()


# class Person:
#     def __init__(myobject, name, age):
#         myobject.name = name
#         myobject.age = age

#     def greet(abc):
#         print(f"hello my name is {abc.name}")


# p1 = Person("saba", 22)
# p1.greet()


# class Car:
#     def __init__(self, brand, model, year):
#         self.rame = brand
#         self.mode = model
#         self.yea = year

#     def display_info(cc):
#         print(f"{cc.rame} {cc.mode} {cc.yea}")


# car1 = Car("honda", "fit", 2003)
# car1.display_info()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"hello {self.name}"

#     def welcome(self):
#         message = self.greet()
#         print(f"{message}! welcome to our website")


# p1 = Person("saba")
# p1.welcome()


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model


# car1 = Car("honda", "fit")
# print(car1.brand)
# print(car1.model)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("saba", 22)

# p1.age = 34

# print(p1.age)

# del p1.age
# # print(p1.age)
# print(p1.name)

# class Person:
#     species = "Human"

#     def __init__(self, name):
#         self.name = name


# p1 = Person("saba")
# p2 = Person("giorgi")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)


# class Person:
#     lastname = ""

#     def __init__(self, name):
#         self.name = name


# p1 = Person("saba")
# p2 = Person("lasha")

# Person.lastname = "okropiridze"

# print(p1.lastname)
# print(p2.lastname)


# class Person:
#     def __init__(self, name):
#         self.name = name


# p1 = Person("saba")

# p1.age = 25
# p1.city = "tbilisi"

# print(p1.city)
# print(p1.age)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")


# p1 = Person("saba")
# p1.greet()

# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def multiply(self, a, b):
#         return a * b


# calc = Calculator()

# print(calc.add(1, 4))
# print(calc.multiply(1, 4))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"


p1 = Person("saba", 23)

print(p1.get_info())

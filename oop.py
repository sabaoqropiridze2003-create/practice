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

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_info(self):
#         return f"{self.name} is {self.age} years old"


# p1 = Person("saba", 23)

# print(p1.get_info())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def celebrate_birthday(self):
#         self.age += 1
#         print(f"happy birthday! you are now {self.age}")


# p1 = Person("saba", 22)
# p1.celebrate_birthday()
# p1.celebrate_birthday()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("saba", 45)
# print(p1)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} ({self.age})"


# p1 = Person("lana", 45)
# print(p1)


# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)
#         print(f"Added: {song}")

#     def remove_song(self, song):
#         if song in self.songs:
#             self.songs.remove(song)
#             print(f"removed: {song}")

#     def show_songs(self):
#         print(f"Playlist: {self.name}")
#         for song in self.songs:
#             print(f"- {song}")


# my_playlist = Playlist("eminem")
# my_playlist.add_song("rap god")
# my_playlist.add_song("godzila")
# my_playlist.show_songs()
# my_playlist.remove_song("rap god")
# my_playlist.show_songs()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("hello")


# p1 = Person("emily")

# del Person.greet

# p1.greet()


##########################################################
########### inheritance####################################

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def printname(self):
#         print(self.fname, self.lname)


# class Student(Person):
#     pass


# x = Person("alexa", "shanava")
# x.printname()

# y = Student("saba", "kvaratskhelia")
# y.printname()


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

#     def mult(self):
#         print(self.firstname * 2)


# x = Student("Mike", "Olsen")
# x.printname()
# x.mult()


# class Person():
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)


# x = Student("Mike", "Olsen")
# x.printname()

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.graduationyear = 2025


# x = Student("saba", "okropiridze")
# print(x.graduationyear)


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year


# x = Student("lasa", "kankava", 2024)
# print(x.graduationyear)


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

#     def welcome(self):
#         print(
#             f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")


# x = Student("saba", "axalaia", 2021)
# x.welcome()

####################### polimorphism#########################


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Drive")


# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Sail")


# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Fly!")


# car1 = Car("ford", "mustang")
# boat1 = Boat("ibiza", "touring 20")
# plane1 = Plane("boeing", "747")

# for x in (car1, boat1, plane1):
#     x.move()


# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Move!!")


# class Car(Vehicle):
#     pass


# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")


# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")


# car1 = Car("ford", "mustang")
# boat1 = Boat("ibiza", "touring 20")
# plane1 = Plane("boeing", "747")

# for x in (car1, boat1, plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()

# def my_function(*kids):
#     print(f"the youngest child is {kids[2]}")


# my_function("elene", "saba", "giorgi")


# def my_function(*args):
#     print(f"Type {type(args)}")
#     print(f"First argument {args[0]}")
#     print(f"Last argument {args[-1]}")


# my_function("elene", "saba", "giorgi")

# def func(*args):
#     print(args)


# func(1, 2, 3, 4, 5, 6)


# def my_function(greeting, *names):
#     for n in names:
#         print(greeting, n)


# my_function("Hello", "Emil", "Tobias", "Linus")


# def my_function(*numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     print(total)


# my_function(1, 2, 3, 4, 5)


# def my_function(*numbers):
#     if len(numbers) == 0:
#         return None
#     max_num = 0
#     for n in numbers:
#         if n > max_num:
#             max_num = n
#     return (max_num)


# print(my_function(-1, 14, 45, -5, 3, 4, 5, 6))


# def my_function(**person):
#     print(f"{person["fname"]} {person["lname"]} is {person["age"]} years old")
#     print(person)


# my_function(fname="saba", lname="okropiridze", age=24)

# def my_function(username, **details):
#     print(f"username: {username}")
#     print("aditional info")
#     for key, value in details.items():
#         print(f"{key} : {value}")


# my_function("emil123", age=25, city="Oslo", hobby="coding")

# def my_function(title, *args, **kwargs):
#     print("Title:", title)
#     print("Positional arguments", args)
#     print("keyword arguments", kwargs)


# my_function("User Info", "Emil", "Tobias", age=25, city="Oslo")


# def my_function(a, b, c):
#     return a + b + c


# numbers = (1, 2, 3)
# numbers = [1, 2, 3]
# result = my_function(*numbers)
# print(result)

def my_function(fname, lname):
    print("hello", fname, lname)


person = {"fname": "saba", "lname": "okropiridze"}
my_function(**person)

# thisislist = ["apple", "banana", "cherry"]
# print(thisislist)

# lst = ["apple", "banana", "apple"]
# print(lst)
# print(len(lst))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 2, 3, 4, 5]
# list3 = [True, False, False]
# print(list3)

# list1 = ["abc", 34, 2.1, True, None,]
# print(type(list1))

# list1 = list(("abc", 34, 2.1, True, None,))
# print(list1)


# list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(list1[1])
# print(list1[-1])
# print(list1[1:5])
# print(list1[:3])
# print(list1[4:])
# print(list1[-4: -1])
# print(list1[::-1])


# thislist = ["apple", "banana", "cherry"]

# if "apple" in thislist:
#     print("apple is in teh list")

# list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# list1[4] = "mango"
# print(list1)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["watermelon", "mango"]
# print(thislist)

# thislist[1:3] = ["banana"]
# print(thislist)


# thislist.insert(2, "watermelon")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]

# thislist.append("orange")

# thislist.insert(1, "mango")

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical)
# thislist.extend(["apple", "watermelon"])

# thistuple = ("kiwi", "banana")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# print(thislist.pop(0))
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[1]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for i in thislist:
#     print(i)


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])


# thislist = ["apple", "banana", "cherry"]

# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1

# thislist = ["apple", "banana", "cherry"]
# [print(i) for i in thislist]


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for i in fruits:
#     if "a" in i:
#         newlist.append(i)
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [i for i in fruits if "a" in i]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [i for i in fruits if i != "apple"]
# print(newlist)


# newlist = [i for i in range(10) if i % 2 == 0]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [i.upper() for i in fruits]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [i if i != "banana" else "orange" for i in fruits]
# print(newlist)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# thislist.sort(reverse=True)
# print(thislist)

# def myfunc(n):
#     return abs(n - 50)


# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key=myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist.sort(key=str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# newlist = thislist.copy()
# print(newlist)


# thislist = ["apple", "banana", "cherry"]
# newlist = list(thislist)
# print(newlist)


# thislist = ["apple", "banana", "cherry"]
# newlist = thislist[:]
# print(newlist)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# for i in list2:
#     list1.append(i)

# print(list1)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# print(fruits.count("apple"))


###### challenge######

# Create a list

# Print the first item

# Change the second item to "yellow"

# Add "purple" to the end

# Remove "red"

# Print the list

# color = ["red", "green", "blue"]
# print(color[0])
# color[1] = "yellow"
# print(color)
# color.append("puple")
# print(color)
# color.remove("red")
# print(color)

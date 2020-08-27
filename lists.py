# names = ['john', 'brian', 'steve', 'sarah']
# names[2] = 'ron'
# print(names[0:4])

# numbers = [3, 6, 8, 10, 20]
# max = numbers[0]
# for number in  numbers:
#     if number > max:
#         max = number
# print(max)

# program to find the oldest child

# ages = [4, 6, 7, 5, 3, 9]
# oldest = ages[0]
# for age in ages:
#     if age > oldest:
#         oldest = age
# print(oldest)

# ************************************************************
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # print(matrix[1][2])
#
# for row in matrix:
#     for item in row:
#         print(item)

# **************************************************************

# numbers = [5, 2, 1, 7, 4]
# numbers2 = numbers.copy()
# numbers.append(20)
# numbers.insert(0, 4)
# numbers.remove(1)
# numbers.pop()
# print(1 in numbers)
# numbers.clear()

# print(numbers2)

# **************************

# write a program that removes the duplicates in a list

# list = [3, 5, 6, 5, 7, 9, 7]
# list_two = []
# for item in list:
#     if item not in list_two:
#         list_two.append(item)
# print(list_two)


# grocery_list = ['apple', 'lettuce', 'tomato', 'apple', 'tomato', 'rice', 'beans']
# uniques_list = []
# for food in grocery_list:
#     if food not in uniques_list:
#         uniques_list.append(food)
# print(uniques_list)

# ***************************
# tuples cant be modified, they are immutable
# numbers = (1, 2, 3, 4)
# # numbers[0] = 10
# print(numbers)

# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(z)

#******************************
# dictionaries
# customer = {
#     "name": "John Doe",
#     "age": 30,
#     "is_verified": True
# }
# customer["birth_date"] = "Jan 1 1980"
# print(customer["birth_date"])

# *******************************

# program that asks for phone number and then translates to

# phone = input("Phone number: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)


# program that turns characters into emojis

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😔",
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)


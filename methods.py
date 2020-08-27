# add to the list

first_list = [1, 2, 3, 4]
first_list.append(5)
print(first_list)

# extend
correct_list = [1, 2, 3, 4]
correct_list.extend([5, 6, 7, 8])
print(correct_list)


second_list = [10, 20, 30, 40, 50]
second_list.insert(-1, "hello world!")
print(second_list)


foods = []
# foods.append('bacon')
# foods.append('eggs')
# foods.append('toast')
foods.extend(['bacon', 'eggs', 'toast'])
print(foods)


# ############################################
# clear
third_list = [1, 2, 3, 4]
third_list.clear()
print(third_list)

# pop
fourth_list = [1, 2, 3, 4]
fourth_list.pop(0)
print(fourth_list)


shopping_list = ['eggs', 'milk', 'flour', 'rice', 'beans']
print(shopping_list)
shopping_list.pop(3)
print(shopping_list)
shopping_list.remove('flour')
print(shopping_list)

# count

swear_words = ['fuck', 'shit', 'ass', 'asshole',
               'fuck', 'bastard', 'bitch', 'nigger']
print(swear_words.count('nigger'))
swear_words.pop(7)
print(swear_words)
swear_words.remove('fuck')
print(swear_words)


#

places = []
places.extend(['Toronto', 'New York', 'Los Angeles', 'Sao Paulo', 'London'])
print(places)
places.pop()
print(places)
places.pop(0)
print(places)
places.insert(0, 'Done')
print(places)

# #####################################################################
# slicing

random_list = [1, 2, 3, 'bacon', 'John', 5, 7, 9, 'blue']
print(random_list)
print(random_list[-3:])
print(random_list[:4])
print(random_list[::-1])

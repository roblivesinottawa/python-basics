# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
# print('Done!')

# secret_number = 9
# chances = 0
# limit = 3
#
# while chances < limit:
#     guess = int(input('Guess: '))
#     chances += 1
#     if guess == secret_number:
#         print('you won!')
#         break
# else:
#     print('sorry you failed')

# age = 34
# guess_age = 0
# guess_age_limit = 3
#
# while guess_age < guess_age_limit:
#     guess = int(input('Guess: '))
#     guess_age += 1
#     if guess == age:
#         print('You are right')
#         break
# else:
#     print('you are wrong')

# command = ""
# started = False
#
#
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop  the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry I don't get that")




#***********************************************************

# for item in ["Python", "Javascript", "C+"]:
#     print(item)

# for item in range(10):
#     print(item)

# prices = [20, 40, 100]
#
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

# nested loops

# for x in range(4):
#     for y in range(3):
#         print(f" ({x}, {y})")

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     print('x' * x_count)


# numbers = [2, 2, 2, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)


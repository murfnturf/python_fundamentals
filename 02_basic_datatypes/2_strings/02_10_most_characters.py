'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
user_input_one = input("Type a word here: ")
user_input_two = input("Type a word here: ")
user_input_three = input("Type a word here: ")

input_one_len = len(user_input_one)
print(input_one_len)
print(user_input_one)

input_two_len = len(user_input_two)
print(input_two_len)
print(user_input_two)

input_three_len = len(user_input_three)
print(input_three_len)
print(user_input_three)

print("The largest word is: ")

if input_three_len > input_two_len and input_three_len > input_one_len:
    print(user_input_three)

if input_two_len > input_three_len and input_two_len > input_one_len:
    print(user_input_two)

if input_one_len > input_three_len and input_one_len > input_two_len:
    print(user_input_one)





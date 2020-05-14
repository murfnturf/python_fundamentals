'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

prompt = input("Write a paragraph about your summer holiday: ")

user_input = prompt.split()

print(user_input)

x = max(user_input, key = user_input.count)

print(x)







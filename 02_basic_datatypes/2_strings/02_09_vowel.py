'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

user_input = input("Type a string here: ")

#if "a" in user_input:
print(user_input.count("a"))
#if "e" in user_input:
print(user_input.count("e"))
#if "i" in user_input:
print(user_input.count("i"))
#if "o" in user_input:
print(user_input.count("o"))# "u" in user_input:
print(user_input.count("u"))



total = (user_input.count("a") + user_input.count("e") + user_input.count("i") + user_input.count("o") + user_input.count("u"))
print(total)
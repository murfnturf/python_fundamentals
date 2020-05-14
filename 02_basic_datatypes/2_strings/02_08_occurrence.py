'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

user_words = input("Type 5 different words: ")


user_letter = input("Type a letter which exists in one of those words: ")


result = user_words.find(user_letter)

print(result)




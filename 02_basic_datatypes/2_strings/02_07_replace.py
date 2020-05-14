'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

user_string = str(input("Type a string of several words in length: "))
print(f"{user_string}")

user_symbol = input("Please choose one symbol: ")
print(f"{user_symbol}")

modified_str = user_string.replace(user_string[0], user_symbol)
print(modified_str)

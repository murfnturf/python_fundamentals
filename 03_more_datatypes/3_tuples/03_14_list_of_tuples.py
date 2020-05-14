'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

words = []

prompt = input("Please say hello to your new computer: ")


words = prompt.split()



print(words)


for i in words:
    print(tuple(i))



new_list = []

for i in words:
    new_list.append(tuple(i))

print(new_list)









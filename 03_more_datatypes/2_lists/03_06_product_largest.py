'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

user_list = []

n = int(input("Enter ten different numbers: "))

for i in range(0, n):
    numb = int(input())

    user_list.append(numb)

max_numb = max(user_list)

print(user_list)
print(max_numb)
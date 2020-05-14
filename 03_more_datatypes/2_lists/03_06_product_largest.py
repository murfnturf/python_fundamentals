'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''


numbers = input("Enter ten different numbers: ")
new_numbers = numbers.split()

max_number = max(new_numbers)

print(numbers)

print(new_numbers)

new_list = []

for i in new_numbers:
    x = int(i)
    new_list.append(x)
    #print(x)

if len(new_list) != 10:
    print ("You haven't entered exactly ten numbers: ")
    #new_prompt = input("Add another number: ")
    #print(new_prompt)


print(new_list)


print(max_number)
max_number1 = max(new_list)
print(max_number1)


'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

user_list = []

user_values = input("Type in 10 numbers: ")
print(user_values)

x = user_values.split()
print(x)

new_list = []

for i in x:
    z = int(i)
    new_list.append(z)
    #print(z)

print(new_list[1])
print(new_list[3])
print(new_list[5])
print(new_list[7])
print(new_list[9])
print(new_list[8])
print(new_list[6])
print(new_list[4])
print(new_list[2])
print(new_list[0])


normal = (new_list[1::2])
r1 = (new_list[-2::-2])



# 44 - 46 is same code as 39

r = (new_list[0::2])
r.reverse()
print(r)

print(normal + r)
print(normal + r1)


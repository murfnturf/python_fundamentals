'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
a = (input("Please enter the temperature in celsius: "))

celsius = float(a)

fahrenheit = (celsius * 1.8) + 32

print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
#
# fahrenheit = 47
# celsius = (fahrenheit - 32) / 1.8
#
# print('%0.1f degree Fahrenheit is equal to %0.1f degree Celsius' %(fahrenheit,celsius))





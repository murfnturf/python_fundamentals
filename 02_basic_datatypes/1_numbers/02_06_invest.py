'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment_a = float(input("Enter an investment amount: "))


interest_rate = float(input("Enter your interest rate: "))


number_of_years = int(input("Enter the number of years for the investment: "))

future_value = investment_a * interest_rate * number_of_years

print(future_value)
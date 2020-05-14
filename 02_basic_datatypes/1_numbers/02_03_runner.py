'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
one_kilometer = 1.6
one_mile = 0.62

total_kilometers = one_mile*10

print(total_kilometers)

total_seconds = 30*60+30

print(total_seconds)

total_hours = (total_seconds / 60) / 60

answer = (total_kilometers / (total_hours))

print(answer)
print(round(answer,2))
print(format(answer,'.2f'))


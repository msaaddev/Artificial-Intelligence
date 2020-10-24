"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""


def calculateFibSeries(num):
    fibSeries = [0, 1]
    temp = [*range(2, num + 1, 1)]
    map(lambda _: fibSeries.append(sum(fibSeries[-2:])), temp)
    return fibSeries


num = input("Enter a number: ")
intNum = int(num)

print(calculateFibSeries(intNum))

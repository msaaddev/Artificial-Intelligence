"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def common(a, b):
    c = set(a) & set(b)
    temp = list(c)
    return temp


print(common(a, b))

# 3.1

list1 = []
list2 = []

for i in range(0, 10):
    list1.append(randint(0, 30))

for i in range(0, 15):
    list2.append(randint(0, 30))

print('\nExtra 3.1', common(list1, list2))

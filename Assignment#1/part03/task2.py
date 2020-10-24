"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

# 2

num = input("\nEnter a number: ")
originalNum = int(num)
counter = int(num) + 1

list = []
for i in range(1, counter):
    if(originalNum % i == 0):
        list.append(i)

print(list)

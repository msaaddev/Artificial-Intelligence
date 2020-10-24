"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

# 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in range(0, len(a)):
    if(a[i] < 5):
        print(a[i])

# 1.1

print('\n')
newList = []
for i in range(0, len(a)):
    if(a[i] < 5):
        newList.append(a[i])

print('\nExtra 1.1: ', newList)

# 1.2

print('\nExtra 1.2: ', list(a[i] for i in range(0, len(a)) if a[i] < 5))

# 1.3

num = input("\nExtra 1.3: Enter a number: ")
intNum = int(num)

print(list(a[i] for i in range(0, len(a)) if a[i] < intNum))

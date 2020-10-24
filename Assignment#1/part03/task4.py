"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

# 4.1

userInput = input("\nEnter any string: ")

if userInput[::-1] == userInput[0:]:
    print ("It is a palindrome")
else:
    print ("It is not a palindrome")


# 4.2

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print ('\n', [i for i in a if i % 2 == 0])

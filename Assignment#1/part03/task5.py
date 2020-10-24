"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

userInput = input("\nEnter any sentence: ")

words = userInput.split()
totalWords = len(words)

for i in reversed(range(0, totalWords)):
    print(words[i], end=" ")

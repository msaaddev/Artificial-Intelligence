"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

from random import randint

# 8.a

listOfWords = ["APPLE", "BILBO", "CHORUSED", "DISIMAGINE", "ENSURING", "FORMALISING", "GLITCHES", "HARMINE", "INDENTATION", "JACKED", "KALPACS",
               "LAUNDRY", "MASKED", "NETTED", "OXFORD", "PARODY", "QUOTIENTS", "RACERS", "SADNESS", "THYREOID", "UNDUE", "VENT", "WEDGED", "XERIC", "YOUTHHOOD", "ZIFFS"]
print("\nRandom Word from list:",
      listOfWords[randint(0, len(listOfWords) - 1)])

# 8.b

randomWord = listOfWords[randint(0, len(listOfWords) - 1)]
wordGuess = ''.join('_' for i in range(len(randomWord)))

while randomWord != wordGuess:
    letter = input("Enter a letter : ")
    letter.lower()
    if letter in randomWord:
        indices = [i for i, s in enumerate(randomWord) if s == letter]
        for i in indices:
            wordGuess = wordGuess[:i] + letter + wordGuess[i + 1:]
        print(wordGuess)
    else:
        print("Incorrected letter. Try again!")
print("Congratulations! You won.")

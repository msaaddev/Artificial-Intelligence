"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

from random import randint

# 8.a

listOfWords = ["APPLE", "BILBO", "CHORUSED", "DISIMAGINE", "ENSURING", "FORMALISING", "GLITCHES", "HARMINE", "INDENTATION", "JACKED", "KALPACS",
               "LAUNDRY", "MASKED", "NETTED", "OXFORD", "PARODY", "QUOTIENTS", "RACERS", "SADNESS", "THYREOID", "UNDUE", "VENT", "WEDGED", "XERIC", "YOUTHHOOD", "ZIFFS"]
print("\n Random Word from list:", listOfWords[randint(0, len(listOfWords) - 1)])

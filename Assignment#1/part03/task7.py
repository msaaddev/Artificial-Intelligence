"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

from random import randint

password = ''
character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*abcdefghijklmnopqrstuvwxyz0123456789'
characterLength = len(character)

for i in range(0, 15):
    index = randint(0, characterLength)
    password += character[index]

print('\nPassword:', password)

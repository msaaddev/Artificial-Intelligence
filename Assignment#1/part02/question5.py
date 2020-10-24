"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

firstList = ['JohnDoe', 'JaneDoe', 'Python', 'JavaScript', 'Flute']

result = list(i.lower() for i in firstList if len(i) > 5)

print(result)

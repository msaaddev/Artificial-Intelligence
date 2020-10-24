"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

newDict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
    "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

uniDict = set(val for dic in newDict for val in dic.values())
print("Unique Values: ", uniDict)

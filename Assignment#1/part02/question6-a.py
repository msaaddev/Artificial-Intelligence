"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

D = {
    '2018-CS-01': [("DSA", 3), ("Algo", 2.5), ('AI', 3)],
    '2018-CS-02': [("LA", 3), ("Algo", 3.5), ('PF', 2.8), ('AI', 2)],
    '2018-CS-03': [("OOP", 3), ("DB", 3.5), ('PF', 2.8), ('DSA', 4)],
    '2018-CS-04': [("OOP", 3), ("DB", 3.5), ('AI', 2.3), ('DSA', 4)],
}

for key in D:
    totalGPAOfSuject = 0.0
    y = len(D[key])
    for i in range(0, y):
        totalGPAOfSuject += (D[key][i][1] * 3)
    gpa = totalGPAOfSuject / (y * 3)
    print('Student with ', key, 'has GPA: ', gpa)

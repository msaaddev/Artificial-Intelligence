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

student = 0

for key in D:
    y = len(D[key])
    for i in range(0, y):
        if(D[key][i][0] == 'AI'):
            if(D[key][i][1] < 2.5):
                student += 1

print('Total students who have less than 2.5 GPA in AI:', student)
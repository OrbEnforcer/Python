quiz = int(input())
exam = int(input())
assign = int(input())
project = int(input())
d = {'Quiz': quiz, 'Exam': exam, 'Assignment': assign, 'Project': project}
if (d['Quiz'] < 0):  
    print('ERROR: Invalid Marks', d['Quiz'],'< 20')
elif (d['Quiz'] > 20):
    print('ERROR: Invalid Marks', d['Quiz'],'> 20')
if (d['Exam'] < 0): 
    print('ERROR: Invalid Marks', d['Exam'],'< 100')
elif (d['Exam'] > 100):
    print('ERROR: Invalid Marks', d['Exam'],'> 100')
if (d['Assignment'] < 0): 
    print('ERROR: Invalid Marks', d['Assignment'],'< 100')
elif (d['Assignment'] > 100):
    print('ERROR: Invalid Marks', d['Assignment'],'> 100')
if (d['Project'] < 0): 
    print('ERROR: Invalid Marks', d['Project'],'< 50')
elif (d['Project'] > 50):
    print('ERROR: Invalid Marks', d['Project'],'> 50')
else:
    print('All marks are valid')
    G = (((quiz/20) * 0.15) * 10) + (((exam/100) * 0.4) * 10) + (((assign/100) * 0.2) * 10) + (((project/50) * 0.25) * 10)
    GPA = round(G,2)
    if (GPA == 10):
        Grade = 'O'
    elif (9 <= GPA < 10):
        Grade = 'A'
    elif (8 <= GPA < 9):
        Grade = 'B'
    elif (6.5 <= GPA < 8):
        Grade = 'C'
    elif (5 <= GPA < 6.5):
        Grade = 'D'
    else:
        Grade = 'F'
    d['GPA'] = GPA
    d['Grade'] = Grade
    print(d)

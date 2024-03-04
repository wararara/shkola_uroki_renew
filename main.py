class Student:
    aidi = 0
    name = ''
    title = ''
    klass = ''
    score = ''


f = open('students.csv', 'r', encoding = 'utf8')
f.readline()
STUD = []
z = 0
for i in f:
    st = Student()
    st.aidi = i.split(',')[0]
    st.name = (i.split(',')[1]).split()
    st.title = i.split(',')[2]
    st.klass = i.split(',')[3]
    st.score = i.split(',')[4]
    STUD.append(st)

def find(STUD, key):
    for i in range (len(STUD)):
        if STUD[i].aidi == key:
            ifamilia = str((STUD[i].name[1])[0] + '. ' + STUD[i].name[0])
            return [STUD[i].title, ifamilia, STUD[i].score]
    return -1

inpat = input()

while inpat != 'СТОП':
    r = find(STUD, inpat)
    if r == -1:
        print('Ничего не найдено')
    else:
        print('Проект № ', r[0], 'делал: ', r[1], 'он(а) получил(а) оценку - ', r[2])

    inpat = input()



class Student:

    aidi = 0
    name = ''
    title = ''
    klass = ''
    score = ''

def vstavit(STUD):
    for i in range (len(STUD)):
        j = i -1
        f = STUD[i]
        while STUD[j].score > f.score and j >= 0:
            STUD[j + 1] = STUD[j]
            j -= 1
        STUD[j + 1] = f

    return STUD

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

vstavit(STUD)

print("10 класс:")

z = 0
for i in range (len(STUD)):
    if '5' in STUD[i].score and '10' in STUD[i].klass:
        if z == 0:
            print('1 место: ', (STUD[i].name[1])[0], '. ', STUD[i].name[0])
        if z == 1:
            print('2 место: ', (STUD[i].name[1])[0], '. ', STUD[i].name[0])
        if z == 2:
            print('3 место: ', (STUD[i].name[1])[0], '. ', STUD[i].name[0])
        if z == 3:
            exit()
        z += 1

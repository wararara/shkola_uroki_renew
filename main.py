import secrets

class Student:

    aidi = 0
    name = ''
    title = ''
    klass = ''
    score = ''
    login = ''
    password = ''

f = open('students.csv', 'r', encoding = 'utf8')
holycow = f.readline().strip()
STUD = []
z = 0
for i in f:
    st = Student()
    st.aidi = i.split(',')[0].strip()
    st.name = (i.split(',')[1]).split()
    st.title = i.split(',')[2]
    st.klass = i.split(',')[3]
    st.score = i.split(',')[4].strip()
    STUD.append(st)

bank = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def disaster(person):
    t = ''
    while (any(chr.isdigit() for chr in t) == False) and (any(chr.islower() for chr in t) == False) and (any(chr.isupper() for chr in t) == False):
        t = ''
        for i in range (8):
            t += secrets.choice(bank)

    return t.strip()

def namemaking(person):
    hi = person.name

    login = str(hi[0]) + '_' + str(hi[1][0]) + str(hi[2][0])
    return login.strip()

for i in range (len(STUD)):
    STUD[i].login = namemaking(STUD[i])
    STUD[i].password = disaster(STUD[i])

out = open('students_password.csv', 'w')
print(holycow, file = out, end = '')
whoa = ',login,password'
print(whoa, file = out)

for i in range (len(STUD)):
    print(STUD[i].aidi,',',STUD[i].name[0] + ' ' + STUD[i].name[1] + ' ' + STUD[i].name[2],',',STUD[i].title,',',STUD[i].klass,',',STUD[i].score,',',STUD[i].login,',',STUD[i].password, file = out, end = '')
    print(file = out)

out.close()
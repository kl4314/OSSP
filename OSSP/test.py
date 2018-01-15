import csv
from .models import School

line = []
line1 = []

f = open('학교정보.csv', 'r')
#f1 = open('장애인편의.csv', 'r')
rdr = csv.reader(f)
#rdr1 = csv.reader(f1)


for row in rdr:
   line.append(row)

#for row in rdr1:
   #line1.append(row)

for lines in line:
    school = School(
        code = lines[0],
        address = lines[17],
        daddress = lines[18],
        pnum = lines[21],
        haddress = lines[23],
        sex = lines[24],
    )
    school.save()
    print(School.objects.get(code = 'S010000749' ).values('address'))

import pandas as pd

import pymysql as py


connection = py.connect(host = 'localhost', db = 'pandasdb', user = 'raghu', password = '1234')

sql = 'select * from studentdata;'

c = connection.cursor()

c.execute(sql)

data=c.fetchall()

names=[]

marks=[]

location=[]

school=[]

for i in data:
    names.append(i[0])
    marks.append(i[1])
    location.append(i[2])
    school.append(i[3])

students={
    
    'snames':names,
    'smarks':marks,
    'loc':location,
    'school':school
    }


indexing=range(1,len(names)+1)

student_details=pd.DataFrame(students,index=indexing)


print(student_details[student_details['snames']=='DHONI'])









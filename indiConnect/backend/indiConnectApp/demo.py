import pymysql

con = pymysql.connect(host='localhost', user='root', password='root', db='indiConnect')
cur = con.cursor()

q1 = "select user_name from indiconnectapp_users"
cur.execute(q1)
ls1 = []
query1 = cur.fetchall()
for p in query1:
    ls1.append(p[0])

q2 = "select pass_word from indiconnectapp_users"
cur.execute(q2)
ls2 = []
query2 = cur.fetchall()
for  q in query2:      
    ls2.append(q[0])

print(ls1)
print(ls2)

q3 = "SELECT id FROM indiconnectapp_users ORDER BY id DESC LIMIT 1"
cur.execute(q3)
query3 = cur.fetchall()

for r in query3:
    last_id = r[0]
print(last_id, type(last_id))
final_agent_code = 'INDC' + str(last_id)
print(final_agent_code,type(final_agent_code))
if 'Suresh' in ls1 and 'Kolekar' in ls2:
    print('username and password is present')
else:
    print('username or password is wrong')


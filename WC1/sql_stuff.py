import numpy as np
import sqlite3 as lite 

data = lite.connect('DDM17.db')


# COMPLETING THE LECTRUE

Q4 = '''
select o.WhereStored
from
	STARS as s
	JOIN OBSERVATIONS as o
	ON s.fieldID = o.ID
Where Star = 'S5'
'''

Q5 = '''
select Star
FROM STARS
WHERE FieldID = 1
'''

info = data.execute("PRAGMA table_info('OBSERVATIONS')")

Q4 = data.execute(Q4)
Q5 = data.execute(Q5)



for row in Q4:
	print(row)
print('---')
for row in Q5:
	print(row)
	
	

# CREATING SIMPLE TABLES
print('-------------------------------------------')
a = '''
select Ra, Dec
FROM MAGTABLE
WHERE B > 16
'''
b = '''
select B, R, T_eff, FeH
from
	MAGTABLE as m
	JOIN PHYSTABLE as p
	ON m.Name = p.Name
'''

c = '''
select B, R, T_eff, FeH
from
	MAGTABLE as m
	JOIN PHYSTABLE as p
	ON m.Name = p.Name
WHERE FeH > 0
'''

d = '''
select B-R as br
from MAGTABLE
'''

d = '''
CREATE TABLE IF NOT EXISTS DiffTable (Name varchar(10), BR FLOAT,)
'''

a = data.execute(a)
b = data.execute(b)
c = data.execute(c)


for r in a:
	print(r)
print('---')
for r in b:
	print(r)
print('---')
for r in c:
	print(r)
print('---')

d = '''
CREATE TABLE IF NOT EXISTS DiffTable (Name varchar(10), BR FLOAT)
'''
d2 = '''
select Name, B, R
from MAGTABLE
'''
d = data.execute(d)
d2 = data.execute(d2)

for r in d2:
	q = "INSERT INTO DiffTable (Name, BR) VALUES ('{N}', {BR})".format(N=str(r[0]), BR = r[1]-r[2])
	print(q)
	data.execute(q)
	
d = '''
select *
from DiffTable
'''

d = data.execute(d)
for r in d:
	print(r)

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

curs.execute('CREATE TABLE demo(s TEXT,x INT,y INT);').fetchall()
curs.execute("""
                INSERT INTO demo(s,x,y)
                VALUES ('g',3,9), ('v', 5, 7), ('f',8,7)
""").fetchall()

conn.commit()
x = curs.execute('SELECT COUNT(*) FROM demo').fetchall()
y = curs.execute('SELECT COUNT(*) FROM demo WHERE x>=5 AND y>=5;').fetchall()
z = curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall()
curs.close()
conn.commit()
print('Rows: ', x)
print('Rows where both x and y are greater than 5: ', y)
print('Unique values of y: ', z)
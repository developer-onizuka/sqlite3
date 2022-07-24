import sqlite3 

CREATE_TABLE='''CREATE TABLE employees
(employeeid INTEGER PRIMARY KEY AUTOINCREMENT,
firstname TEXT,
lastname TEXT)'''

TEST_INSERT='''INSERT INTO employees (employeeid, firstname, lastname)
VALUES('0001', 'Yukichi', 'Fukuzawa') '''

TEST_SELECT="SELECT * FROM employees"

conn = sqlite3.connect('employees.sqlite3')
c = conn.cursor()

c.execute(CREATE_TABLE)
c.execute(TEST_INSERT)

conn.commit
c.execute(TEST_SELECT)
result = c.fetchone()
c.execute(TEST_SELECT)

print(result)

conn.close()


import mysql.connector as m1
conn = m1.connect(
    host = 'localhost',
    user = 'root',
    password = 'accessme',
    database = 'db_python_Class'
)

def MyExecute (SQL):
    cur = conn.cursor()
    cur.execute(SQL)
    conn.commit()
    cur.close()

def MyRead (SQL):
    cur = conn.cursor()
    cur.execute(SQL)
    DT = cur.fetchall()
    cur.close()
    return (DT)

def MyClose():
    conn.close()

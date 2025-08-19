import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute('''delete from users where phone="9067821135" ''')
conn.commit()
conn.close()
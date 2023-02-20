import sqlite3
db = sqlite3.connect('data.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link TEXT,
    label TEXT,
    model TEXT)
    """)
db.commit()

db = sqlite3.connect('data.db')
sql = db.cursor()
rows = sql.execute(f"""SELECT * FROM data""").fetchall()
with open('output_db.txt', 'w') as f:
    for i in rows:
        f.write(str(i)+'\n')
        print(i)

#sql.execute('''DROP TABLE data''')
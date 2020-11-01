import sqlite3

with sqlite3.connect("aloy.db") as db:
    curser = db.cursor()


curser.execute('''
CREATE TABLE IF NOT EXISTS archer(
archerID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
archer_first_name VARCHAR(30) NOT NULL,
archer_middel_name VARCHAR(30),
archer_last_name VARCHAR(30) NOT NULL,
archer_email VARCHAR(100),
password VARCHAR(200) NOT NULL
);
''')

curser.execute('''
INSERT INTO archer (username, archer_first_name,archer_middel_name, archer_last_name, archer_email, password)
VALUES('test_1', 'bob', 'middelton', 'latsis', 'email', 'test_1')
''')
db.commit()

curser.execute('''
SELECT * FROM Archer
''')

print(curser.fetchall())
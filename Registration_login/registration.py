import sqlite3
import hashlib
# connect represent the connection on the on-disk database

con = sqlite3.connect('userdata.db') 
cur = con.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS userdata(
            id INTEGER PRIMARY KEY, 
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            user_type INT
            )""")

'''
Just some old example without the email, the database should be empty now 
username1, password1 = "jeff2408", hashlib.sha256("123456789".encode()).hexdigest()
username2, password2 = "slicelizardman", hashlib.sha256("meat".encode()).hexdigest()
username3, password3 = "krillarmor", hashlib.sha256("cartsliding".encode()).hexdigest()
username4, password4 = "kinguspingus", hashlib.sha256("thebestoftwoworld".encode()).hexdigest()
username5, password5 = "puttshover", hashlib.sha256("herefortheride".encode()).hexdigest()'''

username = str(input("Username: "))
password = str(input("Password: "))
email = str(input("Email: "))

password = hashlib.sha256(password.encode()).hexdigest()
cur.execute('INSERT INTO userdata(username,password,email) VALUES (?,?,?)', (username,password,email))

con.commit()


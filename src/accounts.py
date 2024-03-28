import os
import bcrypt
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Users "
        "(username VARCHAR(255), password VARCHAR(255))"
    )
    connection.close()

create_table()

def register(username, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Users (username, password) VALUES (%s, %s)", 
        (username, hashed)
    )
    connection.commit()
    connection.close()

def login(username, password):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT password FROM Users WHERE username = %s", 
        (username,)
    )
    hashed = cursor.fetchone()[0]
    connection.close()
    if bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')):
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False
import os
import bcrypt
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load environment variables
load_dotenv()

# Function to create a connection to the database
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
        return None

# Function to create the Users table
def create_table():
    connection = create_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)
    except Error as e:
        print("Error while creating table", e)
    connection.close()

# Create the Users table
create_table()

# Function to register a new user
def register(username, password):
    connection = create_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        # Check if username already exists
        cursor.execute(
            "SELECT * FROM Users WHERE username = %s", 
            (username,)
        )
        if cursor.fetchone() is not None:
            print("Username already exists.")
            return
        
        # Hash the password
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # Insert the new user into the Users table
        cursor.execute(
            "INSERT INTO Users (username, password) VALUES (%s, %s)", 
            (username, hashed)
        )
        connection.commit()
        # Only print this message if a new user was successfully registered
        print("User registered successfully.")
    except Error as e:
        print("Error while inserting into table", e)
    connection.close()

# Function to login a user
def login(username, password):
    connection = create_connection()
    if connection is None:
        return False
    cursor = connection.cursor()
    try:
        # Fetch the password of the user with the provided username
        cursor.execute(
            "SELECT password FROM Users WHERE username = %s", 
            (username,)
        )
        result = cursor.fetchone()
        if result is None:
            print("No user found with this username.")
            return False
        hashed = result[0]
        # Check if the provided password matches the stored password
        if bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')):
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False
    except Error as e:
        print("Error while fetching from table", e)
        return False
    finally:
        connection.close()
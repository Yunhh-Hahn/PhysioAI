import sqlite3
import hashlib
import socket
import threading 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()

def handle_connection(c):
    c.send("Username: ".encode()) #Since in the database it is in byte we also have to encode into byte
    username = c.recv(1024).decode()
    
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()

    con = sqlite3.connect("userdata.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username,password))
    try:
        if cur.fetchall():
            c.send("Login successful!\nAre you a user(0) or a physiotherapist(1): ".encode())
            user_type = c.recv(1024).decode()
            cur.execute('''
                        UPDATE userdata
                        SET user_type = ?
                        WHERE username = ?
        ''', (int(user_type),username))
            con.commit()
            
            if user_type == "1":
                c.send("physiotherapist".encode())
            else: 
                c.send("user".encode())
        else:
            raise Exception
    except:
        c.send("Login failed!".encode())
    finally:
        #Because I close the connection, it will display "[WinError 10038] An operation was attempted on something that is not a socket". This is not a bug 
        #It is a way to end the server connectivity, remove it if you want multiple client connection to the server 
        server.close()  

while True:
    client, addr = server.accept()
    #Create thread to handle multiple client connection to the server 
    threading.Thread(target=handle_connection, args=(client,)).start()

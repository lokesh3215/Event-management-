import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    #cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY autoincrement,username text NOT NULL,password text NOT NULL)")
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users
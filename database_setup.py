import sqlite3 # importing the sqlite3 database package

DB_NAME = 'students.db' # The name of the database . python will create it auto

def get_connection():
    return sqlite3.connect(DB_NAME) # function for opening the database . the database will open whenever this function is called

def create_db():
    conn = get_connection() # Opening the database to write
    cursor = conn.cursor() # cursor is like a pen used to write SQL commands
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS  students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER,
                        grade TEXT,
                        email TEXT
                    )
                   ''')# Telling the cursor to create the tables the id will auto increment and the name can't be left empty
    conn.commit() # commit means save changes
    conn.close() # closing the open database which we opened in line 9
    
    print('Database creation complete')
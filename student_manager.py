# We will wrap all the functions in a class and use this file as backend

from database_setup import get_connection # importing the get_connection method so we can open the database

class StudentManager:
    
    # Method for adding a student in database
    def add_student(self,name,age,grade,email): # We are not using id here cause we made id auto increment 
        conn = get_connection() # opening the database to write
        cursor = conn.cursor() # activating the cursor to write in the database tables
        
        cursor.execute('INSERT INTO students (name, age, grade, email) VALUES (?,?,?,?)',(name,age,grade,email,))# Telling the database which data will go in which table
       # the ? values are temporary values to hold the field until we give data
        
        conn.commit() # saving the data
        conn.close() # closing the database which we opened in line 7
        
    # Method to read all the student data from the table
    def view_student(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM students') # holding all the data from student table
        rows = cursor.fetchall() # fetching all the data {fetchall() returns all rows as a list or tuple}
        
        conn.close() # closing the database which we opened in line 18
        print(*rows) if rows else print("! Student not found !") # *rows unpacks the list rows which is a list of tupples 
        
    # Method for searching a student in the database 
    def search_student(self,student_id):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM students WHERE id = ?',(student_id)) # Find the student who has this id number 
        row = cursor.fetchone() # telling the curosr to give me the row it found {fetchone() returns just one row as a tuple}
        
        conn.close() # closing the database which we opened in line 29
        
        print(row) if row else print("! Student not found !")
        
        
    # Method fro updating student
    def update_student(self,student_id,name,age,grade,email): # getting the id for queering the student we want to update info of 
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
                        UPDATE students
                        SET name = ?,age = ?,grade = ?,email = ?
                        WHERE id = ?
                       ''',(name,age,grade,email,student_id))
        
        conn.commit() # you need to commit every time you make any changes to database .
        conn.close() # closing the database which we opened in line 42
        print("Student information updated !")
        
    
    # Method for deleting a student
    def delete_student(self,student_id):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
                        DELETE FROM students WHERE id = ?
                       ''',(student_id,))
        
        conn.commit()
        conn.close() # closing the database which we opened in line 58
        print("Student deleted successfully !")
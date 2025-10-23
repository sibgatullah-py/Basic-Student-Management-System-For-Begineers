# Basic-Student-Management-System-For-Begineers
A simple Student Management System built with Python and SQLite for beginners.
This project demonstrates how to store, manage, and manipulate student data in a database using object-oriented programming (OOP) principles.

Features:
  1. Add new students (Name, Age, Grade, Email)
  2. View all students
  3. Search a student by ID
  4. Update student details
  5. Delete a student
  6. Fully CLI-based (runs in terminal/command prompt)
  7. Beginner-friendly code with OOP structure


How It Works:
  1. Database Setup (database_setup.py)
     
    -> Creates a SQLite database file named students.db
    -> Creates a students table if it doesn’t exist
    -> Columns: id (auto-increment), name, age, grade, email
  
  2. StudentManager Class (student_manager.py)
  
  Encapsulates all student operations:
   -> add_student()
   -> view_students()
   -> search_student()
   -> update_student()
   -> delete_student()
  
  Uses sqlite3 to connect to the database
  
  Each method opens the database connection, executes SQL, commits changes, and closes the connection
  
  3. CLI Menu (main.py)
   -> Displays a menu for the user to choose actions (1-6)
   -> Calls the corresponding method from StudentManager based on user input
   -> Loops continuously until the user selects Exit


How to Run:
  Clone the repository            : git clone <your-repo-url>
  Navigate to the project folder  : cd Basic-Student-Management-System
  Run the progra                  : python main.py


📝 Notes for Beginners

  Always check your SQL syntax — missing commas or parentheses can cause errors
  Use fetchone() when expecting a single row, and fetchall() for multiple rows
  Keep your code organized with separate files and classes
  This project is ideal for learning Python OOP + SQLite

👨‍💻 Future Improvements

  Add search by name or grade
  Add sorting options (by age or name)
  Integrate a GUI using Tkinter or PyQt
  Add CSV import/export functionality

🔗 References

Python official docs: [sqlite3 module](https://docs.python.org/3/library/sqlite3.html)
Python OOP basics   : [Classes and Objects](https://docs.python.org/3/tutorial/classes.html)

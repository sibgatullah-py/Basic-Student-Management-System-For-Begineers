# We will make our CLI menu here . This file will talk to use (the user)
# This file imports both the database and the class, and runs everything including the database_setup.py file 

from database_setup import create_db
from student_manager import StudentManager

def main():
    manager = StudentManager() # making the editor who will perform the CRUD operation on the database (the user)
    
    while True:
        print('\n<----- Student Management System ----->')
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        action = input('Enter action you want to perform (1-6): ') # input functions returns string so we will use str as our conditions
        
        if action == '1':
            name = input('Enter name: ')
            age = input('Enter age: ')
            grade = input('Enter grade: ')
            email = input('Enter email: ')
            manager.add_student(name,age,grade,email)# passing the data to add_student() method/function that we created in student_manager.py file
            
        elif action == '2':
            manager.view_student() # calling the view_student method/function so we can see all the students data in the database as tuple.
            
        elif action == '3':
            student_id = int(input('Enter student ID: '))
            manager.search_student(student_id) # giving the input number to the search_student method/function 
        
        elif action == '4':
            student_id = int(input('Enter student ID: '))
            name = input('Enter new name: ')
            age = input('Enter new age: ')
            grade = input('Enter new grade: ')
            email = input('Enter new email: ')
            manager.update_student(student_id, name, age, grade, email)
        
        elif action == '5':
            student_id = int(input('Enter student ID to delete: '))
            manager.delete_student(student_id)
            
        elif action == '6':
            print('Exiting Database ...')
            break
        
        else:
            print('Invalid Input! Choose the action you want to perform')
            

if __name__ == '__main__': # This dander method is for testing the page you can ignore it 
    main()
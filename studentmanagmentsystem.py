# Student Management System using File Handling in Python
# Saves student data (Name, Roll No, Branch) to a 'students.txt' file.

STUDENT_FILE = "students.txt"

def add_student():
    """Adds new student data to the file."""
    print("\n--- Add New Student ---")
    name = input("Enter Name: ")
    roll_no = input("Enter Roll Number: ")
    branch = input("Enter Branch (e.g., CSE): ")
    
    # Format the data line
    student_data = f"Name: {name}, Roll No: {roll_no}, Branch: {branch}\n"
    
    try:
        # Open file in 'append' mode to add new data
        with open(STUDENT_FILE, 'a') as file:
            file.write(student_data)
        print("✅ Student data added successfully!")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

def view_students():
    """Displays all student data from the file."""
    print("\n--- All Students ---")
    try:
        # Open file in 'read' mode
        with open(STUDENT_FILE, 'r') as file:
            data = file.readlines()
        
        if not data:
            print("💡 No student records found.")
            return

        for line in data:
            print(line.strip()) # strip() removes the extra newline character
            
    except FileNotFoundError:
        print("💡 Student file not found. Please add a student first.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

def main_menu():
    """Main menu to run the program."""
    while True:
        print("\n===== Student Management System =====")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if _name_ == "_main_":
    main_menu()
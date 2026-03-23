import sqlite3

# Connect to database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    salary REAL,
    experience INTEGER
)
""")
conn.commit()

# ADD DATA
def add_teacher():
    name = input("Enter teacher name: ")
    subject = input("Enter subject: ")
    salary = float(input("Enter salary: "))
    experience = int(input("Enter years of experience: "))

    cursor.execute("INSERT INTO teachers (name, subject, salary, experience) VALUES (?, ?, ?, ?)",
                   (name, subject, salary, experience))
    conn.commit()
    print("Teacher added successfully!\n")

# UPDATE DATA
def update_teacher():
    teacher_id = int(input("Enter teacher ID to update: "))
    new_salary = float(input("Enter new salary: "))

    cursor.execute("UPDATE teachers SET salary = ? WHERE teacher_id = ?",
                   (new_salary, teacher_id))
    conn.commit()
    print("Teacher updated successfully!\n")

# DELETE DATA
def delete_teacher():
    teacher_id = int(input("Enter teacher ID to delete: "))

    cursor.execute("DELETE FROM teachers WHERE teacher_id = ?", (teacher_id,))
    conn.commit()
    print("Teacher deleted successfully!\n")

# SELECT DATA
def view_teachers():
    cursor.execute("SELECT * FROM teachers")
    rows = cursor.fetchall()

    print("\nTeacher Records:")
    print("ID | Name | Subject | Salary | Experience")
    print("------------------------------------------")
    for row in rows:
        print(row)
    print()

# ADD MANY DATA
def add_many_teachers():
    n = int(input("How many teachers do you want to add? "))
    teachers_list = []

    for i in range(n):
        print(f"\nEnter details for Teacher {i+1}")
        name = input("Name: ")
        subject = input("Subject: ")
        salary = float(input("Salary: "))
        experience = int(input("Experience: "))

        teachers_list.append((name, subject, salary, experience))

    cursor.executemany("INSERT INTO teachers (name, subject, salary, experience) VALUES (?, ?, ?, ?)",
                       teachers_list)
    conn.commit()
    print("Multiple teachers added successfully!\n")

# Menu-driven program
while True:
    print("====== Teacher Management System ======")
    print("1. Add Teacher")
    print("2. View Teachers")
    print("3. Update Teacher")
    print("4. Delete Teacher")
    print("5. Add Multiple Teachers")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_teacher()
    elif choice == '2':
        view_teachers()
    elif choice == '3':
        update_teacher()
    elif choice == '4':
        delete_teacher()
    elif choice == '5':
        add_many_teachers()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")

# Close connection
conn.close()
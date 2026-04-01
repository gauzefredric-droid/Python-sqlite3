import customtkinter as ctk
import sqlite3

#DATABASE SETUP
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

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

#FUNCTIONS

def add_teacher():
    name = name_entry.get()
    subject = subject_entry.get()
    salary = salary_entry.get()
    experience = exp_entry.get()

    if name and subject and salary and experience:
        cursor.execute(
            "INSERT INTO teachers (name, subject, salary, experience) VALUES (?, ?, ?, ?)",
            (name, subject, float(salary), int(experience))
        )
        conn.commit()
        output_box.insert("end", "Teacher added successfully\n")
        clear_fields()
    else:
        output_box.insert("end", "Please fill all fields\n")


def view_teachers():
    cursor.execute("SELECT * FROM teachers")
    rows = cursor.fetchall()

    output_box.delete("1.0", "end")
    output_box.insert("end", "ID | Name | Subject | Salary | Experience\n")
    output_box.insert("end", "-" * 50 + "\n")

    for row in rows:
        output_box.insert("end", f"{row}\n")


def update_teacher():
    teacher_id = id_entry.get()
    new_salary = salary_entry.get()

    if teacher_id and new_salary:
        cursor.execute(
            "UPDATE teachers SET salary = ? WHERE teacher_id = ?",
            (float(new_salary), int(teacher_id))
        )
        conn.commit()
        output_box.insert("end", "Teacher updated\n")
        clear_fields()
    else:
        output_box.insert("end", "Enter ID and new salary\n")


def delete_teacher():
    teacher_id = id_entry.get()

    if teacher_id:
        cursor.execute("DELETE FROM teachers WHERE teacher_id = ?", (int(teacher_id),))
        conn.commit()
        output_box.insert("end", "Teacher deleted\n")
        clear_fields()
    else:
        output_box.insert("end", "Enter Teacher ID\n")


def clear_fields():
    name_entry.delete(0, "end")
    subject_entry.delete(0, "end")
    salary_entry.delete(0, "end")
    exp_entry.delete(0, "end")
    id_entry.delete(0, "end")


#UI SETUP

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Teacher Management System")
app.geometry("700x500")

#INPUT FIELDS

frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=10, fill="x")

name_entry = ctk.CTkEntry(frame, placeholder_text="Name")
name_entry.grid(row=0, column=0, padx=5, pady=5)

subject_entry = ctk.CTkEntry(frame, placeholder_text="Subject")
subject_entry.grid(row=0, column=1, padx=5, pady=5)

salary_entry = ctk.CTkEntry(frame, placeholder_text="Salary")
salary_entry.grid(row=1, column=0, padx=5, pady=5)

exp_entry = ctk.CTkEntry(frame, placeholder_text="Experience")
exp_entry.grid(row=1, column=1, padx=5, pady=5)

id_entry = ctk.CTkEntry(frame, placeholder_text="Teacher ID (for update/delete)")
id_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

#BUTTONS

btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

ctk.CTkButton(btn_frame, text="Add Teacher", command=add_teacher).grid(row=0, column=0, padx=5, pady=5)
ctk.CTkButton(btn_frame, text="View Teachers", command=view_teachers).grid(row=0, column=1, padx=5, pady=5)
ctk.CTkButton(btn_frame, text="Update Salary", command=update_teacher).grid(row=0, column=2, padx=5, pady=5)
ctk.CTkButton(btn_frame, text="Delete Teacher", command=delete_teacher).grid(row=0, column=3, padx=5, pady=5)

#OUTPUT BOX

output_box = ctk.CTkTextbox(app, height=250)
output_box.pack(padx=10, pady=10, fill="both", expand=True)

app.mainloop()

# Close DB when app exits
conn.close()
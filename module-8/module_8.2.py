"""
Author: Aysa Jordan
Date: November 21, 2025
Assignment: Module 8.2
"""

"""
This program loads a list of students from a JSON file, prints the original list,
adds a new student record, prints the updated list, and then writes the changes
back to the JSON file. A small notification window appears at the end to confirm
that the file was updated.
"""

import json
import tkinter as tk
from tkinter import messagebox

# Print Function
def print_students(student_list):
    for s in student_list:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")
    print()  # blank line for readability

def main():
    # Load the JSON file
    with open("student.json", "r") as file:
        students = json.load(file)

    print("Original Student List:")
    print_students(students)

    # Create a new student record to add to the list
    new_student = {
        "F_Name": "Aysa",
        "L_Name": "Jordan",
        "Student_ID": 88521,  # fictional ID
        "Email": "ayjordan@my365.bellevue.edu"
    }

    students.append(new_student)

    print("Updated Student List:")
    print_students(students)

    # Overwrite the JSON file with new list
    with open("student.json", "w") as file:
        json.dump(students, file, indent=2)

    print("student.json file has been updated.")

    # -----------------------------
    # Show popup simulating "file changed" notification
    root = tk.Tk()
    root.withdraw()  # hide main window

    result = messagebox.askyesno(
        "File Changed",
        "The file student.json has been modified outside. Do you want to reload it?"
    )

    print("Popup result:", "Yes" if result else "No")


if __name__ == "__main__":
    main()
# Existing Dictionary with student details
print("Existing Studnet")
Student = {
    "Rohan": {"Age": 20, "Major": "Computer Science", "Grade": "A"},
    "Sohan": {"Age": 21, "Major": "Engineering", "Grade": "B"},
    "Ram": {"Age": 19, "Major": "Mathematics", "Grade": "B+"}
}
print(Student)

# Print the list of new students
new_Students = [
    {"Name": "Eva", "Age": 22, "Major": "Physics", "Grade": "A"},
    {"Name": "Michael", "Age": 20, "Major": "Biology", "Grade": "A+"},
    {"Name": "Zoya", "Age": 21, "Major": "History", "Grade": "B"},
]

print("Adding three new students...")

# Adding new students to the existing dictionary
for student in new_Students:
    Name = student["Name"]
    details = {"Age": student["Age"], "Major": student["Major"], "Grade": student["Grade"]}
    Student[Name] = details

# Print the updated student dictionary
print("Updated student list:")
for name, details in Student.items():
    print(f"{name}: {details}")



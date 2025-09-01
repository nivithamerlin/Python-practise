# Convert a nested dictionary of students → subjects → marks into a flat list of tuples (student, subject, mark).
students_data = {
    "Nivitha": {"math": 90, "science": 100, "english": 85},
    "Subathra": {"math": 94, "science": 67, "english": 88},
    "Rekha": {"math": 78, "science": 89, "english": 92}
}
flat_list = []

for student, subjects in students_data.items():
    for subject, mark in subjects.items():
        flat_list.append((student, subject, mark))

print(flat_list)

# convert nested dict to list of dict:
students_nested = {
    "S1": {"name": "Nivitha", "marks": {"math": 90, "english": 80}},
    "S2": {"name": "Rekha", "marks": {"math": 45, "science": 55, "english": 40, "history": 75}}
}
students_list = []
for students, data in students_nested.items():
    new_dict = {
        "id": students,
        "name": data["name"],
        "marks": data["marks"]
    }
    students_list.append(new_dict)
print(students_list)

# create a dict of square of number
numbers = [1, 2, 3, 4, 5]
square_nos = {}
for num in numbers:
    square_nos[num] = num ** 2
print("square_nos")
    
# combine the two list into dictionary
students = ["Alice", "Bob", "Charlie"]
marks = [85, 92, 78]
student_marks = {}
for i in range(len(students)):
    student_marks[students[i]] = marks[i]
print(student_marks)

#  email - count the duplicates 
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
email_count = {}
for email in emails:
    if email in email_count:
        email_count[email] += 1
    else:
        email_count[email] = 1
print(email_count)
duplicate = []
for email, count in email_count.items():
    if count > 1:
        duplicate.append(email)
print(duplicate)
print(square_nos)



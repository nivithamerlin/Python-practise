# Remove all entries from a list of dictionaries where any subject mark is less than 35
students = [
    {"name": "Nivitha", "marks": {"math": 90, "science": 100, "english": 85}},
    {"name": "Subathra", "marks": {"math": 94, "science": 30, "english": 88}},
    {"name": "Rekha", "marks": {"math": 78, "science": 89, "english": 92}},
    {"name": "Priya", "marks": {"math": 20, "science": 40, "english": 50}}
]

filtered_students = []  # new list to store students who pass

for student in students:
    has_failed_subject = False
    for mark in student["marks"].values():
        if mark < 35:
            has_failed_subject = True
            break  # stop checking further subjects for this student
    if not has_failed_subject:
        filtered_students.append(student)

print(filtered_students)

#  Merge two lists of dictionaries by "id" so that common IDs combine their data.

list1 = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Phone"}
]

list2 = [
    {"id": 1, "price": 150000},
    {"id": 2, "price": 95000}
]

merged_list = []

for item1 in list1:
    for item2 in list2:
        if item1["id"] == item2["id"]:
            merged_dict = {**item1, **item2}  # merge two dictionaries
            merged_list.append(merged_dict)

print(merged_list)

# convert list of dic into nested dictionary:
products = [
    {"id": "P1", "name": "Pen", "price": 10},
    {"id": "P2", "name": "Book", "price": 50},
    {"id": "P3", "name": "Pencil", "price": 5}
]
nested_dic = {}
for d in products:
    key = d["id"]
    value = {k: v for k, v in d.items() if k != "id"}
    nested_dic[key] = value
print(nested_dic)

# Sort a list of dictionaries by a nested key (e.g., "Subject" → "math" score).
students = [
    {"name": "Nivitha", "Subject": {"math": 85, "science": 90}},
    {"name": "Merlin", "Subject": {"math": 92, "science": 88}},
    {"name": "Rekha", "Subject": {"math": 78, "science": 95}}
]
students.sort(key=lambda student: student["Subject"]["math"])
print(students)

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

# group the second lowest score, if two have same order the name alphabetically
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

scores = []
for stud in students:
    scores.append(stud[1])
print(scores)
unique_score = []
for score in scores:
    if score not in unique_score:
        unique_score.append(score)
print(unique_score)
unique_score.sort()
print(unique_score)
second_lowest = []
second_lowest = unique_score[1]
print(second_lowest)
result = []
for stud in students:
    name = stud[0]
    score = stud[1]
    if score == second_lowest:
        result.append(name)
print(result)
result.sort()
print(result)

# group words by their first letter
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
grouped = {}
for char in words:
    first_letter = char[0]
    if first_letter not in grouped:
        grouped[first_letter] = []
    grouped[first_letter].append(char)
print(grouped)


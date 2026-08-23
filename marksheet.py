print("welcome to the marksheet")

name = input("enter your name: ").strip()
class_name = input("enter your class: ").strip()
roll_no = input("enter your roll no: ").strip()

students = [
    {
        "name": "desh raj pandey",
        "class": "12th A",
        "roll_no": "1",
        "marks": {
            "physics": 98,
            "chemistry": 97,
            "biology": 95,
            "maths": 91,
            "english": 94,
        },
    },
    {
        "name": "aarti pandey",
        "class": "12th A",
        "roll_no": "2",
        "marks": {
            "physics": 89,
            "chemistry": 88,
            "biology": 87,
            "maths": 86,
            "english": 85,
        },
    },
]

found = False
for student in students:
    if (
        student["name"].lower() == name.lower()
        and student["class"].lower() == class_name.lower()
        and student["roll_no"] == roll_no
    ):
        found = True
        print(f"\nMarksheet for {student['name']}")
        print(f"Class: {student['class']}")
        print(f"Roll No: {student['roll_no']}")
        print("Marks:")
        total = 0
        for subject, mark in student["marks"].items():
            print(f"  {subject.title()}: {mark}")
            total += mark
        percentage = total / len(student["marks"])
        print(f"Total: {total}")
        print(f"Percentage: {percentage:.2f}%")
        break

if not found:
    print("invalid input")

students = {}

n = int(input("How many students do you want to add? "))

for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = eval(input("Enter the marks of student: "))

    students[roll] = (name, marks)

print("\nAll records added:", students)

for i in students:
    name = students[i][0]
    marks = students[i][1]

    total = 0
    for m in marks:
        total += m

    average = total / len(marks)

    if average > 80:
        print(name)

r= input("Enter roll number to update marks: ")
 
if r in students:
    name = students[r][0]
    marks = students[r][1]
 
    print("Current marks:", marks)
    new_marks = eval(input("Enter new list of marks: "))
    students[r]=(name, new_marks)
 
    print("Updated record:", students)
else:
    print("Roll number not found.")



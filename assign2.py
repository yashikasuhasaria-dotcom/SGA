students = {}

while True:
    print("1. Add a student record")
    print("2. Display students with average above 80")
    print("3. Update marks for a roll number")

    choice = input("Enter your choice: ")

    if choice == "1":
        n=int(input("Enter number of students to add: "))
        for i in range (n):
            roll = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = eval(input("Enter the marks of student: "))
            students[roll] = (name, marks)
        print("Record added\n", students)

    elif choice == "2":
        for i in students:
            name = students[i][0]
            marks = students[i][1]

            total = 0
            for m in marks:
                total += m

            average = total / len(marks)

            if average > 80:
                print(name)

    elif choice == "3":
        r = input("Enter roll number to update marks: ")
        if r in students:
            name = students[r][0]
            marks = students[r][1]
            print("Current marks:", marks)
            new_marks = eval(input("Enter new list of marks: "))
            students[r] = (name, new_marks)
            print("Updated record:", students[r])
        else:
            print("Roll number not found.")
    else:
        print("Invalid choice, try again.")
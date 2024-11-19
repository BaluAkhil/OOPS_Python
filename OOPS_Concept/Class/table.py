from tabulate import tabulate

class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch 
        self.email = roll_no + '.' + '@gvpce.ac.in'

    def student_details(self):
        return [self.name, self.roll_no, self.branch, self.email]

def display_students(students):
   
    data = [[i + 1] + stu.student_details() for i, stu in enumerate(students)]
    
   
    headers = ["S.No", "Name", "Roll Number", "Branch", "Email"]

    print(tabulate(data, headers, tablefmt='grid'))

def main():
    students = []
    
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            roll_no = input("Enter roll number: ")
            branch = input("Enter branch: ")
            student = Student(name, roll_no, branch)
            students.append(student)
            print("Student added successfully.\n")

        elif choice == '2':
            if students:
                display_students(students)
            else:
                print("No students to display.\n")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.email = roll_no + '@gvpce.ac.in'

    def student_details(self):
        # Return a tuple with individual elements for unpacking
        return (self.name, self.roll_no, self.branch, self.email)

def create_students():
    students = []
    while True:
        name = input("Enter Student's name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        roll_no = input("Enter Student's Roll Number: ")
        branch = input("Enter Student's branch: ")
        students.append(Student(name, roll_no, branch))
    return students

def display_details(students):
    if not students:
        print("Student details are not available.")
    else:
        # Column headings
        print(f"\n{'S.No':<6} {'Name':<20} {'Roll No':<10} {'Branch':<10} {'Email':<30}")
        print("=" * 78)  # Divider for clarity

        # Display student details with aligned columns
        for index, student in enumerate(students, start=1):
            name, roll_no, branch, email = student.student_details()
            print(f"{index:<6} {name:<20} {roll_no:<10} {branch:<10} {email:<30}")

if __name__ == "__main__":
    students = create_students()
    display_details(students)

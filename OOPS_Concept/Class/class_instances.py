## Class
class Student:
    def __init__ (self, name, roll_no , branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch 
        self.email = roll_no + '.' + '@gvpce.ac.in'
    
    #Method
    def Student_Details(self):
        return (self.name, self.roll_no, self.branch, self.email)
  

def create_students():
    students =[]
    while True:
        name = input("Enter Student's name (or type 'exit' to stop : )")
        if name.lower() == 'exit':
            break
        roll_no = input("Enter Student's Roll Number : ")
        branch  = input("Enter Student's branch : ")

        students.append(Student(name, roll_no, branch))
    return students

def Display_Details(students):
    if not students:
        print(" Student Details are not available ")
    else:
        print("\n---------------Student Details--------------------- ")

        print(f"\n{'S.No':<6} {'Name':<20} {'Roll No':<10} {'Branch':<10} {'Email':<30}")
        print("=" * 78) 
        
        for index, student in enumerate(students, start=1):
            name, roll_no, branch, email = student.Student_Details()
            print(f"{index:<6} {name:<20} {roll_no:<10} {branch:<10} {email:<30}")


if __name__ == "__main__":
     ##instance 
     students = create_students()
     Display_Details(students)
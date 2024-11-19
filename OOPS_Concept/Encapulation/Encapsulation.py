### Accesing the Private Attributes Using the Public Methods 
class Student:
    def __init__(self, name, age):
        self.name = name 
        self.__age = age 
    
    def display(self):
        return '{} {} '.format(self.name, self.__age)

def student_Details():
    student = []
    while True:
        name = input("Enter the name : ")
        age = int(input("Enter the age : "))
        student.append(Student(name, age))

        next = int(input("Enter 1 -> continue and 0 -> break : "))
        if next == 0:
            break
    return student

student = student_Details()

for stu in student:
    print(stu.display())
    


    
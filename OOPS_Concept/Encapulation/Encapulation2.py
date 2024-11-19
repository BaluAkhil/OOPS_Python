class Student:
    def __init__(self, name, rollno, age):
        self.name = name 
        self._rollno = rollno 
        self.__age = age 
    
    def __display(self):
        print('{} {} {}'.format(self.name, self._rollno, self.__age))

    def DisplayPrivateData(self):
        self.__display()

s1 = Student("Akhil", 4404, 21)
print(s1._Student__age)
s1._Student__age = 24
s1._Student__display()
s1.DisplayPrivateData()
s1.__age
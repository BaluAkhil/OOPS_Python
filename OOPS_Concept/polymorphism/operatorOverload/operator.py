class ComplexNumber:
    def __init__(self, real, imaginary):
         self.real = real
         self.imaginary = imaginary

    def __add__(self, other):
         return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
    
    def __str__(self):
         return f"{self.real} + {self.imaginary}i"
         
c1 = ComplexNumber(4,5)
c2 = ComplexNumber(1,4)
print(c1 + c2)
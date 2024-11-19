from abc import ABC,abstractmethod

class demo(ABC):
    @abstractmethod
    def method1(self):
        print("Abstrct Method")
    def method2(self):
        print("Concrete Method")

obj = demo()   ## ---> Can't instantiate abstract class demo without an implementation for abstract method 'method1'_
obj.method2()
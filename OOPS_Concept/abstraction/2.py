from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        print("I am computer")

class Laptop(Computer): ## --> Can't instantiate without implementaion of abstrct method 'process'
    pass

class Laptop1(Computer):
    def process(self):    ## --> import abstrct method 'process'
        super().process()  ## --> Inherit from Computer class and it is called method overriding 
        print("I am Laptop")  ## --> Laptop has it's own behaviour 

class Programmer:
    def work(self, com):
        print(" Writing Logic ")

class tester:
    def test(self):
        print("Solving Bugs and Errors")

cp1 = Laptop1()
prog = Programmer()

cp2 = tester()
prog.work(cp2)
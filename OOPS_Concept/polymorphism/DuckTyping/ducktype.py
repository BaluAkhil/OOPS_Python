class Duck:
    def swim(self):
        print("I am a duck and I can swim")
    def speaks(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print("I am dog and I can swim")
    def speaks(self):
        print("Bow Bow ")


def display(duck):
    duck.swim()
    duck.speaks()


obj = Duck()
obj2 = Dog()

display(obj)
display(obj2)
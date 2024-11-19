class Human:
    def __init__(self, no_hearts):
        self.no_eyes = 2
        self.no_nose = 1
        self.no_hearts = no_hearts

    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")

class Male(Human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name = name

    def flirt(self):
        print("I can Flirt")
    def work(self):
        super().work()
        print("I can code")

s1 = Male("Akhil",1)
##s1.eat()
##s1.work()
print(s1.no_eyes)
print(s1.no_hearts)

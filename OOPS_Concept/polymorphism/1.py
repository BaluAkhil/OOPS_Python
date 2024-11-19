class X:
    def __init__(self, x):
        self.x = x
    def __add__(self, y):
        return self.x + y.x
    
obj1  = X(5)
obj2 = X(4)
print(obj1 + obj2)
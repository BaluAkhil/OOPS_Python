class Adding:

    def add(self, *args):   ## agrs --> Variable length arguments 
        sum = 0
        for i in args:
            sum = sum + i
        return sum

a = Adding()

print(a.add(10, 20))
print(a.add(10, 20 ,30))
print(a.add(10, 20, 30, 40))
print(a.add(10, 20, 30, 40, 50, 60))
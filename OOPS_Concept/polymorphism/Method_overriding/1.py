class Father:
    
    def sleep(self):
        print("Sleeps from 10:00 PM to 5:00 AM")
    def eat(self):
        print("Eating")
    
class Son(Father):

    def sleep(self):
        super().sleep()
        print("Sleeps from 2:00 AM to 10:AM ")

obj = Son()
obj.sleep( )
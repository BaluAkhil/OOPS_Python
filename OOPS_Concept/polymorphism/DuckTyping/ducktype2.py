class EmailNotification:

    def send(self, email):
        print("Notification From Enmail")
    def check(self, email):
        print("Spam Notification")
    
class SMSNotification:

    def send(self, sms):
        print("Notification via SMS")
    def check(self, sms):
        print("Spam SMS")

def display(EmailNotification, msg):
    EmailNotification.send(msg)
    EmailNotification.check(msg)

obj1 = EmailNotification()
obj2 =SMSNotification()

display(obj1, "You've got Email ")
display(obj2, "you've got a new SMS")
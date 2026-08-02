class Notification:
    def send(self):
        print("Sending notification...")
class Email(Notification):
    def send(self):
        print("Sending email")
class Sms(Notification):
    def send(self):
        print("Sending sms")
class Push(Notification):
    def send(self):
        print("Push notification")
no1=[Email(),Sms(),Push()]
for n in no1:
    n.send()
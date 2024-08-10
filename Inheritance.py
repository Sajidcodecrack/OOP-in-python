class car:
    color="black"
    @staticmethod
    def start():
        print("Car started ....")

    @staticmethod
    def brake():
        print("Car breaked ....")
class audi(car):
    def __init__(self,brand):
        self.brand=brand
        
class tesla(audi):
    def __init__(self,type):
        self.type=type
car1=tesla("octane")
car1.start()       
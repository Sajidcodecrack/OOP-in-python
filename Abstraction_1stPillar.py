class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.brk = True
        self.acc = True
        print("Car started...")

    def brake(self):  
        self.clutch = False  
        self.brk = True
        self.acc = False  
        print("Car stopped...")

c = Car()
c.start()
# c.brake()  

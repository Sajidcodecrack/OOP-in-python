from abc import ABC  
class shape(ABC):
    def area(self):
        
class rectangle(shape):
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        return self.length*self.width

rec=rectangle(3,5)
print("area is : ", rec.area())
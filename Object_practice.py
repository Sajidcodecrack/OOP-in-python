class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def get_avg(self):
        sum=0
        for val in self.mark:
            sum+=val
        print("Average score :",sum/3)
    @staticmethod
    def hey():
        print("How are you")
       
s1=student("Sajid ahamed",[83,93,88])
print(s1.name ," and his number ", s1.mark) 
s1.get_avg()
s1.name="faiz"
s1.get_avg()
s1.hey()
class student:
    def __init__(self,fullname,mark):
        self.name=fullname
        self.mark=mark
        print("Welcome to the construction")
        
s1=student("Sajid Ahamed",91)
print(s1)
print(s1.name,s1.mark)
s2=student("meaw meaw ",98)
print(s2.name,s2.mark)
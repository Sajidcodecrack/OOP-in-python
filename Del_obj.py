class student:
    def __init__(self, name):
        self.name = name

s1=student("sajid")
s2=student("Ahamed ")
del s1             #To delete the object 

print(s1.name)
print(s2.name)
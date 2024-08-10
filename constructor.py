class student:
    # name="sajid"
    school="Khulna zilla school"
    def __init__(self,fullname,mark):  #object attribute> class attribute
        self.name=fullname
        self.mark=mark
        print("Welcome to the construction")
    def welcome(self):
        print("Welocome to our coding journey ",s2.name,"&",s1.name)
    def get_mark(self):
        return self.mark
    
s1=student("Sajid ahamed",91)
print(s1)
print(s1.name,s1.mark)
s2=student("faiz baby  is my janeman ",97)
print(s2.name,s2.mark)
print(s2.school)
s1.welcome()
print(s1.get_mark())

#Constructor 
#All classes have a function called __init(), which is always executed when the object is being initiated 
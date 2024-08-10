class Person:
    name = "Annonymous"


    # def change_name(self, name):
    #  #Person.name = name
    #  self.__class__.name="Sajid"
    @classmethod
    def change_name(cls,name):
        cls.name="Ahamed"

p1 = Person()
p1.change_name("Sajid Ahamed")
print(p1.name)
print(Person.name)

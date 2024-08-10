class Car:
    def __init__(self, make, model, year):
        self.__make = make  # private 
        self.__model = model  # private 
        self.__year = year  # private 

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year


# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2022)

# Accessing attributes using getters
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

#Attempting to access private attributes directly (will raise an AttributeError)
# print(my_car.__make)
# print(my_car.__model)
# print(my_car.__year)

# Modifying attributes using setters
my_car.set_make("Honda")
my_car.set_model("Civic")
my_car.set_year(2023)

# Accessing attributes after modification
print("\nAfter modification:")
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

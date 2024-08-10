class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real, "i +", self.img, "j")

    # def add_num(self, num2):
    #     new_Real = self.real + num2.real
    #     new_img = self.img + num2.img
    #     return complex(new_Real, new_img)
    def __add__(self, num2):  # Dunder function
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return complex(new_real, new_img)

    def __sub__(self, num2):  # Dunder function
        new_real = self.real - num2.real
        new_img = self.img - num2.img
        return complex(new_real, new_img)

    def __mul__(self, num2):  # Dunder function
        new_real = self.real * num2.real
        new_img = self.img * num2.img
        return complex(new_real, new_img)

    def __div__(self, num2):
        new_real = self.real / num2.real
        new_img = self.img / num2.img
        return complex(new_real, new_img)


num1 = complex(2, 4)
num1.show_number()

num2 = complex(3, 5)
num2.show_number()

# num3=num1.add_num(num2)
# num3.show_number()

num3 = num1 + num2
num3.show_number()

num4 = num1 - num2
num4.show_number()

num5 = num1 * num2
num5.show_number()

num6=num1/num2
num6.show_number()
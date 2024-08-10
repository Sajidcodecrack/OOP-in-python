class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


st1 = student(83, 90, 97)
print(st1.percentage)
st1.math = 82
print(st1.math, "is the Updated number ")
print(f"New percentage ", st1.percentage)

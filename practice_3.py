class order:
    def __init__(self, price, item):
        self.price = price
        self.item = item

    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 = order("Chips", 20)
odr2 = order("coffee", 140)

print(odr1<odr2)
"""
name: {irfan teh}
id: {364211760046}
group: {MIT212}
"""


# create class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private member
        self.mobile = []

    # getter and setter method
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    def introduce(self):
        print(f'My name is {self.name}, I am {self.__age} year old,')
        self.display_mobile()

    def display_mobile(self):
        # print(len(self.mobile))
        for x in self.mobile:
            x.mobile_detail()


class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def mobile_detail(self):
        print(f'Brand: {self.brand} Model: {self.model} price: {self.price}')


p1 = Person('sam', 35)
# create object mobile
m1 = Mobile('Samsung', 'NOte 7', 25000.00)
p1.mobile.append(m1)

m2 = Mobile('iPhone', 'iPhone 13', 30000.00)
p1.mobile.append(m2)

p1.introduce()

p1.mobile.remove(m1)
p1.introduce()

print(p1.mobile[0].price)
p1.mobile[0].price = 33000.00
p1.introduce()
"""
name: {irfan teh}
id: {364211760046}
group: {MIT212}
"""



class Student:
    def __init__(self, name, id, age, weight, height ):
        self.name = name
        self.id = id
        self.__age = age  # private member
        self.__weight = weight
        self.__height = height
        self.vaccine = []

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    def get_height(self):
        return self.__height

    def set_height(self, new_age):
        self.__age = new_age

    def get_weight(self):
        return self.__weight

    def set_weight(self, new_weight):
        self.__age = new_weight

    def introduce(self):
        print(f'My name is {self.name}, ID{self.id}, I am {self.__age} year old, I am height {self.__height}, I am weight {self.__height} ')
        self.display_vaccine()

    def display_vaccine(self):
        for x in self.vaccine:
            x.vaccine_detail()


class vaccine:
    def __init__(self,vac_name):
        self.vac_name = vac_name

    def vaccine_detail(self):
        print(f'vac_name : {self.vac_name}')

std = Student('irfan teh', '046', 21, 53, 172 )
# create object mobile
v1 = vaccine('vac_name')
std.vaccine.append(v1)
print(std.vaccine)

# m2 = Mobile('iPhone', 'iPhone 13', 30000.00)
# p1.mobile.append(m2)

# p1.introduce()

# p1.vaccine.remove(m1)
# p1.introduce()
#
# print(p1.vaccine)
# p1.vaccine[0].price = 33000.00
# p1.introduce()
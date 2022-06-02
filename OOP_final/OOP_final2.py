"""
name: {irfan teh}
id: {364211760046}
group: {MIT212}
"""

class Student:
        def __init__(self, name, id, age, weight, height):
            # object Student
            self.name = name  # str
            self.id = id  # str
            self.age = age  # int
            self.weight = weight  # float
            self.height = height  # int

        def displayDetail(self):
            print(f'f{self.name} {self.id} {self.age} {self.weight} {self.height }')


class Vaccine:
    def __init__(self, vac_name):
        # object Student
        self.vac_name = vac_name  # str

    def displayDetail(self):
        print(f'f{self.vac_name}')


S = input('Student Name?: ')
I = int(input('ID?:'))
A = int(input('Age?: '))
W = float(input('Weight?: '))
H = int(input('Height?: '))
v = input('how many are you vaccincted ?: ')


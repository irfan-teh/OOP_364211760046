# class attributes

class Student:
    # class attribute
    major = 'MT'

    def __init__(self,name,group):
        # object attribute
        self.name = name
        self.group = group

    def introduce(self):
        print(f'My name is {self.name}, I\'m in {self.group} and'
              f'studying in {self.major} major.')

std1 = Student('irfan teh','MIT212')
std1.introduce

std2 = Student('irfan teh','MIT212')
std2.introduce

Student.major = 'LM'

std1.introduce()
std2.introduce()
"""
Student Name: irfan teh
ID: 046
Group: MIT212
"""

# Encapsulation

class Student:
    def __init__(self,name,age):
        # object attributes
        self.name = name  # public member
        self.__age = age    # private member
        self._major = 'MT'  # protected

    def display_info(self):
        print(f'Name: {self.name}\nAge: {self.__age}')

# create object of Student
std = Student('Irfan teh','21')
print(std.name)  # direct access
#print(std.__age)  # 35
# 1. use public methdo to access private member
std.display_info()
# 2. name mangling  --> _ClassName__attributeName
print(std._Student__age)

std._Student__age = 40 #
print(std._Student__age)
std.display_info()

# access to protected member
print(std._major)
std._major = 'AC'
print(std._major)

# std.age = 40
# print(std.age)  # 40
# std.age = -100
# print(std.age)
# std.display_info()

"""
name: {irfan teh}
id: {364211760046}
group: {MIT212}
"""

class Person:
    def __init__(self,name,email,tel):
        # object attributes
        self.__name = name # private member
        self.__email = email
        self.__tel = tel

    # getter and setter method
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email
    def get_tel(self):
        return self.__tel
    def set_tel(self, tel):
        self.__tel = tel

    # display Person object
    def __str__(self):
        print(f'\tName: {self.__name}\n'
              f'\temail: {self.__email}\n'
              f'\ttel: {self.__tel}\n')

class Student(Person):
    def __init__(self,name,email,tel,id,major):
        super().__init__(name,email,tel)
        #Person.__init__(self,name,email,tel)
        self.__id = id
        self.__major = major

    # getter and setter
    def get_id(self):
        return  self.__id
    def set_id(self,id):
        self.__id = id
    def get_major(self):
        return  self.__major
    def set_major(self,major):
        self.__major = major

    def __str__(self):
        # print('MT Vaccinated Passport (Student):')
        super().__str__()
        print(f'\tSID: {self.__id}\n'
              f'\tMajor: {self.__major}\n')

class Employee(Person):
    def __init__(self,name,email,tel,eid,position):
        super().__init__(name,email,tel)
        self.__eid = eid
        self.__position = position

    def get_eid(self):
        return self.__eid
    def set_eid(self, eid):
        self.__eid = eid
    def get_position(self):
        return self.__position
    def set_position(self,position):
        self.__position = position

    def __str__(self):
        # print('MT Vaccinated Passport (Employee):')
        super().__str__()
        print(f'\tPosition: {self.__eid}\n'
              f'\tMajor: {self.__position}\n')

class Courses(Person):
    def __init__(self,name, email, tel,course_id,course_name):
        super().__init__(name, email, tel)
        self.__course_id = course_id
        self.__course_name = course_name

    def get_course_id(self):
        return self.__course_id
    def set_course_id(self,course_id):
        self.__course_id = course_id
    def get_course_name(self):
        return self.__course_name
    def set_course_name(self,course_name):
        self.__course_name = course_name

    def __str__(self):
        # print('MT Vaccinated Passport (Student):')
        super().__str__()
        print(f'\tSID: {self.__course_id}\n'
              f'\tMajor: {self.__course_name}\n')

class CourseRegistration():
    def __init__(self, id,course_regis):
        self.id = id
        self.course_regis = course_regis
    def add_CourseRegistration(self,id,course_regis):
        self.id.append(id)
        self.course_regis.append(course_regis)
    def CourseRegistration_detail(self):
        print('Student Vaccinated Informations:')
        # self.student.student_detail()

name = input('Student Name? : ')
email = input('Student email? : ')
tel = input('Tel. : ')
sid = input('Student ID? : ')
major = input('Student major? : ')
eid = input('Eid? : ')
position = input('position? : ')
course_id = input('course_id? : ')
course_name = input('course_name? : ')

std = Student(name,email,tel,sid,major)
v = [] # list of vaccine object
# for x in vacc:
#     v.append(Vaccine(x))

std_Course = CourseRegistration()
# for x in v:
#     std_Course.add_CourseRegistration()
# for x in date:
#     std_vac.add_date(x)

std_Course.CourseRegistration_detail()






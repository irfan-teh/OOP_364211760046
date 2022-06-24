class Student():
    def __init__(self, name, id, age, weight, height):
        # object attributes
        self.__name = name
        self.__id = id
        self.__age = age
        self.__weight = weight
        self.__height = height

    # getter and setter methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_height(self):
        return self.__height

    def set_hegiht(self, height):
        self.__height = height

    def student_detail(self):
        print(f'\tSTD Name: {self.__name}\n'
                  f'\tID: {self.__id}\n'
                  f'\tAge: {self.__age}\n'
                  f'\tWeight: {self.__weight}\n'
                  f'\tHeight: {self.__height}\n')

class Vaccine():
    def __init__(self,vac_name):
        self.__vac_name = vac_name

    #getter and setter method
    def get_vaccine(self):
        return self.__vac_name
    def set_vaccine(self,new_name):
        self.__vac_name = new_name

    def vaccine_detail(self):
        print(f'Vaccine name: {self.__vac_name}')

class Vaccinated():
    def __init__(self, student):
        self.student = student
        self.vaccinated = list() # []
        self.date = list() # []
    def add_vaccinated(self,vaccine):
        self.vaccinated.append(vaccine)
    def add_date(self,date):
        self.date.append(date)

    def vaccinated_detail(self):
        print('Student Vaccinated Informations:')
        self.student.student_detail()

        for i in range(len(self.vaccinated)):
            print(f'\tvaccine {i+1}: {self.vaccinated[i].get_vaccine()} date: {self.date[i]}')

name = input('Student Name? : ')
id = input('Student ID? : ')
age = int(input('Age? : '))
if (age<18):
    print('ข้อมูลอายุต้องไม่ต่ำกว่า 18 ปี หากผู้ใช้กรอกข้อมูลไม่ถูกต้องให้กรอกข้อมูลใหม่')
weigth = float(input('Weight (kg): '))
heigth = float(input('Height (cm): '))

num = int(input('How many your vaccinated ? : '))
vacc = list()
date = list()
select = 1
for x in range(num):
    print(f'Select :')
    print("\t1.sinovac")
    print('\t2.astrazeneca')
    print('\t3.johnson&johnson')
    print('\t4.moderna')
    print('\t5.sinopharm')
    print('\t6.pfizer')
    while True:
        select = int(input('select(1-6): '))
        if select >=1 and select <=6:
            break
        print('Please, enter number 1-6 only.')

    if select == 1:
        vacc.append('sinovac')
    elif select == 2:
        vacc.append('astrazeneca')
    elif select == 3:
        vacc.append('johnson&johnson')
    elif select == 4:
        vacc.append('moderna')
    elif select == 5:
        vacc.append('sinopharm')
    elif select == 6:
        vacc.append('pfizer')
    else:
        print('Please, enter number 1-6 only.')

    d = input('Date: ')
    date.append(d)

# add data to object
std = Student(name,id,age,weigth,heigth)
v = [] # list of vaccine object
for x in vacc:
    v.append(Vaccine(x))

std_vac = Vaccinated(std)
for x in v:
    std_vac.add_vaccinated(x)
for x in date:
    std_vac.add_date(x)

std_vac.vaccinated_detail()
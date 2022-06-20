"""
name: {irfan teh}
id: {364211760046}
group: {MIT212}
"""



class Student():
    def __init__(self, name, id, age, weigth, height):
        # object attributes
        self.__name = name
        self.__id = id
        self.__age = age
        self.__weigth = weigth
        self.__heigth = height

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
        return self.__weigth

    def set_weight(self, weigth):
        self.__weigth = weigth

    def get_heigth(self):
        return self.__heigth

    def set_hegith(self, heigth):
        self.__heigth = heigth

    def student_detail(self):
        print(f'STD Name: {self.__name}\n'
                  f'ID: {self.__id}\n'
                  f'Age: {self.__age}\n'
                  f'Weight: {self.__weigth}\n'
                  f'Height: {self.__heigth}\n')

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
        # count = 1
        # for v,d in self.vaccinated,self.date:
        #     # print(f'\tvaccine {count}: {v.get_vaccine()} date: {d}')
        #     # count+=1
        #     print(v.get_vaccine())
        #     print(d)

        for i in range(len(self.vaccinated)):
            print(f'\tvaccine {i+1}: {self.vaccinated[i].get_vaccine()} date: {self.date[i]}')


S = input('Student Name?: ')
I = int(input('ID?:'))
A = int(input('Age?: '))
W = float(input('Weight?: '))
H = int(input('Height?: '))
vac = int(input('How many your vaccinated ? : '))
date = []


print(f'which vaccine: ')
print("\t1.sinovac")
print("\t2.astrazeneca")
print("\t3.johnson/johnson")
print("\t4.moderna")
print("\t5.sinopharm")
print("\t6.pfizer")
print('Please, enter number 1-6 only.')
s1 = int(input('select: '))
d1 = input('Date(dd/mm/yyyy): ')
print('1.sinovac')
print('2.astrazeneca')
print('3.johnson&johnson')
print('4.moderna')
print('5.sinopharm')
print('6.pfizer')
s2 = int(input('select: '))
d2 = input('Date(dd/mm/yyyy): ')



1,input('1.sinovac')
2,input('2.astrazeneca')
3,input('3.johnson&johnson')
4,input('4.moderna')
5,input('5.sinopharm')
6,input('6.pfizer')
num = (1,2,3,4,5,6)

print('Student Infomation: ')
print('Student Name: ',S)
print('Age: ',A)
print('Weight: ',W)
print('vaccine 1: ',s1,num,'date: ',d1)
print('vaccine 1: ',s1,num,'date: ',d1)
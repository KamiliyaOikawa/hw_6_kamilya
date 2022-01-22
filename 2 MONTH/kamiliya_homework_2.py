# Наследование
class Employee:
    def __init__(self, name, age, experience, marriage_status, salary):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name is string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age is integer')
        if isinstance(experience, float):
            self.experience = experience
        else:
            raise ValueError('Experience ia float')
        if isinstance(marriage_status, bool):
            self.mar_st = marriage_status
        else:
            raise ValueError('Marriage status is boole')
        if isinstance(salary, int):
            self.salary = salary
        else:
            raise ValueError('Salary is integer')

    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Age:{self.age}\n' \
               f'Experience:{self.experience}\n' \
               f'Marriage status:{self.mar_st}\n' \
               f'Salary:{self.salary}$ в неделю\n'


employee_2 = Employee('Anton', 18, 0.4, True, 500)
employee_1 = Employee('George', 30, 5.0, False, 1700)


# print(employee_2)
# print(employee_1)


class Manager(Employee):
    def __init__(self, name, age, experience, marriage_status, salary, spetsializatsiya, vine):
        super().__init__(name, age, experience, marriage_status, salary)
        if isinstance(spetsializatsiya, str):
            self.spetsializatsiya = spetsializatsiya
        else:
            raise ValueError('Spetsializatsiya is string ')
        if isinstance(vine, str):
            self.vine = vine
        else:
            raise ValueError('Vine is string')

    def __str__(self):
        return super(Manager, self).__str__() + f'Spetsializatsiya:{self.spetsializatsiya}\n' \
                                                f'Vine:{self.vine}\n' \



manager_1 = Manager('Katy', 22, 1.7, False, 2500, 'бугалтерий', 'Middle')

# print(manager_1)


class Boss(Manager):
    def __init__(self, name, age, experience, marriage_status, salary, spetsializatsiya, vine, company, privilege):
        super().__init__(name, age, experience, marriage_status, salary, spetsializatsiya, vine)
        if isinstance(company, bool):
            self.company = company
        else:
            raise ValueError('Company is boole')
        if isinstance(privilege, str):
            self.privilege = privilege
        else:
            raise ValueError('privilege is string')

    def __str__(self):
        return super(Boss, self).__str__() + f'Company:{self.company}\n' \
                                             f'privilege:{self.privilege}\n'


boos_1 = Boss('Oikawa', 27, 5.6, True, 5000, 'top management', 'Boss company Haikyu', True, 'Есть и еще какие')


# print(boos_1)


# Инкапсуляция
class Security:
    def __init__(self, name, kode_password):
        self.name = name  # имя работника
        self.__kode = kode_password  # это индивидуальный код который принадлежит сотруднику, прошу не трогать

    def _name(self):
        print(self.name)

    def __password1(self):
        pass


security_1 = Security('Dan', 123456)


# print(security_1.name)

# Полиморфизм без наследования
class People:
    def __init__(self, name, age, marriage_status, place_of_residence, salary):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name is string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age is integer')
        if isinstance(marriage_status, bool):
            self.mar_st = marriage_status
        else:
            raise ValueError('Marriage status is boole')
        if isinstance(place_of_residence, str):
            self.place = place_of_residence
        else:
            raise ValueError('Place of residence is string')
        if isinstance(salary, int):
            self.salary = salary
        else:
            raise ValueError('Salary is integer')

    def profession(self):
        return f'он безработен'

    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Age:{self.age}\n' \
               f'Marriage status:{self.mar_st}\n' \
               f'Place of residence:{self.place}\n' \
               f'Salary:{self.salary}$ \n'


name_1 = People('Ю Сын Хо', 20, False, 'Тыныстанова 110/2', 0)


# print(name_1.profession())
# print(name_1)

class Fireman(People):

    def profession(self):
        return f'Он работает пожарным'


name_2 = Fireman("Андрей", 23, False, "Киевская 159", 3000)


# print(name_2)
# print(name_2.profession())

class Doctor(People):

    def profession(self):
        return f'Этот человек работает врачом'


name_3 = Doctor("Уэнояма", 24, True, "7 микр 4 дом ", 6000)


# print(name_3)
# print(name_3.profession())

# Полиморфизм с наследованием
class Creature:
    def __init__(self, name, legs, predator):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name is string')
        if isinstance(legs, int):
            self.leg = legs
        else:
            raise ValueError('Legs is integer')
        if isinstance(predator, bool):
            self.predator = predator
        else:
            raise ValueError('Predator is boole')

    def move(self):
        return f'Он ходит {self.leg} ногами\n'

    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Legs:{self.leg}\n' \
               f'Predator:{self.predator}\n'


creature_1 = Creature('People', 2, True)


# print(creature_1)


class Birth(Creature):
    def __init__(self, name, legs, predator, color):
        super().__init__(name, legs, predator)
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color is string')

    def move(self):
        return f'Данная птица умеет и лететь и ходить\n'

    def __str__(self):
        return super(Birth, self).__str__() + f'Color:{self.color}\n'


birth = Birth('Орёл', 2, True, 'White')


# print(birth)
# print(birth.move())

class NonFlyingBirds(Birth):
    def __init__(self, name, legs, predator, color, homemade):
        super().__init__(name, legs, predator, color)
        if isinstance(homemade, bool):
            self.home = homemade
        else:
            raise ValueError('Homemade is boole')

    def move(self):
        return f'данная птица умеет только передвигатся {self.leg}лапками'

    def __str__(self):
        return super(NonFlyingBirds, self).__str__() + f'homemade:{self.home}\n'


birth_1 = NonFlyingBirds('Курица', 2, False, 'brown', True)
# print(birth_1)
# print(birth_1.move())

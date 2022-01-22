# Задание № 2 Множественное Наследование ( Один ко многим )
class People:
    def __init__(self, name, age, marriage_status, kids, alcohol_addiction, experience, salary):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name is string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age is integer')
        if isinstance(marriage_status, bool):
            self.status = marriage_status
        else:
            raise ValueError('Marriage status is boole')
        if isinstance(kids, bool):
            self.kids = kids
        else:
            raise ValueError('Kids is boole')
        if isinstance(alcohol_addiction, bool):
            self.alcohol = alcohol_addiction
        else:
            raise ValueError('Alcohol addiction is bool')
        if isinstance(experience, float):
            self.experience = experience
        else:
            raise ValueError('Experience is float')
        if isinstance(salary, int):
            self.salary = salary
        else:
            raise ValueError('Salary is integer')

    def life(self):
        return f'этот человек по имени {self.name}живет обычной жизнью, работает, на данный момент он в {self.status}  браке'

    def die(self):
        return f'это {self.name} ему на данный момент{self.age}, но примерно в {self.age + 40} он хотел бы выйти на пенсию и дожить свои последние деньки'

    def __str__(self):
        return f'Name:{self.name}\n' \
               f'Age:{self.age}\n' \
               f'Marriage status:{self.status}\n' \
               f'Alcohol addiction:{self.alcohol}\n' \
               f'Experience:{self.experience}\n' \
               f'Salary:{self.salary}$\n' \
               f'Kids:{self.kids}\n'


people = People('Esen', 22, False, True, True, 1.4, 2500)
print(people)
print(people.die())

class Fireman(People):
    def __init__(self, name, age, marriage_status, kids, alcohol_addiction, experience, salary):
        super().__init__(name, age, marriage_status, kids, alcohol_addiction, experience, salary)

    def fire(self):
        return f'Это {self.name}, о он потушил много пожаров'

    def alcohol_add(self):
        if self.alcohol == True:
            return f'это {self.name}, он зависим от алкоголя уже неопределенное количество времени , ему тежело ведь он работает 24/7 спасателем и повидал не мало смертей  '
        else:
            pass

    def __str__(self):
        return super(Fireman, self).__str__()


fireman = Fireman('Dan', 26, False, False, True, 5.6, 4000)
print(fireman.fire())
print(fireman)
print(fireman.alcohol_add())


class Doctor(People):
    def __init__(self, name, age, marriage_status, kids, alcohol_addiction, experience, salary):
        super().__init__(name, age, marriage_status, kids, alcohol_addiction, experience, salary)

    def people(self):
        return f'Это спасатель по имени {self.name} , спас хорошее количество жизней, и не успел немного....'

    def marriage(self):
        if self.status == True:
            return f'это {self.name}, и он женат но из-за того что он работает спасателем они с его второй половинкой не часто видятся и от этого ему грустно, но они все равно любят друг друга , пытаются видятся хотя бы во время перерыва '
        else:
            return f'это {self.name}, и он не в браке и все из-за того что он посвятил всю свою жизнь спасанию чужих жизней а не своей и любви, теперь же он страдает от одиночества, но скрывает это под маской ,ведь знает что ему все равно надо на работу и он с улыбкой должен помогать людям'

    def __str__(self):
        return super(Doctor, self).__str__()


doctor_2 = Doctor('Jom', 30, False, False, True, 10.5, 15000)
doctor_1 = Doctor('Tobio', 26, True, True, False, 5.2, 10000)
print(doctor_1)
print(doctor_2.die())
print(doctor_2.marriage())
print(doctor_2)
print(doctor_1.people())


class MCS(Fireman, Doctor):
    def __init__(self, name, age, marriage_status, kids, alcohol_addiction, experience, salary):
        super().__init__(name, age, marriage_status, kids, alcohol_addiction, experience, salary)

    def exp(self):
        return f'{self.name} он работает в мчс и уже служит спасению народу {self.experience} лет'

    def kid(self):
        if self.kids == True:
            return f'Это спасатель {self.name} и у него есть дети и он сильно их любит но из-за его работы видятся они не часто но он все равно продолжает их любить и старается быть для них хороим отцом  '
        else:
            pass

    def __str__(self):
        return super(MCS, self).__str__()


mcs = MCS(name='Ushidjima', age=27, marriage_status=False, kids=True, alcohol_addiction=False, experience=5.5,
          salary=5000)
# print(mcs)
# print(mcs.life())
# print(mcs.exp())
# print(mcs.kid())

#Задание № 2 Множественное Наследование ( Один ко многим )
class Sport:
    def __init__(self, name, age, height, growth, experience, form, team, inventory):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name is string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age is integer')
        if isinstance(height, float):
            self.height = height
        else:
            raise ValueError('Height is float')
        if isinstance(growth, float):
            self.growth = growth
        else:
            raise ValueError('growth is float')
        if isinstance(experience, float):
            self.exp = experience
        else:
            raise ValueError('Experience is float')
        if isinstance(form, str):
            self.form = form
        else:
            raise ValueError('Form is string')
        if isinstance(team , int):
           self.team = team
        else:
            raise ValueError('Team is integer')
        if isinstance(inventory, str):
            self.inventory = inventory
        else:
             raise ValueError('Inventory is string')

    def body(self):
      return f'это {self.name}, и он весет{self.height} и его рост состовляет {self.form}м, и его тело находится в хорошем телосложений '

    def comand(self):
        return f'он находится в команде из {self.team} человек'

    def __str__(self):
       return f'Name:{self.name}\n' \
              f'Age:{self.age}\n' \
              f'Height:{self.height}\n' \
              f'Growth:{self.growth}\n' \
              f'Experience:{self.exp}\n' \
              f'Form:{self.form}\n' \
              f'Team:{self.team}\n' \
              f'Inventory:{self.inventory}\n'


sport_1 = Sport('Suna', 25, 80.0, 1.80, 10.2, 'Black', 10, 'volleyball ball')
print(sport_1)
print(sport_1.body())

class ValleyBall(Sport):
    def __init__(self, name, age, height, growth, experience, form, team, inventory, position, comanda ):
        super().__init__(name, age, height, growth, experience, form, team, inventory)
        if isinstance(position, str):
            self.position = position
        else:
            raise ValueError('Position is string')
        if isinstance(comanda, str):
            self.comanda = comanda
        else:
            raise ValueError('Comanda is string')

    def jump(self):
        if self.growth == 160.0:
            return f'Это {self.name} , и его прыжок (а если быть точнее самая вышая точка прыжка) равна {self.growth + 100}'
        else:
            return f'Это {self.name} , и его прыжок (а если быть точнее самая вышая точка прыжка) равна {self.growth + 130}'

    def comanda_name(self):
        return f'Наш {self.name} , занимает позицию {self.position}  в команде{self.comanda}'

    def __str__(self):
        return super(ValleyBall, self).__str__() + f'Position:{self.position}\n' \
                                                   f'Comanda:{self.comanda}\n'


vall = ValleyBall('Oikawa', 27, 82.3, 190.0, 12.8, 'Blue', 12, 'volleyball ball', 'Setter', 'Aoba-Josai')
print(vall)
print(vall.comanda_name())
print(vall.jump())


class Football(Sport):

    def foot(self, foot):
        return f'{self.name} его рост {self.growth} , и размер ноги {foot}'

    def speed(self, speed):
        return f'его удар по {self.inventory} достигает до {speed}км/мин'

    def __str__(self):
        return super(Football, self).__str__()

football =Football('Deku', 29, 79.4, 180.0, 7.0, 'green', 25, 'Football ball')
print(football)
print(football.foot(45))
print(football.speed(120))


class Tennis(Sport):
    def __init__(self, name, age, height, growth, experience, form, team, inventory):
        super().__init__(name, age, height, growth, experience, form, team, inventory)

    def play(self):
        return f'Теннис который играет {self.name} является командным и в нее входят человека {self.team}, и они играют {self.inventory}'

    def game(self):
        return f'это {self.name}, и он занимается тенисом {self.exp}, и его формой является {self.form} ведь ему нравится этот цвет'

    def __str__(self):
        return super(Tennis, self).__str__()


tennis = Tennis('Eren', 22, 79.0, 185.0, 9.10, 'White-Red', 2, 'Tennis ball, racket')
print(tennis)
print(tennis.play())
print(tennis.game())



# Задание № 3 Магические методы
class Kino:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.cost + other

    def __str__(self):
        return f'Название: {self.name}\n' \
               f'Цена: {self.cost}\n'


movie1 = Kino(name='Наруто', cost=350)

movie2 = Kino(name='Блич', cost=500)

movie3 = Kino(name='Ходячий замок', cost=200)


print(movie1)
print(f'Фильм в 3D формате будет стоить: {movie1.__add__(50)}')
print(movie2)
print(f'Фильм в 3D формате будет стоить: {movie2.__add__(50)}')
print(movie3)
print(f'Фильм в 3D формате будет стоить: {movie3.__add__(50)}')



class Starbucks:
    def __init__(self, *name):
        self.name = []
        for k in name:
            self.name.append(k)

    def __len__(self):
        return len(self.name)

    def write_name(self):
        print("Имя на кофе")
        for name in self.name:
            if (len(name) >= 9):
                print(name, " - ", name[0:5])
            elif (len(name) >= 5):
                print(name, " - ", name[0:8])
            elif (len(name) == 5):
                print (name, '-', name[0:5])
            elif (len(name) <= 5):
                print(name, "-", name[0:3])

            else:
                print(name, " - ", name)


names = Starbucks("Oikawa", "Ramiliya", "Pony", "Aman", "Adilet")

print(len(names))
names.write_name()


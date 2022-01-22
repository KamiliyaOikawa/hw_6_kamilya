class Animal:
    def __init__(self, name, predators, habitat, heart, growth, ):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name should be integer')
        if isinstance(predators, bool):
            self.predators = predators
        else:
            raise ValueError('Predators should be bool')
        if isinstance(habitat, str):
            self.habitat = habitat
        else:
            raise ValueError('Habitat should be integer')
        if isinstance(heart, int):
            self.heart = heart
        else:
            raise ValueError('Heart should be string')
        if isinstance(growth, float):
            self.growth = growth
        else:
            raise ValueError('growth should be float')

    def __str__(self):
        return f'\nname:{self.name}\n' \
               f'predators:{self.predators}\n' \
               f'Habitat:{self.habitat}\n' \
               f'Heart:{self.heart} камерное\n' \
               f'growth:{self.growth} сантиметров'


class Mammals(Animal):
    def __init__(self, name, predators, habitat, heart, growth, wool, color, horns):
        super().__init__(name, predators, habitat, heart, growth)
        if isinstance(wool, bool):
            self.wool = wool
        else:
            raise ValueError('Wool should be bool')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string')
        if isinstance(horns, bool):
            self.horns = horns
        else:
            raise ValueError('horns should be bool')

    def __str__(self):
        return super(Mammals, self).__str__() + f'\nwool:{self.wool}\n' \
                                                f'color:{self.color}\n' \
                                                f'horns:{self.horns}\n'


animal_1 = Mammals('слон', False, 'Африка', 5, 5.00, False, 'серый', False)
print(animal_1)
animal_2 = Mammals('волк', True, 'В горах', 5, 0.90, True, 'серый', False)
print(animal_2)
animal_3 = Mammals('кошка', False, 'дома', 5, 0.25, True, 'белый', False)
print(animal_3)
animal_4 = Mammals('корова', False, 'на ферме', 5, 1.40, False, 'черно-белый', True)
print(animal_4)


class Reptiles(Animal):
    def __init__(self, name, predators, habitat, heart, growth, squama, poisonous):
        super().__init__(name, predators, habitat, heart, growth)
        if isinstance(squama, bool):
            self.squama = squama
        else:
            raise ValueError('Squama should be bool')
        if isinstance(poisonous, bool):
            self.poisonous = poisonous
        else:
            raise ValueError('poisonous should be bool')

    def __str__(self):
        return super(Reptiles, self).__str__() +'\nscales:{self.squama}\n' \
                                               f'poisonous:{self.poisonous}\n'


animal_5 = Reptiles('Среднеазиатская черепаха', False, 'Средняя азия ', 3, 0.20, False, False)
print(animal_5)
animal_5 = Reptiles('Нильский крокодил', True, 'Арика', 3, 4.5, False, False)
print(animal_5)
animal_5 = Reptiles('Йменский Хамелион', False, 'Средне', 3, 0.60, True, False)
print(animal_5)
animal_5 = Reptiles('Кобра', True, 'Юо Восточная Азия', 3, 3.2, True, True)
print(animal_5)

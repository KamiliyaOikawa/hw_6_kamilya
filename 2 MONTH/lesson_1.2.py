class Phone:
    def __init__(self, number, camera, screen, CPU, memory, flash):
        if isinstance(number, str):
            self.number = number
        else:
            raise ValueError('Number should be string')
        if isinstance(camera, float):
            self.camera = camera
        else:
            raise ValueError('Camera should be float')
        if isinstance(CPU, float):
            self.CPU = CPU
        else:
            raise ValueError('CPU should be float')
        if isinstance(screen, bool):
            self.screen = screen
        else:
            raise ValueError('screen should be bool')
        if isinstance(memory, int):
            self.memory = memory
        else:
            raise ValueError('Memory should be integer')
        if isinstance(flash, bool):
            self.flash = flash
        else:
            raise ValueError('Flash should be bool')

    def __str__(self):
        return f'Number:{self.number}\n' \
               f'Camera:{self.camera}\n' \
               f'Screen:{self.screen}\n' \
               f'CPU:{self.CPU}\n' \
               f'Memory:{self.memory}\n' \
               f'Flash:{self.flash}\n'


nokia_6300 = Phone('+996666321', 1.2, False, 0.7, 512, True)

print(nokia_6300)


class Iphone(Phone):
    def __init__(self, number, camera, screen, CPU, memory, flash, ecosystem, fame, icloud):
        super().__init__(number, camera, screen, CPU, memory, flash)
        if isinstance(ecosystem, bool):
            self.eco = ecosystem
        else:
            raise ValueError('Ecosystem is bool')
        if isinstance(fame, str):
            self.fame = fame
        else:
             raise ValueError('Fame is string')
        if isinstance(icloud, int):
            self.icloud = icloud
        else:
            raise ValueError('Icloud is integer') 

    def __str__(self):
        return super(Iphone, self).__str__() + f'Ecosystem: {self.eco}\n' \
                                               f'Fame:{self.fame}\n' \
                                               f'Icloud:{self.icloud}\n'


iphone_1 = Iphone('+996666321', 16.0, True, 2.4, 512, True, True, 'This is Iphone', icloud=32)
print(iphone_1)

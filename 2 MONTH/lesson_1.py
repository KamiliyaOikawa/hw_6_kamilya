class Car:
    def __init__(self, brand, model, engine, fuel, color, passegers_quantity, price):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.fuel = fuel
        self.color = color
        self.pass_q = passegers_quantity
        self.price = price

        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string')
        if isinstance(model, str):
            self.model = model
        else:
            raise ValueError('Model should be string')
        if isinstance(engine, str):
            self.engine = engine
        else:
            raise ValueError('Engine should be string')
        if isinstance(fuel, float):
            self.fuel = fuel
        else:
            raise ValueError('Fuel should be float')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string')
        if isinstance(passegers_quantity, int):
            self.pass_q = passegers_quantity
        else:
            raise ValueError('Passeder quantity should be integer')
        if isinstance(price, int):
            self.price = price
        else:
            raise ValueError('Price should be integer')

    def tunning(self, price_t):
        total = self.price + price_t
        return f'{total}'

    def __str__(self):
        return f'Brand: {self.brand}\n' \
               f'Model:{self.model}\n' \
               f'Engine:{self.engine}\n' \
               f'Fuel:{self.fuel}\n' \
               f'Color:{self.color}\n' \
               f'P_Q:{self.pass_q}\n' \
               f'Price:{self.price}$\n '


car_1 = Car(brand="Mercedes", model="S-class 340", engine="Germany",
            fuel=5.0, color='black', passegers_quantity=5, price=50000)
car_2 = Car(brand="Lexus", model="570", engine="Katana",
            fuel=5.7, color='silver', passegers_quantity=8, price=13478)

print(car_1.tunning(654))
print(car_1)
print(car_2)

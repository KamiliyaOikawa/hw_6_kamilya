from .kamiliya_homework_2 import security_1

class CustomUser:
    def __init__(self, user_name, first_name, last_name, email, password, age, gender, phone, secret_key):
        if isinstance(user_name, str):
            self.user = user_name
        else:
            raise ValueError('User name is string')
        if isinstance(first_name, str):
            self.first = first_name
        else:
            raise ValueError('First name is string')
        if isinstance(last_name, str):
            self.last = last_name
        else:
            raise ValueError('Last name is string')
        if isinstance(email, str):
            self.email = email
        else:
            raise ValueError('Email is string')
        if isinstance(password, str):
            self.password = password
        else:
            raise ValueError('Password is string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('age is integer')
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('Gender is string')
        if isinstance(phone, int):
            self.phone = phone
        else:
            raise ValueError('phone is ineger')
        if isinstance(secret_key, str):
            self.secret = secret_key
        else:
            raise ValueError('Secret key is string')

    def __str__(self):
        return f'User name:{self.user}\n' \
               f'First name:{self.first}\n' \
               f'last name:{self.last}\n' \
               f'Email:{self.email}\n' \
               f'Password:{self.password}\n' \
               f'Age:{self.age}\n' \
               f'Gender:{self.gender}\n' \
               f'Phone:{self.phone}'

#class Admin(CustomUser)



class VIP(CustomUser):
    def __init__(self, user_name, first_name, last_name, email, password, age, gender, phone, secret_key):
        super().__init__(user_name, first_name, last_name, email, password, age, gender, phone, secret_key)

    def __str__(self):
        return super(VIP, self).__str__()

class SuperUser(CustomUser, VIP):
    def __init__(self)

sup_user =
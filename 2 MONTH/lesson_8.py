import sqlite3
from random import randint

database_1 = sqlite3.connect("server.sqlite3")
sq_l = database_1.cursor()

sq_l.execute(
    """CREATE TABLE IF NOT EXISTS users (
    login TEXT, 
    password TEXT,
    cash INT
    )
    """
)
database_1.commit()


def register_user():
    global user_login, user_password, balance
    user_login = input('Login')
    user_password = input('password')
    numbers = randint(1, 2)

    for i in sq_l.execute(f"SELECT login FROM users WHERE login'{user_login}'"):
        balance = i[0]

    sq_l.execute(f"SELECT login FROM users WHERE login'{user_login}'")
    if sq_l.fetchone() is None:
        sq_l.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, 0))
        print('User reqisterend')
        for value in sq_l.execute('SELECT login FROM users'):
            print(value)
    else:
        print('You lose')
        for value in sq_l.execute('SELECT 8 FROM users')


if __name__ == "__main__":
     register_user()

# sq_l.execute(f'INSERT INTO users WHERE login'{user_login}'")

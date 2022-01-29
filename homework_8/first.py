import sqlite3

data_base = sqlite3.connect("testdb.sqlite3")
t = data_base.cursor()

t.execute("""CREATE TABLE IF NOT EXISTS users(
    time TEXT,
    events TEXT
    )
    """
          )


def register_events():
    global time, events
    time = input('Время')
    events = input('Событие')

    t.execute(f"SELECT events FROM users WHERE events'{events}'")
    if t.fetchone() is None:
        t.execute(f"INSERT INTO users VALUES (?,?)", (time, events))
        print('Events reqisterend')


if __name__ == "__main__":
    register_events()

import sqlite3
d_b = sqlite3.connect("Plan.db")
sql = d_b.cursor()
sql.execute(
    """CREATE TABLE IF NOT EXISTS users
    (Day TEXT,
    Morning TEXT,
    Lunch TEXT,
    Evening TEXT)"""
)
d_b.commit()


def registr():
    global day_week, plan_morning, plan_lunch, plan_evening
    while True:
        day_week = input('What day of the week:')
        plan_morning = input('What are your plans for the morning:')
        plan_lunch = input('What are your lunch plans:')
        plan_evening = input('What are your plans for the evening: ')

        sql.execute(f"SELECT Day FROM users WHERE DAY = '{day_week}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?,?,?,?)",
                        ( day_week, plan_morning, plan_lunch, plan_evening))
            d_b.commit()
            for value in sql.execute("SELECT * FROM users"):
                print(value)
        else:
            print("The day of the week should not be repeated!")
            for value in sql.execute("SELECT * FROM users"):
                print(value)
        delete_choose = input("Do you have any fulfilled days?"
                              "If there is, then write the day of the week, if not, then write no:")
        sql.execute("DELETE FROM users WHERE Day == ?", (delete_choose,))
        if delete_choose != "нет":
            for value in sql.execute("SELECT * FROM users"):
                print(value)
            continue
        choose = input("Do you want to continue recording your plans? Yes or no")
        if choose == "Yes":
            continue
        elif choose == "No":
            for value in sql.execute("SELECT * FROM users"):
                print(value)
            print("Your plans are registered!")
            break
        else:
            print("Write only yes or no")

            break


if __name__ == '__main__':
    registr()



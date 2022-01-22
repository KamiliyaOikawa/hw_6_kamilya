class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds

    def times(self):
        days = int(self.seconds / (24 * 60 * 60))
        self.seconds -= days * 24 * 60 * 60
        hours = int(self.seconds / 60 / 60)
        self.seconds -= hours * 60 * 60
        minutes = int(self.seconds / 60)
        self.seconds -= minutes * 60

        return f'{days} days, {hours} hours, {minutes} minutes, {self.seconds} seconds'

    def show_me_the_time(self):
        oikawa = int(input('Введите секунды:'))
        a = TimeDesk(oikawa)
        return a.times()

    def str(self):
        return f'Seconds: {self.seconds}/n'


tobio = TimeDesk(70)
print(tobio.show_me_the_time())

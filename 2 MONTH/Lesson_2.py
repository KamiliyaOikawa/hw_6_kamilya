# golang

class Junior:
    def __init__(self, prog_lang, laptop, style, experience, salary):
        if isinstance(prog_lang, str):
            self.lang = prog_lang
        else:
           raise ValueError('Proramming language is string')
        if isinstance(laptop, bool):
            self.laptop = laptop
        else:
            raise ValueError('Laptop  is bool')
        if isinstance(style, str):
            self.st = style
        else:
            raise ValueError('Style language is string')
        if isinstance(experience, float):
            self.e = experience
        else:
            raise ValueError('Ex  is Float')
        if isinstance(salary, int):
            self.salary = salary
        else:
            raise ValueError('salary is integer')

    def can_copy_paste(self, source):
        return f'Can copy and paste from {source}, style is{self.st}'

    def __str__(self):
        return f'Programming Languege:{self.lang}\n' \
               f'Laptop:{self.laptop}\n' \
               f'Style:{self.st}\n' \
               f'experience:{self.e}\n' \
               f'Salary:{self.salary}$'

junior_1 = Junior('Java', True, 'awful', 0.5, 250)
junior_2 = Junior('Python', True, 'good', 0.5, 300 )

print(junior_2)
print(junior_1.can_copy_paste('Google'))
print(junior_1)
print(junior_2.can_copy_paste('StackOverFlow'))
#__ только спереди для защиты
class Middle(Junior):
    def __init__(self, prog_lang, laptop, style, experience, salary, responsibility):
        super().__init__(prog_lang, laptop, style, experience, salary)
        if isinstance(responsibility, bool):
            self.r = responsibility
        else:
            raise ValueError('responsibility is bool')

    def can_be_mentor(self, junior):
        return  f'Can help {junior}'

    def can_hangle_pr(self, project):
        return f'can hangle fully project, project name is {project}'

    def __str__(self):
        return super(Middle, self).__str__() + f'responsibility:{self.r}'





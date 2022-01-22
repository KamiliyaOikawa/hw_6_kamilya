class Chapter:
    def __init__(self, name, height, skill):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name is string')
        if isinstance(height, int):
            self.h = height
        else:
            raise ValueError('Height is integer')
        if isinstance(skill, str):
            self.skill = skill
        else:
            raise ValueError('Skill is string')


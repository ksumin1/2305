class Person:
    def __init__(self, name, music):
        self.name = name
        self.music = music

    def __str__(self):
        return f'이름: {self.name}\t좋아하는 음악: {self.music}'

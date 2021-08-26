class Entertainer:
    def __init__(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height

    def set_face(self, face):
        self.face = face

    def set_kind(self, kind):
        self.kind = kind

    def set_name(self, name):
        self.name = name

    # def info(self):
    #     print(f'이름: {set_name()}\t키: {self.name}\t얼굴: {self.face}\t인성: {self.kind}')
    def __str__(self):
        return f'이름 : {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}'

아이유 = Entertainer('아이유')
아이유.set_name('이지은')
아이유.set_height('161cm')
아이유.set_face("이상형")
아이유.set_kind('That\'s very good')
print(아이유)

class Singer(Entertainer):
    def __init__(self, name, song):
        super().__init__(name) # self.name = name
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t대표곡 :{self.song}'

뷔 = Singer('뷔', 'Love Maze') # 파이썬은 new연산자가 없다
뷔.set_height('179cm')
뷔.set_face('진이지 이상형')
뷔.set_kind('That\'s very good and cute.')
print(뷔)

RM = Singer('RM', 'Answer: love myself')
RM.set_height('179cm')
RM.set_face('쏘쏘')
RM.set_kind('자기철학이 있어보임')
print(RM)


class Talent(Entertainer):
    def __init__(self,name, drama):
        super().__init__(name)
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'
    
주단탱 = Talent('주단태', '팬트하우스')
주단탱.set_height('180?cm')
주단탱.set_face('사실 이름만 알고있다..!')
주단탱.set_kind('ㅇ.ㅇ')
print(주단탱)

방탄소년단 = []
방탄소년단.append(뷔)
방탄소년단.append(RM)
print(방탄소년단)

class Icecream:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor
        #이름:  name 맛:flavor,설명:description

    def set_description(self, description):
        self.set_description = description

    def __str__(self):
        return f'이름: {self.name} \t맛: {self.flavor}'


슈팅스타 = Icecream("슈팅스타", "말랑캔디?, 체리시럽")
슈팅스타.set_description("톡톡튀기는 맛")

엄마는외계인 = Icecream("엄마는외계인", "초코")

블랙소르베 = Icecream("블랙소르베", "레몬, 라임")

class Cup:
    _CUP_CATEGORIES = ['싱글컵', '더블컵', '파인트']
    _PRICES = [4000, 6200, 8200]


    def __init__(self, name, price, count_flavor):
        self.name = name
        self.price = price
        self.count_flavor = count_flavor
        self.price = Cup._PRICES[self.count_flavor]
        self.menu = []
        self.add_menu()
        self.order_menu = []

    def add_menu(self):
        슈팅스타 = Icecream("슈팅스타", "말랑캔디?, 체리시럽")
        슈팅스타.set_description("톡톡튀기는 맛")

        엄마는외계인 = Icecream("엄마는외계인", "초코")

        블랙소르베 = Icecream("블랙소르베", "레몬, 라임")

        self.menu.append(슈팅스타)
        self.menu.append(엄마는외계인)
        self.menu.append(블랙소르베)

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(index + 1, icecream)
    def order_menu(self):
        for n in range(self.count_flavor):
            self.show_menu()                    # 메뉴 보여주기
            flavor = input('맛을 고르세요: ')     # 사용자 선택
            flavor = int(flavor)                # 인덱스사용 문자 -> 숫자
            icecream = self.menu[flavor -1]
            self.order_menu.append(icecream)    # 주문한 메뉴추가
        print('주문한 아이스크림입니다.')
        for icecream in self.order_menu():      # 주문내역
            print(icecream)

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t종류: {Cup._CUP_CATEGORIES[self.count_flavor -1]}'

이지꺼 = Cup('더블컵', 6200, 2)
print(이지꺼)
이지꺼.show_menu()
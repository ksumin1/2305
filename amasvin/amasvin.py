class Drink:
    _CUPS = ('레귤러', '정보')
    _ICES = ('0%', '50%', '100%', '150%')
    _SUGARS = ('0%', '50%', '100%', '150%')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0  # Drink._CUPS[0]
        self.ice = 2  # Drink._ICES[2]
        self.sugar = 3  # Drink._SUGARS[2]

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):
            print(f'{index + 1}: {cup}')
        cup = input('컵사이즈를 선택하세요: ')
        if cup == '':
            self.cup = 0
        else:
            cup = int(cup) - 1
            self.cup = cup
        if self.cup == 1:
            self.price += 500
            self.set_ice()

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):
            print(f'{index + 1}: {ice}')
        ice = input('얼음량을 선택하세요: ')
        self.ice = 2 if ice == '' else int(ice) - 1
        # if ice == '':
        #     self.ice = 2
        # else:
        #     self.ice = int(ice) -1

    def set_sugar(self):
        for index, sugar in enumerate(Drink._SUGARS):
            print(f'{index + 1}: {sugar}')
        sugar = input('당도를 선택하세요: ')
        self.sugar = 2 if sugar == '' else int(sugar) - 1

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}\t당도: {Drink._SUGARS[self.sugar]}'



class Coffee(Drink):
    pass


class Bubbletea(Drink):

    _PEARL = ("타피오카", '코코', "젤리", "알로에")
    def __init__(self, name, price):
        super().__init__(name, price)
        self.pearl = 0 # Bubbletea._PEARL[0]


    def set_pearl(self):
        for index, pearl in enumerate(Bubbletea._PEARL):
            print(f'{index + 1} : {pearl}')
        pearl = input("펄을 골라주세요: ")
        self.pearl = 0 if pearl == '' else int(pearl) - 1

    def __str__(self):
        return super().__str__() + f'\t펄: {Bubbletea._PEARL[self.pearl]}'

    def order(self):
        super().order()
        self.set_pearl()


class Order:
    def __init__(self):
        self.menu = []
        self.init_menu()
        self.order_menu = []

    def init_menu(self):
        drink1 = Coffee('아메리카노', 1000)
        drink2 = Bubbletea('하동녹차오레오', 3300)
        drink3 = Bubbletea('딸기요거트', 3400)
        self.menu.append(drink1)
        self.menu.append(drink2)
        self.menu.append(drink3)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1}: {drink.name}\t{drink.price}원')

    def order_drink(self):
        while True:
            self.show_menu()
            drink = input('메뉴를 선택하세요: ')
            drink = int(drink) - 1
            new_drink = self.menu[drink]
            new_drink.order()
            self.order_menu.append(new_drink)
            is_add = input('더 주문하실까요?(n: 끝) : ')
            if is_add == 'n':
                break
        print(self)

    def sum_price(self):
        total_price = 0
        for drink in self.order_menu:
            total_price += drink.price
        return total_price

    def __str__(self): # 주문 내역
        s = '-' * 20 + "주문 내역" + '-' * 20 + '\n'
        for drink in self.order_menu:
            s += f'{drink}\n'
        s += f'주문한 음료수 개수: {len(self.order_menu)}개'
        s += f'총 가격: {self.sum_price()}원'
        return s

order = Order()
order.order_drink()
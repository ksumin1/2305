from recepie import Recipe

class Recipebook:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self):
        recipe_name = input('>> 레시피 이름을 입력하세요: ')
        for recipe in self.recipe_list:
            if recipe_name == recipe.name:
                print('이미 존재하는 레시피입니다! ')
                return
        new_recipe = Recipe(recipe_name)
        new_recipe.set_recipe()
        self.recipe_list.append(new_recipe) # 시험범위 append함수

    def show_all_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'\n{index+1}번.')
            print(recipe)

    def search_recipe(self):
        recipe_name = input('>> 원하는 레시피를 검색하세요: ')
        searched_recipe = []
        for recipe in self.recipe_list:
            if recipe_name in recipe.name:
                print(recipe)
                searched_recipe.append(recipe)
        if len(searched_recipe) == 0:
            choice = input('>> 원하는 레시피가 없습니다. 추가하시겠습니까? (1: 예, 0: 아니오)')
            if choice == '1':
                self.add_recipe()
            else:
                return
    def search_whatin(self):
        # 재료보여주기
        whatin_set =set()
        for recipe in self.recipe_list:
            for whatin in recipe.whatin:
                whatin_set.add(whatin)

        for index, whatin in enumerate(whatin_set):
            print(f'{index + 1}, {whatin}')

        # 사용할 재료 구하기
        num = int(input('>>사용할 재료 번호를 입력하세요'))
        use_whatin = list(whatin_set)[num-1]
        # 고른 재료 출력
        for recipe in self.recipe_list:
            if use_whatin in recipe.whatin: # 딕셔너리를 키 값으로
                print(recipe)



    def __str__(self):
        pass
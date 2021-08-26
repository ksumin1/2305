from recipebook import Recipebook

def print_menu():
    print('1. 레시피 검색')
    print('2. 레시피 추가')
    print('3. 재료 검색')
    print('4. 레시피 모음')
    print('5. 종료')
    menu = input('>> 메뉴를 선택하세요: ')
    return menu

def main():
    recipebook_203 = Recipebook()
    while True:
        menu = print_menu()
        if menu == '1':
            # 레시피 검색
            recipebook_203.search_recipe()
        elif menu == '2':
            # 레시피 추가
            recipebook_203.add_recipe()
        elif menu == '3':
            recipebook_203.search_recipe()
            # 재료 검색
        elif menu == '4':
            # 레시피 모음
            recipebook_203.show_all_recipe()
        elif menu == '5':
            break
        else:
            print('다시 입력하세요.')

if __name__ == '__main__':
    main()
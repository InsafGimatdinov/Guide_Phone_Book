import user_iterface as ui
import add_user as au
import del_user as du
import search_user as su
                                                                       # Модуль логики работы программы
def botton_click():
    mode = ui.get_mode()
    if mode == 1:
        print('Режим добавления пользователей')
        au.log_csv()
    elif mode == 2:
        print('Режим поиска данных пользователя')
        su.search_info()
    elif mode == 3:
        print('Режим удаления данных пользователя')
    elif mode == 5:
        print('Режим просмотра всего справочника')
        guide = open('guide_csv.csv', 'r')
        print(*guide)
        guide.close()

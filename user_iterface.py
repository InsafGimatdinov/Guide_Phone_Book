def get_mode():
    mode = int(input('''Выберите режим работы программы:
            1 - Добавление пользователя
            2 - Просмотр данных о пользователе
            3 - Удаление пользователя
            4 - Изменение данных о пользователе                             
            5 - Просмотр справочника
            ОЖИДАНИЕ: '''))
    while mode < 1 or mode > 5:                                            # Модуль интерфейса
        mode = int(input('''ОШИБКА! Попробуйте снова:
                    1 - Добавление пользователя
                    2 - Просмотр данных о пользователе
                    3 - Удаление пользователя
                    4 - Изменение данных о пользователе
                    5 - Просмотр справочника
                    ОЖИДАНИЕ: '''))
    else:
        return mode

def get_fname():
    first_name = input('Введите имя нового пользователя: ')
    return first_name
def get_lname():
    last_name = input('Введите фамилию нового пользователя: ')
    return last_name
def get_dbirth():
    date_birth = input('Введите дату рождения нового пользователя: ')
    return date_birth
def get_pnumber():
    phone_number = input('Введите номер телефона нового пользователя: ')
    return phone_number
def get_comment():
    comment = input('Введите комментарий для нового пользователя: ')
    return comment
def del_info():
    delete = input('Введите id пользователя котолрого нужно удалить: ')
    return delete

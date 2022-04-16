import user_iterface as ui
import csv
import xml

def add_new_user():
    data = {'fname': ui.get_fname(), 'lname': ui.get_lname(), 'dbirth': ui.get_dbirth(),
            'pnumber': ui.get_pnumber(), 'comment': ui.get_comment()}
    guide = {get_id(): data}
    print('Добавление нового прользователя прошло успешно')
    return guide

def get_id():
    with open('guide_csv.csv', 'r', newline='') as f:
        id_reader = csv.reader(f)
        data = list(id_reader)
        key_id = len(data) + 1
        return key_id
                                                        # Модуль добавления пользователя и запись в файл
def log_csv():
    with open('guide_csv.csv', 'a') as f:
        result = add_new_user()
        f.write(f'{result}\n')

def log_xml():
    with open('guide_xml.xml', 'a') as f:



def search_info():
    info = input('Введите данные для поиска: ')
    with open('guide_csv.csv', 'r') as f:
        for line in f:                                 # Модуль поиска данных из файла
            if info in line:
                print(line, end=' ')
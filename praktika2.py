class Person:
    name = {}
    phone = {}
    address = {}
    job = {}
    spravochnik = {}
    
    def __init__(self):
        print('-Создание контакта-\n')
        self.name = {}
        self.phone = {}
        self.address = {}
        self.job = {}
        name_key = ['Фамилия','Имя','Отчество']
        name_value = list(input("Введите {0}:".format(name_key[i])).capitalize() for i in range(len(name_key)))
        fio = {}
        for i in range(len(name_key)):
            fio[name_key[i]] = name_value[i]
        self.name['name'] = fio
        self.phone['phone'] = input("Введите номер телефона:")
        self.address['address'] = input("Введите адрес проживания:")
        self.job['job'] = input("Введите место работы:")

class SpravochnikAdd(Person):
    def add(self):
        print('\n-Добавление контакта в справочник-\n')
        if self.spravochnik == {}:
            index = int(input("Введите номер контакта для добавления в справочник:"))
            step = 0
            while step == 0:
                if index in self.spravochnik:
                    print("Данный номер контакта уже занят")
                    index = int(input("Введите новый номер контакта для добавления в справочник:"))
                else:
                    step = 1
                    self.spravochnik[index] = [self.name, self.phone, self.address, self.job]
            return print("\nКонтакт добавлен в справочник\n")
        else:
            for i in self.spravochnik:
                if self.name == self.spravochnik[i][0] and self.phone == self.spravochnik[i][1]:
                    return print("Данный контакт уже имеется в справочнике\n")
                else:
                    print("Номера контавтов в справочнике:", self.spravochnik.keys())
                    index = int(input("Введите номер контакта для добавления в справочник:"))
                    step = 0
                    while step == 0:
                        if index in self.spravochnik:
                            print("Данный номер контакта уже занят")
                            print("Номера контавтов в справочнике:", self.spravochnik.keys())
                            index = int(input("Введите новый номер контакта для добавления в справочник:"))
                        else:
                            step = 1
                            self.spravochnik[index] = [self.name, self.phone, self.address, self.job]
                    return print("\nКонтакт добавлен в справочник\n")

class SpravochnikNoAdd(SpravochnikAdd):

    def __init__(self):
        pass

    def delete(self):
        print('\n-Удаление контакта из справочника-\n')
        if self.spravochnik == {}:
            print("Справочник пуст\n")
        else: 
            print("Номера контавтов в справочнике:", self.spravochnik.keys())
            index = int(input("Введите номер контакта для удаления из справочника:"))
            step = 0
            while step == 0:
                if index in self.spravochnik:
                    step = 1
                    print("Выбранный контакт для удаления:", self.spravochnik[index])
                    del self.spravochnik[index] 
                else:
                    print("Данный номер контакта отсутствует в справочнике")
                    print("Номера контавтов в справочнике:", self.spravochnik.keys())
                    index = int(input("Введите новый номер контакта для удаления из справочника:")) 
            return print("\nКонтакт удален из справочника\n")

    def edit(self):
        print('\n-Редактирование контакта в справочнике-\n')
        if self.spravochnik == {}:
            print("Справочник пуст\n")
        else: 
            print("Номера контавтов в справочнике:", self.spravochnik.keys())
            index = int(input("Введите номер контакта для редактирования в справочнике:"))
            step = 0
            start = 0
            while step == 0:
                if index in self.spravochnik:
                    step = 1
                    while start == 0:
                        print("Выбранный контакт для редактирования:", self.spravochnik[index])
                        print("\nВыберите, что требуется изменить:\n"
                              "1: ФИО\n"
                              "2: Номер телефона\n"
                              "3: Адрес проживания\n"
                              "4: Место работы\n"
                              "5: Выход\n")
                        start = int(input())
                        if start == 1:
                            fio_start = self.spravochnik[index][0]['name']
                            name_key = ['Фамилия','Имя','Отчество']
                            name_value = list(input("Введите {0}:".format(name_key[i])).capitalize() for i in range(len(name_key)))
                            fio = {}
                            for i in range(len(name_key)):
                                fio[name_key[i]] = name_value[i]
                            self.spravochnik[index][0]['name'] = fio
                            step = 0
                            for i in self.spravochnik:
                                if self.spravochnik[index][0]['name'] == self.spravochnik[i][0]['name'] and self.spravochnik[index][1]['phone'] == self.spravochnik[i][1]['phone'] and i != index:
                                    self.spravochnik[index][0]['name'] = fio_start
                                    print("Данный контакт уже имеется в справочнике")
                                    step = 1
                            if step == 0:
                                print("\nКонтакт отредактирован в справочнике")
                            start = 0  
                        elif start == 2:
                            phone_start = self.spravochnik[index][1]['phone']
                            self.spravochnik[index][1]['phone'] = input("Введите номер телефона:")
                            step = 0
                            for i in self.spravochnik:
                                if self.spravochnik[index][0]['name'] == self.spravochnik[i][0]['name'] and self.spravochnik[index][1]['phone'] == self.spravochnik[i][1]['phone'] and i != index:
                                    self.spravochnik[index][1]['phone'] = phone_start
                                    print("Данный контакт уже имеется в справочнике")
                                    step = 1
                            if step == 0:
                                print("\nКонтакт отредактирован в справочнике")
                            start = 0
                        elif start == 3:
                            self.spravochnik[index][2]['address'] = input("Введите адрес проживания:")
                            print("\nКонтакт отредактирован в справочнике")
                            start = 0
                        elif start == 4:
                            self.spravochnik[index][3]['job'] = input("Введите место работы:")
                            print("\nКонтакт отредактирован в справочнике")
                            start = 0
                        elif start == 5:
                            print("Выход из редактирования")
                        else:
                            print("Выберите нужный вариант\n")
                            start = 0

                else:
                    print("Данный номер контакта отсутствует в справочнике")
                    print("Номера контавтов в справочнике:", self.spravochnik.keys())
                    index = int(input("Введите новый номер контакта для редактирования в справочнике:")) 
            

    def screen(self):
        print('\n-Вывод всех контактов в справочнике на экран-\n')
        if self.spravochnik == {}:
            print("Справочник пуст\n")
        else:
            return print(self.spravochnik)

    def search(self):
        print('\n-Поиск контактов в справочнике по различным параметрам-\n')
        if self.spravochnik == {}:
            print("Справочник пуст\n")
        else:
            start = 0
            while start == 0:
                print("-Выбирете параметр поиска-\n"
                      "1: Поиск по номеру контакта в справочнике\n"
                      "2: Поиск по ФИО\n"
                      "3: Поиск по номеру телефона\n"
                      "4: Поиск по адресу проживания\n"
                      "5: Поиск по месту работы\n")
                start = int(input())

                if start == 1:
                    print("\n-Поиск по индексу-\n"
                          "Номера контавтов в справочнике:")
                    for i in self.spravochnik.keys():
                        print("{0}:".format(i), self.spravochnik[i][0]['name'])
                    index = int(input("Введите нужный номер контакта в справочнике:"))
                    step = 0
                    while step == 0:
                        if index in self.spravochnik:
                            step = 1
                            print("Контакт найден: {0}:".format(index), self.spravochnik[index])
                        else:
                            print("Данный номер контакта отсутствует в справочнике")
                            print("Номера контавтов в справочнике:", self.spravochnik.keys())
                            index = int(input("Введите нужный номер контакта в справочнике:"))

                elif start == 2:
                    print("\n-Поиск по ФИО-\n")
                    print("Все ФИО в справочнике:")
                    for i in self.spravochnik.keys():
                        print("{0}:".format(i), self.spravochnik[i][0]['name'])
                    name = {}
                    name_key = ['Фамилия','Имя','Отчество']
                    name_value = list(input("Введите {0}:".format(name_key[i])).capitalize() for i in range(len(name_key)))
                    fio = {}
                    for i in range(len(name_key)):
                        fio[name_key[i]] = name_value[i]
                    name['name'] = fio
                    step = 0
                    step_w = 0
                    while step_w == 0:
                        for i in self.spravochnik.keys():
                            if name == self.spravochnik[i][0]:
                                print("Контакт найден: {0}:".format(i), self.spravochnik[i])
                                step = 1
                                step_w = 1
                        if step == 0:
                            print("Данное ФИО отсутствует в справочнике")
                            name_key = ['Фамилия','Имя','Отчество']
                            name_value = list(input("Введите заново {0}:".format(name_key[i])).capitalize() for i in range(len(name_key)))
                            fio = {}
                            for i in range(len(name_key)):
                                fio[name_key[i]] = name_value[i]
                            name['name'] = fio           

                elif start == 3:
                    print("\n-Поиск по номеру телефона-\n")
                    print("Все номера телефонв в справочнике:")
                    for i in self.spravochnik.keys():
                        print("{0}:".format(i), self.spravochnik[i][0]['name'], self.spravochnik[i][1]) 
                    phone = {}
                    phone['phone'] = input("Введите нужный номер телефона:")
                    step = 0
                    step_w = 0
                    while step_w == 0:
                        for i in self.spravochnik.keys():
                            if phone == self.spravochnik[i][1]:
                                print("Контакт найден: {0}:".format(i), self.spravochnik[i])
                                step = 1
                                step_w = 1
                        if step == 0:
                            print("Данный номер телефона отсутствует в справочнике")
                            phone['phone'] = input("Введите заново нужный номер телефона:")

                elif start == 4:
                    print("\n-Поиск по адресу проживания-\n")
                    print("Все адреса проживания в справочнике:")
                    for i in self.spravochnik.keys():
                        print("{0}:".format(i), self.spravochnik[i][0]['name'], self.spravochnik[i][2]) 
                    address = {}
                    address['address'] = input("Введите нужный адрес проживания:")
                    step = 0
                    step_w = 0
                    while step_w == 0:
                        for i in self.spravochnik.keys():
                            if address == self.spravochnik[i][2]:
                                print("Контакт найден: {0}:".format(i), self.spravochnik[i])
                                step = 1
                                step_w = 1
                        if step == 0:
                            print("Данный адрес проживания отсутствует в справочнике")
                            address['address'] = input("Введите заново нужный дрес проживания:")

                elif start == 5:
                    print("\n-Поиск по месту работы-\n")
                    print("Все места работы в справочнике:")
                    for i in self.spravochnik.keys():
                        print("{0}:".format(i), self.spravochnik[i][0]['name'], self.spravochnik[i][3]) 
                    job = {}
                    job['job'] = input("Введите нужное мнсто работы:")
                    step = 0
                    step_w = 0
                    while step_w == 0:
                        for i in self.spravochnik.keys():
                            if job == self.spravochnik[i][3]:
                                print("Контакт найден: {0}:".format(i), self.spravochnik[i])
                                step = 1
                                step_w = 1
                        if step == 0:
                            print("Данное место работы отсутствует в справочнике")
                            job['job'] = input("Введите заново нужное место работы:")

start = 0
while start == 0:
    print("\n           ---* МЕНЮ *---\n"
          "--Выберите одно из нескольких действий--\n"
          "1: Добавление контакта\n"
          "2: Удаление контакта\n"
          "3: Редактирование контакта\n"
          "4: Вывод всех контактов на экран\n"
          "5: Поиск контактов по различным параметрам\n"
          "6: Выход\n")
    start = int(input())
    if start == 1:
        person = SpravochnikAdd()
        person.add()
        start = 0
    elif start == 2:
        person = SpravochnikNoAdd()
        person.delete()
        start = 0
    elif start == 3:
        person = SpravochnikNoAdd()
        person.edit()
        start = 0
    elif start == 4:
        person = SpravochnikNoAdd()
        person.screen()
        start = 0
    elif start == 5:
        person = SpravochnikNoAdd()
        person.search()
        start = 0
    elif start == 6:
        print("Выход из программы")
    else:
        print("Выберите нужный вариант в МЕНЮ\n")
        start = 0


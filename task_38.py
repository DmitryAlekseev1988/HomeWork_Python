def Write_Contact(path_telefon_list="c:/Users/88_d1/OneDrive/Рабочий стол/HomeWork_8/telefon_list.txt"):
    with open(path_telefon_list, "a", encoding="UTF-8") as telefon_list:
        first_name = input("Введите имя: ")
        second_name = input("Введите фамилию: ")
        phone = input("Введите номер телефона: ")
        telefon_list.write(f"{first_name}, {second_name}, {phone}\n")

def Find_Contact(path_telefon_list="c:/Users/88_d1/OneDrive/Рабочий стол/HomeWork_8/telefon_list.txt"):
    with open(path_telefon_list, "r", encoding="UTF-8") as telefon_list:
        find_name = input("Поиск: ")
        lines = telefon_list.readlines()
        found_contact = True
        for i in lines:
            if find_name in i:
                print(i, end="")
                found_contact = False
        if found_contact == True:
            print("Контакт не найден ")

def Print_All_Contact(path_telefon_list="c:/Users/88_d1/OneDrive/Рабочий стол/HomeWork_8/telefon_list.txt"):
    with open(path_telefon_list, "r", encoding="UTF-8") as telefon_list:
        lines = telefon_list.readlines()
        for i in lines:
            print(i, end="")

def Main_menu(path_telefon_list="c:/Users/88_d1/OneDrive/Рабочий стол/HomeWork_8/telefon_list.txt"):
    menu_contact = int(
        input(" ----------------------------------\n Телефонный справочник \n\n 1 - Поиск\n 2 - Добавление нового контакта\n 3 - Вывод всех контактов\n 4 - Редактировать запись\n 5 - Удалить запись\n 0 - Выход\n\nВведитек нужный номер: "))
    while menu_contact != 0:
        if menu_contact == 1:
            Find_Contact()
        elif menu_contact == 2:
            Write_Contact()
        elif menu_contact == 3:
            print("\nСписок контактов\n")
            Print_All_Contact()
        elif menu_contact == 4:
            Edit_Contact()
        elif menu_contact == 5:
            Delet_Contact()
        else:
            print("Таких параметров нет")
        menu_contact = int(input(" ----------------------------------\n Телефонный справочник \n\n 1 - Поиск\n 2 - Добавление нового контакта\n 3 - Вывод всех контактов\n 4 - Редактировать запись\n 5 - Удалить запись\n 0 - Выход\n\nВведитек нужный номер: "))
            
def Edit_Contact(path_telefon_list="c:/Users/88_d1/OneDrive/Рабочий стол/HomeWork_8/telefon_list.txt"):
    first_name = input("Введите изменяемое имя: ").title() # .title() - возвращает стрроку с заглавной буквы.
    second_name = input("Введите изменяемую фамилию: ").title()
    with open(path_telefon_list, 'r', encoding='UTF=8') as telefon_list:
            lines = telefon_list.readlines()
    found_contacts = False
    for i in range(len(lines)):
        contact_data = lines[i].strip().split(',') # Разделяем наш контакт на имя и фамилию убераем пробелы и индексируем
                                                       # ".split(',')" разделяем нашу строку по символу (","), теперть каждое слово будет индексироваться по [i] элементу (Если параметр не задать, то разделение будет выполнено именно по символу пробела)
                                                       #".strip()" - удаляем отступы справа и слева строки  
                                                       #".rstrip()" - удаляем отступы только справа  
                                                       #".lstrip()" - удаляем отступы только слева
        contact_first_name = contact_data[0].strip()
        contact_second_name = contact_data[1].strip()
        if contact_first_name == first_name and contact_second_name == second_name:
            new_first_name = input("Введите новое имя: ").title() 
            new_second_name = input("Введите новую фамилию: ").title()
            new_phone = input("Введите новый телефон : ")
            contact_data[0] = new_first_name
            contact_data[1] = new_second_name
            contact_data[2] = new_phone
            lines[i] = ','.join(contact_data) + '\n'
            found_contacts = True
            break
    if found_contacts == True:
        with open(path_telefon_list, 'w', encoding='UTF=8') as telefon_list:
            telefon_list.writelines(lines)
        print('Контакт успешно обновлен')
    else:
        print('Контакт не найден')

def Delet_Contact(path_telefon_list='c:/Users/88_d1/OneDrive/Рабочий стол/HomeWork_8/telefon_list.txt'):
    first_name = input("Введите имя: ").title() # .title() - возвращает стрроку с заглавной буквы.
    second_name = input("Введите фамилию: ").title()
    with open(path_telefon_list, "r" ,encoding="UTF-8") as telefon_list:
        lines = telefon_list.readlines()
    with open(path_telefon_list, "w" ,encoding="UTF-8") as telefon_list:
        contact_found = False
        for i in lines:
            contact = i.strip().split(',')
            if not ((first_name in contact[0]) and (second_name in contact[1])):
                telefon_list.write(i)
            else:
                contact_found = True
        if contact_found == True:
            print("Контакт успешно удален")
        else:
            print('Контакт не найден')

Main_menu()

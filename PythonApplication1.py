from math import *
#S1 = input("Введите первую строку: ")
#S2 = input("Введите вторую строку: ")
#result = S1 + S2
#print("ответ", result)



from math import *

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
abc = ['Abc', 'B', 'C']
slovo = "Programmeerimine"
slovo_list = list(slovo)
print(slovo)
print(slovo_list)

while True:
    print("1-добавить букву в список")
    print("2-склеить списки\n3-добавить букву в позицию")
    print("4-рассмотреть пример кода isspace()")
    print("5-рассмотреть пример кода .replace()")
    print("6-проверить, начинаются ли все слова в строке с заглавной буквы")
    print("7-проверить, все ли символы в строке в нижнем регистре")
    print("8-преобразовать все слова в строке к виду с заглавной буквы")
    valik = int(input())

    if valik == 1:
        a = input("Введи букву: ")
        slovo_list.append(a)
        print(f"Добавили {a} в новый список", slovo_list)
    elif valik == 2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik == 3:
        a = input("Введи букву, которую хочешь добавить: ")
        i = int(input("Введи номер позиции, куда хочешь добавить букву: "))
        slovo_list.insert(i - 1, a)
    elif valik == 4:
        example_code = """
        # Пример использования метода isspace() 
        s = "   "  # Пример строки, состоящей только из пробельных символов
        result = s.isspace()
        print(result)  # Выведет True, если строка состоит только из пробельных символов
        """
        print("Пример использования метода isspace():")
        s = input("Что вы хотите ввести?")
        result = s.isspace()
        print(example_code)
        print(result)
    elif valik == 5:
        a = input("Введи букву, которую хочешь удалить: ")
        n = slovo_list.count(a)
        if n > 0:
            for i in range(n):
                slovo_list.remove(a)
    elif valik == 6:
        print("Проверка, начинаются ли все слова в строке с заглавной буквы:")
        s = input("Введите строку: ")
        if s.istitle():
            print("Все слова в строке начинаются с заглавной буквы.")
        else:
            print("Не все слова в строке начинаются с заглавной буквы.")
    elif valik == 7:
        s = input("Введите строку: ")
        if s.islower():
            print("Все символы в строке находятся в нижнем регистре.")
        else:
            print("Не все символы в строке находятся в нижнем регистре.")
    elif valik == 8:
        s = input("Введите строку с разным регистром слов: ")
        print("Преобразованные слова к виду с заглавной буквы:", s.title())


  nimed=[]
for i in range(5):
        nimi=input(f"Sisetage {i+1}. nimi: ").capitalize()
        nimed.append(nimi)
        
        print("Max: ",nimed)
        nimed.sort()
        print("Sortimise parast: ",nimed)
        print("Viimasena oli lisatud: ",nimi)

        vananimi=input("Mis nimi on vaja asendada? ")
        if nimed.count(vananimi)>0:
            uusnimi=input("Mis on uus nimi?")
            i=0
            for nimi in nimed:
                if nimi==vananimi:
                    vananimi.replace(vananimi,uusnimi)
                    nimed[i]=uusnimi
                i+=1
        else:
            print(f"{vananimi} ei ole")
        print(nimed)


#print("Меню:")
#print("1. Салаты")
#print("2. Мясо")
#print("3. Десерты")
#print("4. Напитки")
#print("5. Выход")

#choice = input("Выберите пункт меню: ")

#if choice == '1':
#    print("Салаты:")
#    print("1. Цезарь - 4.50 eur")
#    print("2. Греческий - 4.20 eur")
#    print("3. Оливье - 4.60 eur")
#    salad_choice = input("Выберите вид салата: ")
#    if salad_choice == '1':
#        print("Вы выбрали Цезарь за 4.50 eur")
#    elif salad_choice == '2':
#        print("Вы выбрали Греческий за 4.20 eur")
#    elif salad_choice == '3':
#        print("Вы выбрали Оливье за 4.60 eur")
#    else:
#        print("Неверный выбор.")

#elif choice == '2':
#    print("Мясо:")
#    print("1. Стейк - 5.60 eur")
#    print("2. Курица - 5.30 eur")
#    print("3. Свинина - 5.70 eur")
#    meat_choice = input("Выберите вид мяса: ")
#    if meat_choice == '1':
#        print("Вы выбрали Стейк за 5.60 eur")
#    elif meat_choice == '2':
#        print("Вы выбрали Курицу за 5.30 eur")
#    elif meat_choice == '3':
#        print("Вы выбрали Свинину за 5.70 eur")
#    else:
#        print("Неверный выбор.")

#if choice == '3':
#    print("Десерты:")
#    print("1. Торт медовик - 2.50 eur")
#    print("2. Мороженное - 2.20 eur")
#    print("3. Крем Брюле - 2.90 eur")
#    salad_choice = input("Выберите вид салата: ")
#    if salad_choice == '1':
#        print("Вы выбрали Торт медовик за 2.50 eur")
#    elif salad_choice == '2':
#        print("Вы выбрали Мороженное за 2.20 eur")
#    elif salad_choice == '3':
#        print("Вы выбрали Крем Брюле за 2.90 eur")
#    else:
#        print("Неверный выбор.")

#if choice == '4':
#    print("Десерты:")
#    print("1. Лимонад - 1.50 eur")
#    print("2. Вода - 1.20 eur")
#    print("3. Сок - 1.70 eur")
#    salad_choice = input("Выберите вид салата: ")
#    if salad_choice == '1':
#        print("Вы выбрали Лимонад - 1.50 eur")
#    elif salad_choice == '2':
#        print("Вы выбрали  Вода - 1.20 eur")
#    elif salad_choice == '3':
#        print("Вы выбрали Сок - 1.70 eur")
#    else:
#        print("Неверный выбор.")

#elif choice == '5':
#    print("Спасибо за покупку! До свидания.")

#else:
#    print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 5.")

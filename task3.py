#Python

f = open('1.txt')   #в файле 1.txt содержатся данные из столбца health таблицы monster game.csv
s = list(map(int, f.readlines()))   #считываем данные в список. тип данных - int
k = 0   #счетчик
atack = 0   #переменная для определения атаки/завершения игры
ff = True

while ff == True:   #основной цикл программы

    print('Введите силу атаки героя:')
    atack = input()

    if atack != 'хватит' and atack.isdigit() == True: #ситуация, когда atack является числом
        ff = True

        for i in range(len(s)):     #цикл для подсчета монстров
            if int(atack) > s[i]:
                k += 1
        if k == 0:
            print('Вы очень слабы. Сходите и наберитесь опыта!')    #вариант, когда k == 0
            continue

        print(f'Вы сможете победить: {k} монстров')     #вариант, когда k != 0

        k = 0   #обнуление счетчика

    elif atack.isdigit() == False and atack != 'хватит': #ситуация, когда atack не является числом и не равняется 'хватит'
        print('Вы очень слабы. Сходите и наберитесь опыта!')
        continue

    else:   #вариант, когда atack равняется 'хватит'
        ff = False
        break




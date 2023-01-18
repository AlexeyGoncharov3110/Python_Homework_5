from random import randint
konf = randint(100, 3000)
print(f'Всего на столе {konf} конфет')
max_konf = randint(20,50)
print(f'За один раз максимум можно взять {max_konf}')
name1 = input('Игрок №1 введите имя : ')
name2 = 'Бот с интеллектом'
lot = randint(1, 2)
while konf > 0:
    if lot == 1:
        print(f'Берёт конфеты {name1}')
        a = int(input(f'Игрок {name1} введите число от 1 до {max_konf} : '))
        while a < 1 or a > max_konf:
            a = int(
                input(f'Игрок {name1} введите корректное количество конфет: '))
        konf = konf-a
        if konf <= 0:
            print(f'Выиграл игрок {name1}')
            break
        if konf % (max_konf+1) == 0:
            print(f'{name2} берёт {max_konf} конфет ')
            konf = konf-max_konf
        elif konf % (max_konf+1) != 0:
            if konf > max_konf:
                print(f'{name2} берёт {konf%(max_konf+1)} конфет ')
                konf = konf-konf % (max_konf+1)
            if konf <= max_konf:
                print(f'{name2} берёт {max_konf} конфет ')
                konf = konf-max_konf
            if konf <= 0:
                print(f'Выиграл игрок {name2} ')
                break
        print(konf)
    else:
        print(f'Берёт конфеты {name2}')
        if konf % (max_konf+1) != 0:
            count = 0
            while konf > 0:
                if count == 0:
                    print(f'{name2} берёт {konf%(max_konf+1)} конфет')
                    konf = konf-konf % (max_konf+1)
                    if konf <= 0:
                        print(f'Выиграл игрок {name2} ')
                        break
                if count >= 1:
                    print(f'{name2} берёт {(max_konf+1)-a} конфет')
                    konf = konf-(max_konf+1-a)
                    if konf <= 0:
                        print(f'Выиграл игрок {name2} ')
                        break
                count += 1
                a = int(
                    input(f'Игрок  {name1} введите число от 1 до {max_konf} : '))
                while a < 1 or a > max_konf:
                    a = int(
                        input(f'Игрок {name1} введите корректное количество конфет: '))
                konf = konf-a
                if konf <= 0:
                    print(f'Выиграл игрок {name1}')
                    break
                print(konf)

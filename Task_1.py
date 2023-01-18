from random import randint
konf = randint(100,3000)
max_konf=int(input('Введите максимальное кол-во конфет , которое можно взять за один раз : '))
print(konf)
name1=input('Игрок №1 введите имя : ')
name2=input('Игрок №2 введите имя : ')
if name1==name2:
    name1= str(name1 +'1')
    name2= str(name2 +'2')
lot = randint(1, 2)
print(lot)
while konf > 0:
    if lot==1:
        a = int(input(f'Игрок  {name1} введите число от 1 до {max_konf} : '))
        while a < 1 or a > max_konf:
            a = int(input(f'Игрок {name1} введите корректное количество конфет: '))
        konf = konf-a
        if konf <= 0:
            print(f'Выиграл игрок {name1}')
            break   
        b = int(input(f'Игрок  {name2} введите число от 1 до {max_konf} : '))
        while b < 1 or b > max_konf :
            b = int(input(f"Игрок {name2} , введите корректное количество конфет: "))
        konf = konf-b
        if konf <= 0:
            print(f'Выиграл игрок {name2} ')
            break  
        print(konf)
    else:
        a = int(input(f'Игрок {name2} введите число от 1 до {max_konf} : '))
        while a < 1 or a > 28:
            a = int(input(f"Игрок {name2} , введите корректное количество конфет: "))
        konf = konf-a
        if konf <= 0:
            print(f'Выиграл игрок {name2} ')
            break   
        b = int(input(f'Игрок {name1} введите число от 1 до {max_konf} : '))
        while b < 1 or b > 29-a :
            b = int(input(f"Игрок {name1} , введите корректное количество конфет: "))
        konf = konf-b
        if konf <= 0:
            print(f'Выиграл игрок {name1} ')
            break  
        print(konf)

        
        
   
## Вебирнар по структуре данных: Списки и словари
my_list = [] ## создание пустого списка
spisok = ['лебедь', 'рак', 'щука']  ##создание списка с 3мя элементами
spisok[2]  ## обращение к 3му элементу списка
spisok[1] = 'форель'  ## замена рака на форель!
len(spisok)  ## длина списка
if 'щука' in spisok:  ## вхождение элемента в список
    print('True')
else:
    print('False')
def pr(): ## функция вывода и проверки на существующую букву
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    print(vowels)
    idx = int(input('Введите индекс:'))
    if len(vowels)<idx:
        print('Буквы под таким номером не существует!')
    else:
        print(vowels[idx-1])
##pr()

##Срезы списка
## list[start:stop:step]
def sliens(): ##пример срезов
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    print(vowels[0:3])  ## ['а', 'е', 'ё']
    print(vowels[4::2])  ## ['о', 'ы', 'ю']
    print(vowels[5:])  ## ['у', 'ы', 'э', 'ю', 'я']
    print(vowels[-6:-3])  ## ['о', 'у', 'ы']
##sliens()

## операции со списками

spisok.append('рак') ## добавление элемента
##print(spisok)['лебедь', 'форель', 'щука', 'рак']

spisok.remove('форель')  ## удаление элемента
## print(spisok) ['лебедь', 'щука', 'рак']

spisok.sort(reverse=True) ## сортировка в обратную сторону по алфавиту
## print(spisok) ['щука', 'рак', 'лебедь']
spisok.sort() ## сортировка по алфавиту просто (reverse по умолчанию False)
##print(spisok) ['лебедь', 'рак', 'щука']

##также списки можно склыдывать и умножать
##[1,3]*3=[1,3,1,3,1,3]
##[1,5]+[3]=[1,5,3]

##ПРИМЕР ЗАДАЧИ НА СПИСОК С ЦИКЛОМ!!!
def pr_gruz(): ## проверка груза на допустимость веса(100кг)
    items = [1, 5, 76, 12, 123, 333, 5, 6, 7]
    good_gruz = []
    for kg in items:
        print(f'Груз весит: {kg} килограмм')
        if kg > 100:
            print('Груз весит слишком много, не подходит!')
        else:
            good_gruz.append(kg)
            print(f'Груз подходит! Берем!')
    print(good_gruz)
##pr_gruz()

## Вложение Списков !!!

array_of_arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  ##создаем списки в списке (получаем матрицу)
## print(array_of_arrays[1][1]) Получаем: 5

## задача умножение каждого элемента на 2
def ymn():
    for i in range(len(array_of_arrays)):
        for j in range(len(array_of_arrays)):
            array_of_arrays[i][j] *= 2
    print(array_of_arrays)
## ymn() [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

## ГЕНЕРАТОР СПИСКОВ
def generator():  ## создаем список состоящий из квадратов от 0 до 9
    gen_list = []
    for i in range(10):
        gen_list.append(i**2)
    print(gen_list)
##generator()[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
gen_spisok = [i**2 for i in range(10)] ## ДЕЛАЕМ ТОЖЕ САМОЕ НО В 1 СТОЧКУ
##print(gen_spisok)[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

## также можем добавить еще усовие
gen_y_sp = [i for i in range(10, 100) if i % 3 == 0 and i % 5 == 0]
##print(gen_y_sp) [15, 30, 45, 60, 75, 90]

##Задача от платформы
gen_zad = [((i // 10) + (i % 10)) for i in range(90,100)]
##print(gen_zad)[9, 10, 11, 12, 13, 14, 15, 16, 17, 18]



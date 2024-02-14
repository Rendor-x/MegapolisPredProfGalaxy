def readFile(filename):
    '''
    Считываем файл и записываем данные в список
    :param filename: txt, имя файла
    :return: list, список с данными из файла
    '''
    f = open(filename, 'r', encoding='utf-8')
    ls = []
    for j in range(101):
        ls.append(f.readline().strip().split('*'))
    return ls


def hash(sp):
    '''
    Функция, создающая хеш-таблицу
    :param sp: list, список значение из файла space.txt
    :return: dict, хеш-таблица
    '''
    list_of_planets = []
    dc = {}
    for i in sp[1:]:
        if i[1] not in list_of_planets:
            list_of_planets.append(i[1])
    for i in list_of_planets:
        dc[i] = []
        for j in sp[1:]:
            if j[1] == i:
                dc[i].append(j[0])

    return dc


def planetsgone(planet):
    '''
    функция вывода кораблей, улетевших с заданной планеты
    :param planet: str, планета
    :return: str, планета и улетевшие с нее корабли
    '''
    return f'{planet}: {hash_table[planet]}'


space = readFile('space.txt')
hash_table = hash(space)
cnt = 0
for key in hash_table:
    if cnt != 10:
        print(planetsgone(key))
        cnt += 1
    else:
        break


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


def passwordgen(planet, ship):
    '''
    Создание пароля для корабля
    :param planet: str, название планеты
    :param ship: str, название корабля
    :return: str, пароль
    '''
    password = planet[-3:] + ship[1:3][::-1] + planet[:3][::-1]
    return password.upper()


def writeLs(sp):
    '''
    Запсиь в список, где хранятся данные из файла space.txt, паролей
    :param sp: list, список данныз из файла space.txt
    :return: list, изменненный список
    '''
    sp[0].append('password')
    for i in range(1, 101):
        sp[i].append(passwordgen(sp[i][1], sp[i][0]))
    return sp


def writeFile(filename, par):
    '''
    Запись данных из списка в новый файл
    :param filename: str, имя файла
    :param par: list, список значений
    :return: -
    '''
    f = open(filename, 'w', encoding='utf-8')
    for j in par:
        f.write('*'.join(j) + '\n')
    f.close()


space = readFile('space.txt')
new_space = writeLs(space)
writeFile('space_uniq_password.csv', new_space)



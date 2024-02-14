def readFile(filename):
    '''
    Считываем файл и записываем данные в список
    :param filename: txt, имя файла
    :return: list, список с данными из файла
    '''
    f = open(filename, 'r', encoding='utf-8')
    ls = []
    for j in range(501):
        ls.append(f.readline().strip().split('*'))
    return ls


space = readFile('space.txt')
ship = input()
cnt = 0
while ship != 'stop':
    for i in space:
        if ship == i[0]:
            print(f'Корабль {ship} был отправлен с планеты: {i[1]} и его направление движения было: {i[3]}')
            cnt = 1
            break
    if cnt == 0:
        print('error.. er.. ror..')
    else:
        cnt = 0
    ship = input()

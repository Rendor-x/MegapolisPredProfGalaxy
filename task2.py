def readFile(filename):
    '''
    Считываем файл и записываем данные в список
    :param filename: txt, имя файла
    :return: list, список с данными из файла
    '''
    f = open(filename, 'r', encoding='utf-8')
    f.readline()
    ls = []
    for j in range(1, 101):
        ls.append(f.readline().strip().split('*'))
    return ls


space = readFile('space.txt')
for i in range(100):
    g = i
    while g > 0 and int(space[g][0].split('-')[1]) > int(space[g - 1][0].split('-')[1]):
        space[g],  space[g - 1] = space[g - 1], space[g]
        g -= 1
space = space[::-1]
print(space)
for i in range(10):
    print(space[i][0])

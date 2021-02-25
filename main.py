def parse(file_path):
    file = open(file_path)
    d, i, s, v, f = file.readline().rstrip().split(' ')
    d, i, s, v, f = int(d), int(i), int(s), int(v), int(f)

    for j in range(s):
        b, e, street_name, l = file.readline().rstrip().split(' ')
        b, e, l = int(b), int(e), int(l)

    for j in range(v):
        cpt = 0
        line = file.readline().rstrip()
        p = 0
        path = []
        for word in line.split(' '):
            if cpt == 0:
                p = int(word)
            else:
                path.append(word)
            cpt += 1



if __name__ == '__main__':
    parse('a.txt')
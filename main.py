from model import *

def parse(file_path):
    file = open(file_path)
    d, i, s, v, f = file.readline().rstrip().split(' ')
    d, i, s, v, f = int(d), int(i), int(s), int(v), int(f)

    street_map = {}
    inter_map = {}
    for j in range(s): #street
        b, e, street_name, l = file.readline().rstrip().split(' ')
        b, e, l = int(b), int(e), int(l)
        street_map[street_name] = Street(street_name, l, b, e)
        #Out

        if b not in inter_map:
            inter_map[b] = Intersection(b, [], [street_map[street_name]])
        else:
            inter_map[b].streets_out.append([street_map[street_name]])
        #in
        if e not in inter_map:
            inter_map[e] = Intersection(e, [street_map[street_name]], [])
        else:
            inter_map[e].streets_in.append([street_map[street_name]])

    # Cars
    cars = []
    car_id = 0
    for j in range(v):
        cpt = 0
        line = file.readline().rstrip()
        p = 0
        path = []
        for word in line.split(' '):
            if cpt == 0:
                p = int(word)
            else:
                path.append(street_map[word])
            cpt += 1
        car_id += 1
        cars.append(Car(car_id, d, True, path))

    return street_map, inter_map, cars



if __name__ == '__main__':
    street_map, inter_map, cars = parse('a.txt')

    print(street_map)
    print(inter_map)
    print(cars)
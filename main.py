from model import *

def parse(file_path):
    file = open(file_path)
    d, i, s, v, f = file.readline().rstrip().split(' ')
    d, i, s, v, f = int(d), int(i), int(s), int(v), int(f)

    street_hist = {}
    street_map = {}
    inter_map = {}
    for j in range(s): #street
        b, e, street_name, l = file.readline().rstrip().split(' ')
        b, e, l = int(b), int(e), int(l)
        street_map[street_name] = Street(street_name, l, b, e)
        street_hist[street_name] = (0, l)

        #Out

        if b not in inter_map:
            inter_map[b] = Intersection(b, [], [street_name])
        else:
            inter_map[b].streets_out.append(street_name)
        #in
        if e not in inter_map:
            inter_map[e] = Intersection(e, [street_name], [])
        else:
            inter_map[e].streets_in.append(street_name)

    for inter_elt in inter_map.values():
        inter_elt.init_scheduler()

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
                street_hist[word] = (street_hist.get(word)[0] + 1, street_hist.get(word)[1])
            cpt += 1
        car_id += 1
        cars.append(Car(car_id, d, True, path))

    return street_map, inter_map, cars, street_hist



if __name__ == '__main__':
    street_map, inter_map, cars, street_hist = parse('a.txt')

    print(street_map)
    print(inter_map)
    print(cars)
    print(street_hist)
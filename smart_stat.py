from helper import get_never_list_streets
from model import Car, Intersection, Street
from writer import write_result

def parse_smart_2(file_path):
    file = open(file_path)
    d, i, s, v, f = file.readline().rstrip().split(' ')
    d, i, s, v, f = int(d), int(i), int(s), int(v), int(f)


    step_one_histo = {}
    step_two_histo = {}
    street_hist = {}
    street_map = {}
    inter_map = {}
    for j in range(s): #street
        b, e, street_name, l = file.readline().rstrip().split(' ')
        b, e, l = int(b), int(e), int(l)
        street_map[street_name] = Street(street_name, l, b, e)
        street_hist[street_name] = (0, l)
        step_one_histo[street_name] = (0, l)
        step_two_histo[street_name] = (0, l)

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
                if cpt == 1:
                    step_one_histo[word] = (step_one_histo.get(word)[0] + 1, step_one_histo.get(word)[1])
                if cpt == 2:
                    step_two_histo[word] = (step_two_histo.get(word)[0] + 1, step_two_histo.get(word)[1])


            cpt += 1
        car_id += 1
        cars.append(Car(car_id, d, True, path))

    list_never_streets = get_never_list_streets(street_hist)

    for inter_elt in inter_map.values():
        inter_elt.init_scheduler_histo(list_never_streets, street_hist, step_one_histo)

    return street_map, inter_map, cars, street_hist, step_one_histo, step_two_histo


def parse_smart(file_path):
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

    list_never_streets = get_never_list_streets(street_hist)

    for inter_elt in inter_map.values():
        inter_elt.init_scheduler_histo(list_never_streets, street_hist, )

    return street_map, inter_map, cars, street_hist


if __name__ == '__main__':
    files = [
        'a.txt',
        'b.txt',
        'c.txt',
        'd.txt',
        'e.txt',
        'f.txt',
    ]

    for f in files:
        print(f, " -- Parse")

        street_map, inter_map, list_cars, street_hist, s2, s3 = parse_smart_2(f)

        print(f, " -- Write")

        write_result(f + '.out', inter_map.values(), street_map.values(), list_cars)
        print()

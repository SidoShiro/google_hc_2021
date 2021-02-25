from helper import get_never_list_streets
from main import parse
from writer import write_result

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

        street_map, inter_map, list_cars, street_hist = parse(f)

        print(f, " -- Write")

        write_result(f + '.out', inter_map.values(), street_map.values(), list_cars)
        print()

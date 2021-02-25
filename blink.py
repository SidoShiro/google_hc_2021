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

        parse(f)
        list_intersection, list_streets = [], []
        list_cars = []
        write_result(f + '.out', list_intersection, list_streets, list_cars)

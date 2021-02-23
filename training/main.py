from model import Pizza


def parse(file_path):
    f = open(file_path)
    nb_pizza, nb_2group, nb_3group, nb_4group = f.readline().rstrip().split(' ')
    nb_pizza, nb_2group, nb_3group, nb_4group = int(nb_pizza), int(nb_2group), int(nb_3group), int(nb_4group)

    pizza_list = []
    for i in range(nb_pizza):
        line = f.readline().rstrip()
        cpt = 0
        nb_ingrediant = 0
        list_ingrediant = []
        for word in line.split(' '):
            if cpt == 0:
                nb_ingrediant = int(word)
            else:
                list_ingrediant.append(word)
            cpt += 1
        p = Pizza(nb_ingrediant, list_ingrediant)
        pizza_list.append(p)

    return pizza_list, nb_2group, nb_3group, nb_4group



def create_open(file_path):
    f = open(file_path + ".out", 'w')
    for i in v_list:
        f.write("OUTPUT")
        f.write('\n')
    f.close()


if __name__ == '__main__':
    print("start")
    pizza_list, nb_2group, nb_3group, nb_4group = parse('files/a_example')
    for pizza in pizza_list:
        pizza.pretty_print()

from model import Pizza, Team
from helper import define_target
from algo_v1 import algo_v1_fun


def parse(file_path):
    f = open(file_path)
    nb_pizza, nb_2group, nb_3group, nb_4group = f.readline().rstrip().split(' ')
    nb_pizza, nb_2group, nb_3group, nb_4group = int(nb_pizza), int(nb_2group), int(nb_3group), int(nb_4group)

    pizza_list = []
    id_pizza = 0
    hist = {}
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
                hist[word] = hist.get(word, 0) + 1
            cpt += 1
        p = Pizza(id_pizza, nb_ingrediant, list_ingrediant)
        pizza_list.append(p)
        id_pizza += 1

    return pizza_list, nb_2group, nb_3group, nb_4group, hist


# Team
#  .nb
#  .pizzas
def create_open(file_path, teams: list):
    f = open(file_path + ".out", 'w')
    f.write(str(len(teams)) + '\n')
    for team in teams:
        line = str(team.nb) + ' ' + str(team.pizzas[0].id_pizza)
        for pizza in team.pizzas[1:]:
            line += ' ' + str(pizza.id_pizza)
        f.write(line + '\n')
    f.close()


if __name__ == '__main__':
    print("start")

    file_name = 'files/a_example'

    pizza_list, nb_2group, nb_3group, nb_4group, hist = parse(file_name)

    target = define_target(pizza_list)

    teams = algo_v1_fun(pizza_list, nb_2group, nb_3group, nb_4group, target)

    create_open(file_name, teams)

    print('end')

from model import Pizza


def define_target(list_pizza: []):
    if len(list_pizza) == 0:
        return 1

    mean = 0
    for i in list_pizza:
        mean += i.nb_in
    mean /= len(list_pizza)

    return mean / 4

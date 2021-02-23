from main import parse
from model import Team
from basic import score_2_pizzas
from basic import score_3_pizzas
from basic import score_4_pizzas


def algo_v1(pizza_list, nb_2group, nb_3group, nb_4group, target = 2):
    teams_list = []
    # Add Pizza to each Team
    for i in range(nb_2group):
        if len(pizza_list) > 2:
            t = Team(2)
            p1 = pizza_list[0]
            p2 = pizza_list[1]
            sc2 = score_2_pizzas(p1, p2)
            j = 2
            while sc2 < target and j < len(pizza_list):
                p2 = pizza_list[j]
                j += 1
                sc2_y =

            t.add_score(sc2)
            t.add_pizza(p1)
            t.add_pizza(p2)
            pizza_list.remove(p1)
            pizza_list.remove(p2)
            teams_list.append(t)
    for i in range(nb_3group):
        if len(pizza_list) > 3:
            t = Team(3)
            p1 = pizza_list[0]
            p2 = pizza_list[1]
            p3 = pizza_list[2]
            t.add_pizza(p1)
            t.add_pizza(p2)
            t.add_pizza(p3)
            pizza_list.remove(p1)
            pizza_list.remove(p2)
            pizza_list.remove(p3)
            teams_list.append(t)
    for i in range(nb_4group):
        if len(pizza_list) > 4:
            t = Team(4)
            p1 = pizza_list[0]
            p2 = pizza_list[1]
            p3 = pizza_list[2]
            p4 = pizza_list[3]
            t.add_pizza(p1)
            t.add_pizza(p2)
            t.add_pizza(p3)
            t.add_pizza(p4)
            pizza_list.remove(p1)
            pizza_list.remove(p2)
            pizza_list.remove(p3)
            pizza_list.remove(p4)
            teams_list.append(t)

    return teams_list

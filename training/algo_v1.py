from main import parse
from model import Team
from basic import score_2_pizzas
from basic import score_3_pizzas
from basic import score_4_pizzas


def algo_v1(pizza_list, nb_2group, nb_3group, nb_4group, target = 2):
    teams_list = []
    # Add Pizza to each Team
    for i in range(nb_2group):
        if len(pizza_list) >= 2:
            t = Team(2)
            p1 = pizza_list[0]
            p2 = pizza_list[1]
            sc2 = score_2_pizzas(p1, p2)
            j = 2
            sc2_y = 0

            while sc2_y < target and j < len(pizza_list):
                p_tmp = pizza_list[j]
                j += 1
                sc2_y = score_2_pizzas(p1, p_tmp)
                if sc2_y > sc2:
                    p2 = p_tmp

            t.add_score(sc2)
            t.add_pizza(p1)
            t.add_pizza(p2)
            pizza_list.remove(p1)
            pizza_list.remove(p2)
            teams_list.append(t)
    for i in range(nb_3group):
        if len(pizza_list) >= 3:
            t = Team(3)
            p1 = pizza_list[0]
            p2 = pizza_list[1]
            t.add_pizza(p1)
            pizza_list.remove(p1)

            j = 2
            while sc2_y < target and j < len(pizza_list):
                p_tmp = pizza_list[j]
                j += 1
                sc2_y = score_2_pizzas(p1, p_tmp)
                if sc2_y > sc2:
                    p2 = p_tmp

            t.add_pizza(p2)
            pizza_list.remove(p2)

            p3 = pizza_list[0]
            sc3 = score_3_pizzas(p1, p2, p3)

            j = 1
            while sc3 < target and j < len(pizza_list):
                p_tmp = pizza_list[j]
                j += 1
                sc3_tmp = score_3_pizzas(p1, p2, p_tmp)
                if sc3_tmp > sc3:
                    p3 = p_tmp

            t.add_pizza(p3)
            pizza_list.remove(p3)
            teams_list.append(t)

    for i in range(nb_4group):
        if len(pizza_list) >= 4:
            t = Team(4)
            p1 = pizza_list[0]
            p2 = pizza_list[1]
            t.add_pizza(p1)
            pizza_list.remove(p1)

            j = 1
            while sc2_y < target and j < len(pizza_list):
                p_tmp = pizza_list[j]
                j += 1
                sc2_y = score_2_pizzas(p1, p_tmp)
                if sc2_y > sc2:
                    p2 = p_tmp

            t.add_pizza(p2)
            pizza_list.remove(p2)

            p3 = pizza_list[0]
            sc3 = score_3_pizzas(p1, p2, p3)

            j = 1
            while sc3 < target and j < len(pizza_list):
                p_tmp = pizza_list[j]
                j += 1
                sc3_tmp = score_3_pizzas(p1, p2, p_tmp)
                if sc3_tmp > sc3:
                    p3 = p_tmp

            t.add_pizza(p3)
            pizza_list.remove(p3)
            p4 = pizza_list[0]
            sc4 = score_4_pizzas(p1, p2, p3, p4)

            j = 1
            while sc4 < target and j < len(pizza_list):
                p_tmp = pizza_list[j]
                j += 1
                sc4_tmp = score_4_pizzas(p1, p2, p3, p_tmp)
                if sc4_tmp > sc3:
                    p4 = p_tmp

            t.add_pizza(p4)
            pizza_list.remove(p4)
            teams_list.append(t)

    return teams_list

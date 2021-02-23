class Pizza:
    def __init__(self, id_pizza, nb_in, list_in):
        self.id_pizza, self.nb_in, self.list_in = id_pizza, nb_in, list_in

    def pretty_print(self):
        print("-----")
        print(self.nb_in)
        for i in self.list_in:
            print('-' + i)


class Team:
    def __init__(self, nb: int):
        self.nb = nb
        self.pizzas = []

    def addPizza(self, pizza: Pizza):
        if len(pizza) > nb:
            self.pizzas.append(pizza)
            return True
        return False

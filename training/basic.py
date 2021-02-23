from .main import Pizza


def score_2_pizzas(a: Pizza, b: Pizza) :
    return a.nb_in + a.nb_in - set(a.list_in).update(b.list_in)
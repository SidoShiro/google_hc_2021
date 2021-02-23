from model import Pizza


def score_2_pizzas(a: Pizza, b: Pizza):
    inset = set(a.list_in)
    inset.update(b.list_in)
    return a.nb_in + b.nb_in - inset


def score_3_pizzas(a: Pizza, b: Pizza, c: Pizza):
    inset = set(a.list_in)
    inset.update(b.list_in)
    inset.update(c.list_in)
    return a.nb_in + b.nb_in + c.nb_in - inset


def score_4_pizzas(a: Pizza, b: Pizza, c: Pizza, d: Pizza):
    inset = set(a.list_in)
    inset.update(b.list_in)
    inset.update(c.list_in)
    inset.update(d.list_in)
    return a.nb_in + b.nb_in + c.nb_in + d.nb_in - inset

def get_never_list_streets(histo):
    list_never_streets = []
    for k in histo.keys():
        if histo[k][0] == 0:
            list_never_streets.append(k)
    return list_never_streets

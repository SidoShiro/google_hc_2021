class Pizza:
    def __init__(self, nb_in, list_in):
        self.nb_in, self.list_in = nb_in, list_in

    def pretty_print(self):
        print("-----")
        print(self.nb_in)
        for i in self.list_in:
            print('-' + i)

class Street:
    def __init__(self, street_id, length: int, inter_a: int, inter_b: int):
        self.street_id = street_id
        self.length = length
        self.inter_a = inter_a
        self.inter_b = inter_b
        self.cars_list = []


class Intersection:
    def __init__(self, inter_id, streets_in: [], streets_out: []):
        self.inter_id = inter_id
        self.streets_in = streets_in
        self.streets_out = streets_out
        self.traffic_lights = [TrafficLight(False) for i in range(len(streets_in))]
        self.scheduler = []

    def init_scheduler(self, blacklist_streets: []):
        for i in self.streets_in:
            if not i in blacklist_streets:
                self.scheduler.append((i, 1))
        if 0 == len(self.scheduler):
            self.scheduler.append((self.streets_in[0], 1))

    def init_scheduler_histo(self, blacklist_streets: [], histo):
        # Clean Histo
        """
        list_keys_to_rm = []
        for k in histo.keys():
            if histo[k][0] == 0:
                list_keys_to_rm.append(k)
        for k in list_keys_to_rm:
            del histo[k]
        """

        small_used_key = self.streets_in[0]
        small_used_value = 10000000

        biggest_len = 0
        biggest_key = 0
        smallest_len = 10000000
        smallest_key = 0

        for s in self.streets_in:
            if 0 < histo[s][0] < small_used_value:
                small_used_key = s
                small_used_value = histo[s][0]
            if histo[s][1] > biggest_len:
                biggest_len = histo[s][1]
                biggest_key = s
            if histo[s][1] < smallest_len:
                smallest_len = histo[s][1]
                smallest_key = s

        time_ponderator = 1000000
        for i in self.streets_in:
            if i not in blacklist_streets:
                time = 1 + ((histo[i][0] * biggest_len) // (2 * histo[i][1] * histo[small_used_key][0]))
                if time < time_ponderator:
                    time_ponderator = time
                self.scheduler.append((i, time))

        for i in range(len(self.scheduler)):
            self.scheduler[i] = (self.scheduler[i][0], self.scheduler[i][1] // time_ponderator)

        # Sort Schedulers depending on car position in streets_in
        # self.scheduler.sort(key=lambda t: t[1], reverse=True)
        # self.scheduler.sort(key=lambda t: t[1], reverse=False)

        if 0 == len(self.scheduler):
            self.scheduler.append((self.streets_in[0], 1))


class Car:
    def __init__(self, car_id, min_time_left: int, stuck: bool, path: []):
        self.id = car_id
        self.min_time_left = min_time_left
        self.stuck = stuck
        self.path = path


class TrafficLight:
    def __init__(self, green: bool):
        self.green = green

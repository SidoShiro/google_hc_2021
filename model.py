
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

    def init_scheduler(self):
        self.scheduler = [(self.streets_in[i], 1) for i in range(len(self.streets_in))]



class Car:
    def __init__(self, car_id, min_time_left: int, stuck: bool, path: []):
        self.id = car_id
        self.min_time_left = min_time_left
        self.stuck = stuck
        self.path = path


class TrafficLight:
    def __init__(self, green: bool):
        self.green = green


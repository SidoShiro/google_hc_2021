
class Street:
    def __init__(self, street_id, len: int, inter_a: int, inter_b: int):
        self.id = street_id
        self.len = len
        self.interA = inter_a
        self.interB = inter_b
        self.cars_list = []


class Intersection:
    def __init__(self, inter_id, streets_in: [], streets_out: []):
        self.inter_id = inter_id
        self.streetsIn = streets_in
        self.streetsOut = streets_out
        self.trafficLights = [TrafficLight(False) for i in len(streets_in)]


class Car:
    def __init__(self, car_id, min_time_left: int, stuck: bool, path: []):
        self.id = car_id
        self.minTimeLeft = min_time_left
        self.stuck = stuck
        self.path = path


class TrafficLight:
    def __init__(self, green: bool):
        self.green = green


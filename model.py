
class Street:
    def __init__(self, id, len: int, interA: int, interB: int):
        self.id = id
        self.len = len
        self.interA = interA
        self.interB = interB


class Intersection:
    def __init__(self, streetsIn : [], streetsOut: []):
        self.streetsIn = streetsIn
        self.streetsOut = streetsOut


class Car:
    def __init__(self, id, minTimeLeft: int, stuck: bool, path: []):
        self.id = id
        self.minTimeLeft = minTimeLeft
        self.stuck = stuck
        self.path = path


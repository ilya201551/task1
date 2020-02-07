import json


class Rooms:
    def __init__(self, rooms_path: str):
        with open(rooms_path, 'r') as read_file:
            self.rooms_list = json.load(read_file)

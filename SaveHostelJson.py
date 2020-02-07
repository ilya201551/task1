import json


class HostelJson:
    def __init__(self, hostel_list: dict):
        with open('Hostel.json', 'w') as write_file:
            json.dump(hostel_list, write_file, indent=4)

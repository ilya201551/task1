import json


class HostelJson:
    @staticmethod
    def save(hostel_list: dict):
        with open('Hostel.json', 'w') as write_file:
            json.dump(hostel_list, write_file, indent=4)

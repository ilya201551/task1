import json


class Students:
    def __init__(self, students_path: str):
        with open(students_path, 'r') as read_file:
            self.students_list = json.load(read_file)

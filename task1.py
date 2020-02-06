import json


class Students:
    def __init__(self, students_path: str):
        with open(students_path, 'r') as read_file:
            self.students_list = json.load(read_file)


class Rooms:
    def __init__(self, rooms_path: str):
        with open(rooms_path, 'r') as read_file:
            self.rooms_list = json.load(read_file)


class HostelList:
    def __init__(self, students_path: str, rooms_path: str):
        self.students_list = Students(students_path).students_list
        self.rooms_list = Rooms(rooms_path).rooms_list
        self.hostel_list = self.hostel_list()

    def hostel_list(self):
        hostel_list = self.rooms_list[:]
        for student in self.students_list:
            for room in hostel_list:
                if 'students' in room.keys():
                    if room['id'] == student['room']:
                        room['students'].append(student)
                else:
                    room['students'] = []
        return hostel_list


class HostelJson:
    def __init__(self, hostal_list: dict):
        with open("Hostel.json", "w") as write_file:
            json.dump(hostal_list, write_file, indent=4)


class FormattedHostelList:
    def __init__(self, students_path: str, rooms_path: str, format_: str):
        if format_.lower() == "json":
            HostelJson(HostelList(students_path, rooms_path).hostel_list)


def main():
    FormattedHostelList('students.json', 'room.json', 'json')


if __name__ == '__main__':
    main()

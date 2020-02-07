from StudentsLoader import Students
from RoomsLoader import Rooms


class HostelList:
    def __init__(self, students_path: str, rooms_path: str):
        self.students_list = Students(students_path).students_list
        self.rooms_list = Rooms(rooms_path).rooms_list
        self.hostel_list = self.__hostel_list()

    def __hostel_list(self):
        hostel_list = self.rooms_list[:]
        for student in self.students_list:
            for room in hostel_list:
                if 'students' in room.keys():
                    if room['id'] == student['room']:
                        room['students'].append(student)
                else:
                    room['students'] = []
        return hostel_list

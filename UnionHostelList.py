from JsonLoader import Loader


class HostelList:
    @staticmethod
    def getting_hostel_list(students_path: str, rooms_path: str):
        students_list = Loader.load(students_path)
        rooms_list = Loader.load(rooms_path)
        hostel_list = rooms_list[:]
        for student in students_list:
                for room in hostel_list:
                    if 'students' in room.keys():
                        if 'room' in student.keys() and room['id'] == student['room']:
                            del student['room']
                            room['students'].append(student)
                    else:
                        room['students'] = []

        return hostel_list

from loader import Loader


class StudentsRoomsMerger:
    @staticmethod
    def merge(students_path: str, rooms_path: str):
        students_list = Loader.load(students_path)
        rooms_list = Loader.load(rooms_path)
        students_rooms_list = rooms_list[:]
        for student in students_list:
                for room in students_rooms_list:
                    if 'students' in room.keys():
                        if 'room' in student.keys() and room['id'] == student['room']:
                            del student['room']
                            room['students'].append(student)
                    else:
                        room['students'] = []

        return students_rooms_list

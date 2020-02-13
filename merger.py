from loader import JsonLoader


class StudentsRoomsMerger:
    @staticmethod
    def merge(students_path: str, rooms_path: str):
        students_list = JsonLoader.load(students_path)
        rooms_list = JsonLoader.load(rooms_path)
        students_rooms_list = rooms_list[:]
        for student in students_list:
            if 'students' in students_rooms_list[student['room']]:
                students_rooms_list[student['room']]['students'].append(student)
            else:
                students_rooms_list[student['room']]['students'] = [student]
        return students_rooms_list

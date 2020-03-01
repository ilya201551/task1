class StudentsRoomsMerger:
    @staticmethod
    def merge(students_list: list, rooms_list: list):
        students_rooms_list = rooms_list[:]
        for student in students_list:
            if 'students' in students_rooms_list[student['room']]:
                students_rooms_list[student['room']]['students'].append(student)
            else:
                students_rooms_list[student['room']]['students'] = [student]
        return students_rooms_list

import json
import xml.etree.ElementTree as ET
from xml.dom import minidom


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


class HostelJson:
    def __init__(self, hostel_list: dict):
        with open('Hostel.json', 'w') as write_file:
            json.dump(hostel_list, write_file, indent=4)


class HostelXml:
    def __init__(self, hostel_list: dict):
        self.hostel_list = hostel_list

    def creating_xml_hostel_list(self):
        new = ET.Element('HostelList')
        for r in self.hostel_list:
            room = ET.SubElement(new, 'room')
            room_id = ET.SubElement(room, 'room_id')
            room_id.text = str(r['id'])
            room_name = ET.SubElement(room, 'room_name')
            room_name.text = str(r['name'])
            students = ET.SubElement(room, 'students')
            for s in r['students']:
                student = ET.SubElement(students, 'student')
                student_id = ET.SubElement(student, 'student_id')
                student_id.text = str(s['id'])
                student_name = ET.SubElement(student, 'student_name')
                student_name.text = str(s['name'])
                student_room_id = ET.SubElement(student, 'student_room_id')
                student_room_id.text = str(s['room'])
            self.save_xml_hostel_list(new)

    def save_xml_hostel_list(self, xml_code):
        xml_string = ET.tostring(xml_code).decode()

        xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
        with open('Hostel.xml', 'w') as xml_file:
            xml_file.write(xml_prettyxml)


class FormattedHostelList:
    def __init__(self, students_path: str, rooms_path: str, format_: str):
        if format_.lower() == 'json':
            HostelJson(HostelList(students_path, rooms_path).hostel_list)
        elif format_.lower() == 'xml':
            HostelXml(HostelList(students_path, rooms_path).hostel_list).creating_xml_hostel_list()


def main():
    FormattedHostelList('students.json', 'room.json', 'json')
    FormattedHostelList('students.json', 'room.json', 'xml')


if __name__ == '__main__':
    main()

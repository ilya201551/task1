import xml.etree.ElementTree as ET
from xml.dom import minidom


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

    @staticmethod
    def save_xml_hostel_list(xml_code):
        xml_string = ET.tostring(xml_code).decode()

        xml_pretty = minidom.parseString(xml_string).toprettyxml()
        with open('Hostel.xml', 'w') as xml_file:
            xml_file.write(xml_pretty)

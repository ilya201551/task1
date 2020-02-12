from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
import json


class Saver:
    @staticmethod
    def save(students_rooms_list: dict, format_: str):
        savers = {
            'json': JsonSaver(),
            'xml': XmlSaver(),
        }
        try:
            return savers[format_.lower()].save(students_rooms_list)
        except KeyError:
            raise ValueError('Invalid format.')


class JsonSaver:
    @staticmethod
    def save(students_rooms_list: dict):
        with open('result.json', 'w') as write_file:
            json.dump(students_rooms_list, write_file, indent=4)


class XmlSaver:
    @staticmethod
    def save(students_rooms_list: dict):
        xml = dicttoxml(students_rooms_list)
        pretty_xml = parseString(xml).toprettyxml()
        with open('result.xml', 'w') as write_file:
            write_file.write(pretty_xml)



import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from abc import abstractmethod, ABC


class Saver(ABC):
    @staticmethod
    @abstractmethod
    def save(students_rooms_list: dict):
        pass


class JsonSaver(Saver):
    @staticmethod
    def save(students_rooms_list: dict):
        with open('result.json', 'w') as write_file:
            json.dump(students_rooms_list, write_file, indent=4)


class XmlSaver(Saver):
    @staticmethod
    def save(students_rooms_list: dict):
        xml = dicttoxml(students_rooms_list)
        pretty_xml = parseString(xml).toprettyxml()
        with open('result.xml', 'w') as write_file:
            write_file.write(pretty_xml)



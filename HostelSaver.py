from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
import json


class Saver:
    def save(self, hostel_list: dict, format_: str):
        if format_.lower() == 'json':
            return self.__saving_json(hostel_list)
        elif format_.lower() == 'xml':
            return self.__saving_xml(hostel_list)
        else:
            raise ValueError('Invalid format.')

    @staticmethod
    def __saving_json(hostel_list: dict):
        with open('Hostel.json', 'w') as write_file:
            json.dump(hostel_list, write_file, indent=4)

    @staticmethod
    def __saving_xml(hostel_list: dict):
        xml = dicttoxml(hostel_list)
        pretty_xml = parseString(xml).toprettyxml()
        with open('Hostel.xml', 'w') as write_file:
            write_file.write(pretty_xml)



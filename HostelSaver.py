from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
import json


class Saver:
    @staticmethod
    def saving_json(hostel_list: dict):
        with open('Hostel.json', 'w') as write_file:
            json.dump(hostel_list, write_file, indent=4)

    @staticmethod
    def saving_xml(hostel_list: dict):
        xml = dicttoxml(hostel_list)
        pretty_xml = parseString(xml).toprettyxml()
        with open('Hostel.xml', 'w') as write_file:
            write_file.write(pretty_xml)

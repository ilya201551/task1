from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


class HostelXml:
    @staticmethod
    def save(hostel_list: dict):
        xml = dicttoxml(hostel_list)
        pretty_xml = parseString(xml).toprettyxml()
        with open('Hostel.json', 'w') as write_file:
            write_file.write(pretty_xml)


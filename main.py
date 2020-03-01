from saver import JsonSaver, XmlSaver
from loader import JsonLoader
from merger import StudentsRoomsMerger
import argparse


def parsing_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('students_path', type=str, help='Path to the students file.')
    parser.add_argument('rooms_path', type=str, help='Path to the rooms file.')
    parser.add_argument('format_', type=str, help='Source file format(json/xml).')
    args = parser.parse_args()
    return args


def main():
    args = parsing_args()
    students_list = JsonLoader.load(args.students_path)
    rooms_list = JsonLoader.load(args.rooms_path)
    students_rooms_list = StudentsRoomsMerger.merge(students_list, rooms_list)

    savers = {
        'json': JsonSaver(),
        'xml': XmlSaver(),
        }
    try:
        return savers[args.format_.lower()].save(students_rooms_list)
    except KeyError:
        raise ValueError('Invalid format.')


if __name__ == '__main__':
    main()

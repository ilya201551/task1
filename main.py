from saver import Saver
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
    students_rooms_list = StudentsRoomsMerger.merge(args.students_path, args.rooms_path)
    Saver().save(students_rooms_list, args.format_)


if __name__ == '__main__':
    main()

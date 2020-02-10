from HostelSaver import Saver
from UnionHostelList import HostelList
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
    hostel_list = HostelList.getting_hostel_list(args.students_path, args.rooms_path)

    if args.format_.lower() == 'json':
        Saver.saving_json(hostel_list)
    elif args.format_.lower() == 'xml':
        Saver.saving_xml(hostel_list)
    else:
        raise ValueError('Invalid format.')


if __name__ == '__main__':
    main()

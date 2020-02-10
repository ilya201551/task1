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
    Saver().save(hostel_list, args.format_)


if __name__ == '__main__':
    main()

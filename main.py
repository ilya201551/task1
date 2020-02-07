from SaveHostelJson import HostelJson
from SaveHostelXml import HostelXml
from UnionHostelList import HostelList
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('students_path', type=str, help='')
    parser.add_argument('rooms_path', type=str, help='')
    parser.add_argument('format_', type=str, help='')
    args = parser.parse_args()

    if args.format_.lower() == 'json':
        HostelJson(HostelList(args.students_path, args.rooms_path).hostel_list)
    elif args.format_.lower() == 'xml':
        HostelXml(HostelList(args.students_path, args.rooms_path).hostel_list).creating_xml_hostel_list()
    else:
        raise ValueError('Invalid format.')


if __name__ == '__main__':
    main()

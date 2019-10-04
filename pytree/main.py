import os
import argparse
from termcolor import colored


def list_files(startpath):
    for root, dirs, files in sorted(os.walk(startpath)):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print colored(('{}{}/'.format(indent, os.path.basename(root))),'blue')
        subindent = ' ' * 4 * (level + 1)
        for f in sorted(files):
            print colored(('{}{}'.format(subindent, f)),'magenta')


def is_valid_path(parser, arg):
    if not os.path.exists(arg):
        parser.error("The path %s does not exist!" % arg)
    else:
        return list_files(arg)  # return an open file handle


def main():
    parser = argparse.ArgumentParser(description="Tree view of all subdirectories")
    parser.add_argument("-l", dest="path", required=True,
                    help="List all subdirectories and files in a tree" ,
                    type=lambda x: is_valid_path(parser, x)
                )
    parser.parse_args()


if __name__ == '__main__':
    main()

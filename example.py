# author        :   ignorantshr
# create_date   :   2020/04/14 10:11 AM
# description   :   example of using mkdown2ReStructuredText

import sys
import getopt
import os

from mkdown2ReStructuredText import mkdown2ReStructuredText as m2r

if __name__ == '__main__':
    tool = m2r()
    s_d = ''
    d_d = ''

    opts, args = getopt.getopt(sys.argv[1:], 's:d:')
    for opt, val in opts:
        if opt == '-s':
            s_d = val
        elif opt == '-d':
            d_d = val

    if len(s_d) == 0 or len(d_d) == 0:
        print("You must provide two arguments, "
              "the first is the source directory/file,"
              " and the second is the destination directory.")
        exit(1)

    if os.path.isdir(d_d):
        if os.path.isfile(s_d):
            tool.convert_from_file(s_d, d_d)
        elif os.path.isdir(s_d):
            tool.convert_from_dir(s_d, d_d)
        else:
            print("Please Check to see if the source directory/file exists."
                  " Or check your permissions")
    else:
        print("Please Check to see if the destination directory exists."
              " Or check your permissions")

# $ python3.6 example.py -s /home/docs/python/test.md -d /tmp
# $ ls /tmp/test.rst

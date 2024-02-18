import re
import sys

def print_usage():
    print('USAGE: python3 regex.py <DATA_FILE> <REGEX>')

def print_match(match):
    if match == None:
        return
    else:
        print(match.group())

# check if data file was passed as command line argument
if len(sys.argv) <= 2:
    print_usage()
    exit()

data_file = sys.argv[1]
regex = sys.argv[2]

with open(data_file, 'r') as data:
    for line in data:
        found = re.search(regex, line)
        print_match(found)

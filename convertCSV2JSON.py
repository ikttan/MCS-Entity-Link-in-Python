# Ian Tan, Copyright (c) 2016
# Data Science Institute, Multimedia University

import csv
import json
import sys
import getopt
import os.path

# Process input arguments
# Assign argv from argument 1 onwards
argv = sys.argv[1:]

inputfile = ''
outputfile = ''

try:
    opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print 'convertCSV2JSON.py -i <inputfile> -o <outputfile>'
    sys.exit(2)

for opt, arg in opts:
    # If asking for help '-h'
    if opt == '-h':
        print 'convertCSV2JSON.py -i <inputfile> -o <outputfile>'
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg

# Next two lines are for debugging only
print 'Input CSV file is "', inputfile
print 'Output JSON file is "', outputfile

if os.path.exists(inputfile):
    # To do: Parameterize the next line, currently only for 2 column CSV file
    csvfile = open(inputfile, 'r')
    fieldnames = ("id", "text")
    reader = csv.DictReader(csvfile, fieldnames)
else:
    print 'Input CSV file not found'
    sys.exit(1)

if (outputfile != ''):
    try:
        jsonfile = open(outputfile, 'w+')
    except OSError:
        print('Hmmmm, cannot open or create file')
else:
    print 'Output JSON file not stated'
    sys.exit(1)

for row in reader:
    json.dump(row, jsonfile)
    # Last entry should remove the ','
    jsonfile.write(',\n')
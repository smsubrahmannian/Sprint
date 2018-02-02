import os
import json
import sys
from os.path import expanduser


def proc_line(line, text_file):
    """
    Extract name and age property from each json blob
    Write them to the given file
    """
    json_text = json.loads(line)
    try:
        name = json_text['name']
        age = json_text['prop']['age']
        if name != '' and age != '':
            text_file.write(str(name) + "\t" + str(age) + '\n')
        else: pass

    except: pass


def write_json(prefix):
    """
    Collect all json files in the directory and process them using proc_line
    """
    json_files = [ x for x in os.listdir(PATH) if x.startswith(prefix) ]

    with open(PATH+str(prefix)+'.txt','w') as text_file: # open file to write

        for item in json_files: # process each file

            with open(os.path.join(PATH, item)) as file:

                for line in file:
                    try: proc_line(line, text_file)
                    except: pass

    text_file.close()

# run prefix
dir = "/srv/runme/"
PATH = expanduser("~") + dir
PREFIX = sys.argv[1]

write_json(PREFIX)


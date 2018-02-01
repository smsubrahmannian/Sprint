import os
import json
import sys
from os.path import expanduser


def proc_line(line, text_file):

    json_text = json.loads(line)
    try:
        text_file.write(str(json_text['name']) + "\t" + str(json_text['prop']['age']) + '\n')
    except:
        pass


def write_json(prefix):

    json_files = [ x for x in os.listdir(PATH) if x.startswith(prefix) ]
    with open(PATH+str(prefix)+'.txt','w') as text_file:

        for item in json_files:

            with open(os.path.join(PATH, item)) as file:

                for line in file:
                    try: proc_line(line, text_file)
                    except: pass

    text_file.close()

# run prefix
dir = "/srv/runme/"
PATH = expanduser("~")+ dir

PREFIX = sys.argv[1]
write_json(PREFIX)

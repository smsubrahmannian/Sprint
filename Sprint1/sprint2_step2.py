import os
import json
import sys


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
    if os.path.exists(PATH):

        json_files = [ x for x in os.listdir(PATH) if x.startswith(prefix) ]

        with open(PATH+str(prefix)+'.txt','w') as text_file: # open file to write

            for item in json_files: # process each file

                with open(os.path.join(PATH, item)) as file:
                    for line in file:
                        try: proc_line(line, text_file)
                        except: pass
                        
    else: print("Directory " + PATH + " does not exist!")

#----------------------------------------------------#

# run script
PATH = "/srv/runme/"

if len(sys.argv)==2: 
    PREFIX = sys.argv[1]
    write_json(PREFIX)
else:
    print("Missing prefix argument")


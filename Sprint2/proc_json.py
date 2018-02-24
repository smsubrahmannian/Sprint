import os
import json
import sys

#-----------------------------------------------------
# JSON File Process
#-----------------------------------------------------

# PATH = "/srv/runme/"

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

    except (KeyError, ValueError): print("JSON format is invalid!") 


def write_json(prefix, path):
    """
    Read json blobs from Raw.txt
    Process them using proc_line and write them to proc.txt
    """
    raw_file_path = path + str(prefix) + '/Raw.txt'

    if os.path.exists(raw_file_path):

        raw_file = open(raw_file_path,'r') # open file to write
        proc_file = open(path + str(prefix) + '/proc.txt', 'w')

        for line in raw_file:
            try: proc_line(line, proc_file)
            except: pass # TODO: Check what kind of error is this
        
        raw_file.close()
        proc_file.close()
                        
    else: print("Directory " + path + " does not exist!")






import os 

#-----------------------------------------------------
# Log File Process
#-----------------------------------------------------
def write_log(prefix, json_str, path):
    """
    Write json strings to the file path of log file
    e.g. /srv/runme/prefix/Raw.txt
    """
    file_path = path + str(prefix)
    
    if os.path.exists(file_path):
        # if path exists, open and write json blobs in the file
        text_file = open(file_path + "/Raw.txt", "a")
        blobs = json_str.split("\n")
        for i, blob in enumerate(blobs): 
            if i != len(blobs): text_file.write(blob+"\n")
            else: text_file.write(blob)
        text_file.close()
    
    else: print("Directory " + file_path + " does not exist!")
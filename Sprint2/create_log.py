import os 

#-----------------------------------------------------
# Log File Process
#-----------------------------------------------------
def write_log(prefix, json_str, path):
    """
    Write json strings to the file path of log file
    e.g. /srv/runme/prefix/Raw.txt
    """
    file_path = path + str(prefix) + "/Raw.txt"
    
    if os.path.exists(file_path):
        # if path exists, open and write json blobs in the file
        text_file = open(file_path, "w")          
        blobs = json_str.split("\n")
        for blob in blobs: text_file.write(blob + "\n")
        text_file.close()
    
    else: print("Directory " + file_path + " does not exist!")
import json

#-----------------------------------------------------
# JSON File Process
#-----------------------------------------------------

def proc_request(request):
    """
    Process a JSON POST request and return the processed string
    """
    blobs = request.split("\n")
    outputs = []

    for blob in blobs:
        try: outputs.append(get_age_name(blob))
        except ValueError: print("No JSON object can be encoded")

    return "\n".join(outputs)

def get_age_name(line):
    """
    Extract and return name and age property from each json blob
    """
    json_text = json.loads(line)

    try: # extract name & age
        name = json_text['name']
        age = json_text['prop']['age']
        # check if name / age exists
        if name != '' and age != '':
            return str(name) + "\t" + str(age)
        else: print("Missing value for name/age")

    except (KeyError, ValueError):
        print("JSON format is invalid!")


# def proc_line(line, text_file):
#     """
#     Extract name and age property from each json blob
#     Write them to the given file
#     """
#     json_text = json.loads(line)
#     try:
#         name = json_text['name']
#         age = json_text['prop']['age']
#         if name != '' and age != '':
#             text_file.write(str(name) + "\t" + str(age) + '\n')
#         else: print("Missing value for name/age")
#
#     except (KeyError, ValueError): print("JSON format is invalid!")
#
# def write_json(path, filename):
#
#     if os.path.exists(path+filename):
#
#         raw_file = open(path+filename, 'r')  # open file to write
#         proc_file = open(path, '/proc.txt', 'a')
#         for line in raw_file:
#             try:
#                 proc_line(line, proc_file)
#             except (ValueError):
#                 print("No JSON object can be encoded")
#         raw_file.close()
#         proc_file.close()
#
#     else: print("No file exists")
# def proc_file(prefix, path):
#     files = [f for f in os.listdir(path + prefix)]
#
#     if len(files) == 1:
#         try: write_json(path+prefix, "Raw.txt")
#         except: pass
#
#     if len(files) > 1:
#         files = [f for f in os.listdir(path+prefix) if f.endswith(".log")]
#         last_file = sorted(files)[:-1]
#         write_json(path + prefix, last_file)



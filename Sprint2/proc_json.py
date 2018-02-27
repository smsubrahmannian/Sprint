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
        try: outputs.append(proc_line(blob))
        except ValueError: print("No JSON object can be encoded")

    return "\n".join(outputs)


def proc_line(line):
    """
    Extract and return name and age property from each json blob
    """
    json_text = json.loads(line)

    try: # extract name & age
        name = json_text['name']
        age = json_text['prop']['age']

        # check if name / age exists and with a correct format
        if name != '' and age != '' and age.isdigit():
            return str(name) + "\t" + str(age)

        else: print("Missing value for name/age")

    except (KeyError, ValueError):
        print("JSON format is invalid!")


directory = "srv/runme/"
prefix = "t"

import os, json

json_files = [x for x in os.listdir(directory) if x.startswith(prefix)]

for item in json_files:
    with open(os.path.join(directory, item)) as file:
        json_text = json.load(file)
        print(json_text)
        print (json_text['name'] + "\t" + str(json_text['prop']['age']))

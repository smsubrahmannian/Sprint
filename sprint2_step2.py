

def prefix(directory,prefix):
    if directory == "srv/sunme/":
        json_files = [x for x in os.listdir(directory) if x.startswith(prefix)  ]
        with open(directory+str(prefix)+'.txt','w') as text_file:
        
            for item in json_files:
            
                with open(os.path.join(directory, item)) as file:
                    
                    for line in file:
                        json_text = json.loads(line)
                        try:
                            text_file.write(str(json_text['name']) + "\t" + str(json_text['prop']['age'])+'\n')
                        except:
                            pass
        text_file.close()

prefix("srv/runme/",prefix)
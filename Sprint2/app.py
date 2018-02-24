from flask import Flask, request
import sys
from create_log import * 
from proc_json import *

#-----------------------------------------------------
# Flask App
#-----------------------------------------------------
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def receive_request():
    """
    Receive and process POST requests from client
    """
    try: 
        content = request.data
        #print(content)
        if content is not None: 
            write_log(PREFIX, content, PATH)  # call create_log
            write_json(PREFIX, PATH) # call proc_json

    except Exception as e: print(e) 
    return "Received data!"


if __name__ == '__main__':

    PATH = "/home/ec2-user/"
    PREFIX = sys.argv[1]
    app.run(host='0.0.0.0', port=8080, debug=True)

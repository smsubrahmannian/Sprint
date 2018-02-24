import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, request
from create_log import *
from proc_json import *

#-----------------------------------------------------
# Flask App
#-----------------------------------------------------

def create_timed_rotating_log(raw_file_path):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(raw_file_path,
                                       when="s",
                                       interval=2,
                                       backupCount=0)
    logger.addHandler(handler)
    with open(raw_file_path, 'r') as raw:
        logger.info(raw.read())


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def receive_request():
    """
    Receive and process POST requests from client
    """
    try:
        content = request.data
        if content is not None:
            create_timed_rotating_log(PATH + PREFIX + "/Raw.txt")
            write_log(PREFIX, content, PATH)  # call create_log
            # write_json(PREFIX, PATH) # call proc_json

    except Exception as e: print(e) 
    return "Received data!"


if __name__ == '__main__':

    PATH = "/Users/ThyKhueLy/msan603/00-sprint/"
    PREFIX = sys.argv[1]
    app.run(host='0.0.0.0', port=8080, debug=True)
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, request
import time
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
        if content is not None:
            LOGGER.info(content)
            # write_log(PREFIX, content, PATH)  # call create_log
            # write_json(PREFIX, PATH) # call proc_json

    except Exception as e: print(e)
    return "Received data!"


if __name__ == '__main__':

    PATH = "/Users/ThyKhueLy/msan603/00-sprint/"
    PREFIX = sys.argv[1]
    log_filename = PATH + PREFIX + "/Raw.txt"
    LOGGER = logging.getLogger('MyLogger')
    LOGGER.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(log_filename,
                                       when="s",
                                       interval=30,
                                       backupCount=0)
    handler.suffix = "%Y%m%d-%H%M%s.log"
    LOGGER.addHandler(handler)
    app.run(host='0.0.0.0', port=8080, debug=True)
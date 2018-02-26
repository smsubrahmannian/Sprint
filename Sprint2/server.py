import sys
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, request
from proc_json import *

#-----------------------------------------------------
# Setup Log Rotate
#-----------------------------------------------------

def setup_logger(log_filepath, logger_name):
    """
    Set up a logger that rotates every 30s
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(log_filepath, when="s", interval=30, backupCount=0)
    handler.suffix = "%Y%m%d-%H%M%s.log"
    logger.addHandler(handler)

    return logger

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
            logger_raw.info(content) # add raw data to Raw.txt
            processed_line = proc_request(content) # process the raw data
            logger_proc.info(processed_line) # add processed data to proc.txt

    except Exception as e: print(e)
    return "Received data"


if __name__ == '__main__':

    # TODO: change to /srv/runme/
    # i = sys.argv.index('server:app')
    PREFIX = sys.argv[1]
    PATH = "/home/ec2-user/"

    # create loggers
    if os.path.exists(PATH + PREFIX):

        raw_filename = PATH + PREFIX + "/Raw.txt"
        proc_filename = PATH + PREFIX + "/proc.txt"

        logger_raw = setup_logger(raw_filename, "logger_raw")
        logger_proc = setup_logger(proc_filename, "logger_proc")

    # app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
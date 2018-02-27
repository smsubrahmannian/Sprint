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
    Set up a logger that rotates every 2 minutes
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(log_filepath, when="m", interval=2, backupCount=0)
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
        logger_raw.info(content) # add raw data to Raw.txt
        processed_line = proc_request(content) # process the raw data
        logger_proc.info(processed_line) # add processed data to proc.txt

    except Exception as e: print(e)
    return "Received data!"


@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    """
    Shutting down server
    """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None: os._exit(0)
    else: func()
    return 'Server is shutting down...'


if __name__ == '__main__':

    # TODO: change to /srv/runme/
    PREFIX = sys.argv[1]
    PATH = "/home/ec2-user/"

    # create loggers
    if os.path.exists(PATH + PREFIX):

        raw_filename = PATH + PREFIX + "/Raw.txt"
        proc_filename = PATH + PREFIX + "/proc.txt"

        logger_raw = setup_logger(raw_filename, "logger_raw")
        logger_proc = setup_logger(proc_filename, "logger_proc")

        print("Server is currently running")
        print("Press Cltr+Z to suspend and go to server_address:8080/shutdown to completely shut down the process")

        app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)

    else: print("Directory %s does not exist" % (PATH + PREFIX))


## EOF ##
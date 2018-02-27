#!/usr/bin/env python

import paramiko
import os

def execute_command(command, client):
    """
    Execute a command given a ssh client
    """
    stdin, stdout, stderr = client.exec_command(command)
    out, err = (stdout.read(), stderr.read())
    if len(out) > 0: print(out)
    if len(err) > 0: print(err)

    return None


def deploy(key_path, host, prefix):
    """
    Connect to server
    Build a Flask app server to receive and process POST requests
    """
    git_repo = 'https://github.com/smsubrahmannian/Sprint.git'
    server_file = 'sprint/Sprint2/server.py '

    print("Connecting to box")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, username="testtest", key_filename=key_path)
        print('Connected')

        execute_command("rm -rf sprint; git clone %s sprint" % git_repo, ssh) # clone git repo
        execute_command('pkill python', ssh) # kill all processes with python
        execute_command('pkill gunicorn', ssh)  # kill all processes with gunicorn

        print("Server is currently running")
        print("Press Cltr+Z to suspend and go to server_address:8080/shutdown to completely shut down the process")

        execute_command('python ' + server_file + prefix, ssh) # set up server

        ssh.close()

    except Exception as e: print(e)

# if __name__ == '__main__':

    # key_path = "/Users/ThyKhueLy/msan630/msan630_maisely.pem"
    # server_address = "ec2-52-35-129-27.us-west-2.compute.amazonaws.com"
    # prefix = "storm"
    # deploy(key_path, server_address, prefix)


## EOF ##

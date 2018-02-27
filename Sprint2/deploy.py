#!/usr/bin/env python

import paramiko
import os
import subprocess
import signal
import socket

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

    print("Connecting to box")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, username="ec2-user", key_filename=key_path)
        print('Connected')

        git_repo = 'https://github.com/smsubrahmannian/Sprint.git'
        execute_command("rm -rf sprint; git clone %s sprint" % git_repo, ssh) # clone git repo

        execute_command('pkill python', ssh) # kill all processes with python
        execute_command('pkill gunicorn', ssh)  # kill all processes with gunicorn

        print("Server is currently running\nPress Cltr+Z to stop")
        print("Go to %s:8080/shutdown to completely shut down the process" % server_address)
        server_file = 'sprint/Sprint2/server.py '
        execute_command('python ' + server_file + prefix, ssh) # set up server

        ssh.close()

    except Exception as e: print(e)

if __name__ == '__main__':

    key_path = "/Users/ThyKhueLy/msan630/msan630_maisely.pem"
    server_address = "ec2-54-202-4-108.us-west-2.compute.amazonaws.com"
    prefix = "storm"
    deploy(key_path, server_address, prefix)

## EOF ##

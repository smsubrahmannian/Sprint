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
        execute_command('pkill gunicorn', ssh)  # kill all processes with python

        # gunicorn_command = 'gunicorn -D -b 0.0.0.0:8080 server:app %s' % prefix
        # execute_command('cd sprint/Sprint2; ' + gunicorn_command, ssh)

        print("Server is currently running\nPress Cltr+Z to stop")
        server_file = 'sprint/Sprint2/server.py '
        execute_command('python ' + server_file + prefix, ssh) # set up server

        ssh.close()

    except Exception as e: print(e)

if __name__ == '__main__':

    # key_path = "/Users/ThyKhueLy/msan630/msan630_maisely.pem"
    key_path = "/Users/maisely/maise_tally.pem"
    server_address = "ec2-52-33-35-38.us-west-2.compute.amazonaws.com"
    prefix = "t"
    deploy(key_path, server_address, prefix)

## EOF ##

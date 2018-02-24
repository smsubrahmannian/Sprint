#!/usr/bin/env python

import paramiko
import time
# import sys

def deploy(key_path, host, prefix):
    print "Connecting to box"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username="ec2-user", key_filename=key_path)
        print('Connected\n')
        time.sleep(2)
        print('Running commands\n')

        crontab_command = "echo '*/5 * * * * python sprint/sprint2_step2.py " + prefix + "' >> mycron"

        commands = ["rm -rf sprint; git clone https://github.com/smsubrahmannian/Sprint.git sprint",
                    "crontab -r",
                    "rm -rf mycron",
                    "rm -rf /srv/runme/" + prefix + ".txt",
                    "crontab -l > mycron",
                    crontab_command,
                    "crontab mycron"]

        for command in commands:
                print command
                stdin, stdout, stderr = ssh.exec_command(command)
                out, err = (stdout.read(), stderr.read())
                if len(out) > 0: print out
                if len(err) > 0: print err

        ssh.close()

    except: print("Connection error, check the pem file and/or server")


#---------------------------------------------------------------------------#

# Input
# key_path = "/Users/ThyKhueLy/msan630/msan630_maisely.pem"
# server_address = "ec2-54-245-199-99.us-west-2.compute.amazonaws.com"
# prefix = "t"
# Call deploy

# deploy(key_path, server_address, prefix)


## EOF ##

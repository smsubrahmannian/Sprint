#!/usr/bin/env python

import paramiko
import time
# import sys

def deploy(key_path, host, prefix):

    print "Connecting to box"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=user, key_filename=key_path)
        #ssh.invoke_shell()
        print('Connected\n')
        time.sleep(2)
        print('Running commands\n')
        time.sleep(2)

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
                if len(out) > 0:
                        print out
                if len(err) > 0:
                        print err
                time.sleep(2)

        ssh.close()

    except: print("Connection error, check the pem file and/or server")


#---------------------------------------------------------------------------#

# Input
user = "ec2-user"
key_path = "/Users/ThyKhueLy/msan630/msan630_maisely.pem"
server_address = "ec2-54-245-199-99.us-west-2.compute.amazonaws.com"
prefix = "t"
# Call deploy
deploy(key_path, server_address, prefix)


# # check if all variables are provided
# if len(sys.argv)==4:
#         key_path = sys.argv[1]
#         host = sys.argv[2]
#         prefix = sys.argv[3]
#         user = 'ec2-user' # ML: Isn't this going to be 'testtest'?
#         deploy(key_path, host, prefix)
# else:
#         print("Missing parameters, please check!")


## EOF ##

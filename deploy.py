#!/usr/bin/env python

import paramiko
import time
import sys

# #Change these for your instance
# key_path = '/Users/davischum/Documents/classes/aws/sprint.pem'
# host = 'ec2-54-191-242-17.us-west-2.compute.amazonaws.com'

key_path = sys.argv[1]
host = sys.argv[2]
prefix = sys.argv[3]
user = 'ec2-user'

def deploy(key_path, host, prefix):

	print "Connecting to box"
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, username=user, key_filename=key_path)
	print 'Connected\n'
	time.sleep(1)

	print 'Running commands\n'
	time.sleep(1)

	crontab_command = "echo '* * * * * python sprint/sprint2_step2.py "+prefix+"' >> mycron"
	commands = ["if [ ! -d 'sprint' ]; then git clone https://github.com/smsubrahmannian/Sprint.git sprint; fi",
				"rm -f -- /srv/runme/" + prefix + ".txt",
				"crontab -l > mycron", crontab_command,
				"crontab mycron"]

	for command in commands:
		print command
		stdin, stdout, stderr = ssh.exec_command(command)
		out, err = (stdout.read(), stderr.read())
		if len(out) > 0:
			print out
		if len(err) > 0:
			print err
		time.sleep(1)

	ssh.close()

deploy(key_path, host, prefix)

## EOF ##

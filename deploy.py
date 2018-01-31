#!/usr/bin/env python

import paramiko
import time

#Change these for your instance
key_path = '/Users/davischum/Documents/classes/aws/sprint.pem'
host = 'ec2-54-203-87-49.us-west-2.compute.amazonaws.com'
user = 'ec2-user'

print "Connecting to box"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=user, key_filename=key_path)
print 'Connected\n'
time.sleep(1)

print 'Running commands\n'
time.sleep(1)

commands = ["pwd", "mkdir fartface", "ls" , "rm fartface", "rm -r fartface", "ls"]
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
## EOF ##

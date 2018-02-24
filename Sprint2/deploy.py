import paramiko


def deploy(key_path, host, prefix):
	print("Connecting to box")
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	run_py_file = 'python receive_request.py ' + prefix
	try:
		ssh.connect(hostname=host, username="ec2-user", key_filename=key_path)
		print('Connected\n')

		commands = ["rm -rf sprint; git clone https://github.com/smsubrahmannian/Sprint.git sprint",
		            "screen -dmS sprintScreen", "screen -S sprintScreen -p 0 -X stuff 'cd sprint \n'",
		            "screen -S sprintScreen -p 0 -X stuff 'ls \n'"]

		for command in commands:
			stdin, stdout, stderr = ssh.exec_command(command)
			out, err = (stdout.read(), stderr.read())
			if len(out) > 0: print(out)
			if len(err) > 0: print(err)

		ssh.close()

	except:
		print("Connection error, check the pem file and/or server")


if __name__ == '__main__':
	import sys

	key_path = sys.argv[1]
	server_address = sys.argv[2]
	prefix = sys.argv[3]
	deploy(key_path, server_address, prefix)

## EOF ##

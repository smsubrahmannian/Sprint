import paramiko
import sys


def deploy(key_path, host, prefix):
    print("Connecting to box")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    server_file = "sprint/Sprint2/receive_request.py " + prefix

    try:
        ssh.connect(hostname=host, username="ec2-user", key_filename=key_path)
        print('Connected\n')

        commands = ["rm -rf sprint; git clone https://github.com/smsubrahmannian/Sprint.git sprint",
                    "echo 'Server is currently running...'",
                    "echo 'Press Ctrl+Z to stop'",
                    "python " + server_file ]

        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            out, err = (stdout.read(), stderr.read())
            if len(out) > 0: print(out)
            if len(err) > 0: print(err)

        print("Server is shutting down...")
        ssh.close()

    except:
        print("Connection error, check the pem file and/or server")


if __name__ == '__main__':
    key_path = "/Users/davischum/Documents/classes/aws/sprint.pem"
    server_address = "ec2-34-217-13-160.us-west-2.compute.amazonaws.com"
    prefix = "t"
    deploy(key_path, server_address, prefix)

## EOF ##

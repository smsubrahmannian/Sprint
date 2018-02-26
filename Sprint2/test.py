import subprocess, signal
import os

def kill_process(name):
    """
    Kill a process using its name
    """
    process = subprocess.Popen("ps cax | grep %s" % name,
                                shell=True, stdout=subprocess.PIPE)

    outputs, errors = process.communicate()
    for proc in outputs.splitlines():
        proc_id = proc.split(None, 1)
        os.kill(proc_id, signal.SIGKILL)
import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd: 
        return
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr=subprocess.STDOUT)
    return output.decode()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP NET Tool',
        fomatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            netcat.py -t 192.168.1.108 -p 5555 -1 -c # command shell
            netcat.py -t 192.168.1.108 -p 5555 -1 -u=mytest.txt # upload to file
            netcat.py -t 192.168.1.108 -p 5555 -1 -e=\"cat /etc/passwd\" # executive command 
            echo 'ABC' | ./netcat.py -t 192.168.108 -p 135 # echo text to server port 135
            netcat.py -t 192.168.1.108 -p 5555 # connect to server                                                           
            '''))
parser.add_argument('-c', '--command', action='store_true', help ='command shell')
parser.add_argument('-e', '--execute', help='execute specified command')
parser.add_argument('-1', '--listen', action='store_true', help ='listen')
parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')    
__author__ = 'sancheng'

'''
a function to excute batch commands via python through SSH

dependency:
1. paramiko
2. Pycrypto

the commond would be:

python sshbatch.py your_host_config.txt

the your host_config.txt would be like this :

host=192.168.0.1
port=22
user=test
pwd=testpwd

'''

import paramiko
import Crypto
import time
import sys


def exec_cmd(channel,commands):

    for c in commands:
        if(len(c.strip()) == 0):
            continue;
        channel.send(c + '\n')
        while not channel.recv_ready():
            time.sleep(2)
        output = channel.recv(4096)
        print output


if(len( sys.argv) <=1):
    exit(-1)

batch_file = sys.argv[1]

f = open(batch_file)
batch_cmds = f.readlines()
f.close()

dict = {}
for line in batch_cmds:
    dict[line.split('=')[0]] = line.split('=')[1].strip()



print 'connecting to : ', dict

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(dict['host'],port=int(dict['port']),username=dict['user'], password=dict['pwd'])

channel = ssh.invoke_shell()
#stdin = channel.makefile('wb')
#stdout = channel.makefile('rb')

#the command set can be added into a file
cmds = '''
su - root
blabla
cd /usr/local/debugger
ll | grep server.log$
tail -10 server.log
exit
'''

exec_cmd(channel,cmds.split('\n'))



#print stdout.read()

#stdout.close()
#stdin.close()
ssh.close()
#print stdout.read()
#print stdout.read()


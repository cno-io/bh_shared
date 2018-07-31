#!/usr/local/bin/python

with open("cnoio_cntr_list.txt") as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

sDockerRunOptions = "-v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap"

for sLine in content:
	print("")
	print("function cnoio_"+sLine+"() {")
	print("    docker run "+sDockerRunOptions+" cnoio/"+sLine+" $@")
	print("}")

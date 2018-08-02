import urllib2
import time

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

__author__ = '@TweekFawkes'
__website__ = 'Stage2Sec.com'
__blog__ = 'https://Stage2Sec.com/blog/2017/11/13/automating-aws-ec2-metadata-service-enumeration'

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

'''

--- SoMeta - AWS EC2 Metadata Service Enumeration - Alpha v0.0.3 ---

This script automates the collection of secrets within user data, roles, and public keys.
You can do this all by hand via curl from most instances but this can also be tedious in more complex AWS environments hence many attackers skip these steps.
Also, SoMeta does not rely on curl being installed on the endpoint which may be a plus in more hardened environments and/or container centric environments.
See blog post for more details: https://Stage2Sec.com/blog/2017/11/13/automating-aws-ec2-metadata-service-enumeration


--- Example Usage ---

# python soMeta.py


 _____      ___  ___     _
/  ___|     |  \/  |    | |
\ `--.  ___ | .  . | ___| |_ __ _
 `--. \/ _ \| |\/| |/ _ \ __/ _` |
/\__/ / (_) | |  | |  __/ || (_| |
\____/ \___/\_|  |_/\___|\__\__,_|



Alpha v0.0.3

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
Instance ID
[+] URL: http://169.254.169.254/latest/meta-data/ami-id
[+] Content: ami-0a00ce72
--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
...


--- References ---

- Instance Metadata and User Data
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html

- Instance Metadata Categories
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-categories


'''

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

sVersion = 'Alpha v0.0.3'
sStartUrl = 'http://169.254.169.254/latest/' 
iSleepInterval = 2 # 2 second sleep to avoid hammering the metadata service
sLineBreak = "--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- "

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

def newUrl(sUrl, sLine):
    if sUrl.endswith('/'):
        sNewUrl = sUrl + sLine
    else:
        sNewUrl = sUrl + '/' + sLine
    return sNewUrl

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

def curlMetadataService(sUrl):
    try:
        oResponse = urllib2.urlopen(sUrl)
        iResponseCode = oResponse.getcode()
        sResponseCode = str(iResponseCode)
        sResponseHeader = oResponse.info()
        sResponseContent = oResponse.read()
        #
        if iResponseCode == 200:
            print("[+] URL: " + sUrl)
            print("[+] Content: " + sResponseContent)
    except:
        print("[!] URL Failed: " + sUrl)

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

print("""

 _____      ___  ___     _        
/  ___|     |  \/  |    | |       
\ `--.  ___ | .  . | ___| |_ __ _ 
 `--. \/ _ \| |\/| |/ _ \ __/ _` |
/\__/ / (_) | |  | |  __/ || (_| |
\____/ \___/\_|  |_/\___|\__\__,_|
                                  
                                  
""")

print(sVersion + "\n")

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

print(sLineBreak)
print("Instance ID")
sUrl = 'http://169.254.169.254/latest/meta-data/ami-id'
curlMetadataService(sUrl)

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

print(sLineBreak)
print("Internet Facing Hostname")
sUrl = 'http://169.254.169.254/latest/meta-data/public-hostname'
curlMetadataService(sUrl)

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

print(sLineBreak)
print("Internal Hostname")
sUrl = 'http://169.254.169.254/latest/meta-data/local-hostname'
curlMetadataService(sUrl)

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

print(sLineBreak)
print("User Data (e.g. boot strap scripts)")
sUrl = 'http://169.254.169.254/latest/user-data'
curlMetadataService(sUrl)

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

print(sLineBreak)
print("IAM roles associated with the instance")
sUrl = 'http://169.254.169.254/latest/meta-data/iam/security-credentials/'
try:
    oResponse = urllib2.urlopen(sUrl)
    iResponseCode = oResponse.getcode()
    sResponseCode = str(iResponseCode)
    sResponseHeader = oResponse.info()
    sResponseContent = oResponse.read()
    if iResponseCode == 200:
        #print(sResponseContent)
        lResponseContent = sResponseContent.splitlines()
        for sLine in lResponseContent:
            sNewUrl = newUrl(sUrl, sLine)
            try:
                oResponse = urllib2.urlopen(sNewUrl)
                iResponseCode = oResponse.getcode()
                sResponseCode = str(iResponseCode)
                sResponseHeader = oResponse.info()
                sResponseContent = oResponse.read()
                if iResponseCode == 200:
                    print("[+] URL: " + sNewUrl)
                    print("[+] Content: " + sResponseContent)
            except:
                print("[!] URL Failed: " + sNewUrl)
except:
    print("[!] URL Failed: " + sUrl)

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

print(sLineBreak)
print("Public Keys")
sUrl = 'http://169.254.169.254/latest/meta-data/public-keys/'
try:
    oResponse = urllib2.urlopen(sUrl)
    iResponseCode = oResponse.getcode()
    sResponseCode = str(iResponseCode)
    sResponseHeader = oResponse.info()
    sResponseContent = oResponse.read()
    if iResponseCode == 200:
        #print(sResponseContent)
        lResponseContent = sResponseContent.splitlines()
        for sLine in lResponseContent:
            sLine = sLine[:1]
            sNewUrl = newUrl(sUrl, sLine)
            try:
                oResponse = urllib2.urlopen(sNewUrl)
                iResponseCode = oResponse.getcode()
                sResponseCode = str(iResponseCode)
                sResponseHeader = oResponse.info()
                sResponseContent = oResponse.read()
                if iResponseCode == 200:
                    try:
                        sNewNewUrl = newUrl(sNewUrl, sResponseContent)
                        oResponse = urllib2.urlopen(sNewNewUrl)
                        iResponseCode = oResponse.getcode()
                        sResponseCode = str(iResponseCode)
                        sResponseHeader = oResponse.info()
                        sResponseContent = oResponse.read()
                        if iResponseCode == 200:
                            print("[+] URL: " + sNewNewUrl)
                            print("[+] Content: " + sResponseContent)
                    except:
                        print("[!] URL Failed: " + sNewNewUrl)
            except:
                print("[!] URL Failed: " + sNewUrl)
except:
    print("[!] URL Failed: " + sUrl)

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

print(sLineBreak)
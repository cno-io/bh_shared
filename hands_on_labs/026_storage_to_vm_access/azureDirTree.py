
#!/usr/bin/python
"""
Ubuntu 16.04

apt-get upgrade
apt-get -y install python
apt-get -y install python-pip

pip install azure
pip install azure-storage-blob

"""

import azure
import azure.storage
import azure.storage.blob

blob_service = azure.storage.blob.baseblobservice.BaseBlobService(account_name='rg001disks543', account_key='Fp8Ub...3IkRQ==')

containers = blob_service.list_containers() 
for sContainer in containers:
	sContainerName = str(sContainer.name)
	print("[+] sContainerName: " + str(sContainerName))
	marker = None
	while True:
		blobs = blob_service.list_blobs(sContainerName, marker=marker)
		for blob in blobs:
			sBlobName = str(blob.name)
			print("[+] sBlobName: " + str(sBlobName))
		if blobs.next_marker:
			marker = blobs.next_marker
		else:
			break

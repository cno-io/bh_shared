import json
import urllib
import boto3
import gzip
import tempfile
import shutil
 
dirty_tag = "18.191.208.172"
 
def filter_dirty_tag(log):
    return dirty_tag in json.dumps(log)
     
s3 = boto3.client('s3')
 
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
    resp = s3.get_object(Bucket=bucket, Key=key)
    gzip_tmp = tempfile.NamedTemporaryFile(delete=False)
    shutil.copyfileobj(resp['Body'], gzip_tmp)
    gzip_tmp.close()
 
    gzip_filename = gzip_tmp.name
    with gzip.open(gzip_filename, 'rb') as f:
        file_content = f.read()
 
    logs = json.loads(file_content)
 
    old_num_logs = len(logs['Records'])
    print old_num_logs
    logs['Records'] = filter(lambda x: not filter_dirty_tag(x), logs['Records'])
    print len(logs['Records'])
 
    if len(logs['Records']) == 0:
        print "Deleting empty %s" % key
        s3.delete_object(Bucket=bucket, Key=key)
    elif len(logs['Records']) == old_num_logs:
        print "Doing nothing no log records filtered"
    else:
        print "Updating %s" % key
        with gzip.open(gzip_filename, 'wb') as f:
            f.write(json.dumps(logs, separators=(',',':')))
        s3.put_object(Bucket=bucket, Key=key, Body=open(gzip_filename, 'rb'))
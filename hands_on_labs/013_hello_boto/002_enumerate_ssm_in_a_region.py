import boto3
session = boto3.Session(profile_name='vulnlambda')
ssmClient = session.client("ssm", 'us-east-1')
params = ssmClient.describe_parameters()
for p in params['Parameters']:
    p_name = p['Name']
    response = ssmClient.get_parameter(
        Name=p_name)
    val = response['Parameter']['Value']
    print "%s - %s" % (p_name, val)

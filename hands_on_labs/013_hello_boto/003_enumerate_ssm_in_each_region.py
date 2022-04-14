import boto3
session = boto3.Session(profile_name='vulnlambda')
ec2 = session.client("ec2", "us-east-1")
regions = ec2.describe_regions()
regions = [r['RegionName'] for r in regions['Regions']]
for r in regions:
    print("Region: " + r)
    ssmClient = session.client("ssm", r)
    params = ssmClient.describe_parameters()
    for p in params['Parameters']:
        p_name = p['Name']
        response = ssmClient.get_parameter(
            Name=p_name)
        val = response['Parameter']['Value']
        print(str(p_name) + " - " + str(val))

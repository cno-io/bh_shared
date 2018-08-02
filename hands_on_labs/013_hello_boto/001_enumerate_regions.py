import boto3
session = boto3.Session(profile_name='lambdavuln')
ec2 = session.client("ec2",)
regions = ec2.describe_regions()
regions = [r['RegionName'] for r in regions['Regions']]
for r in regions:
    print r
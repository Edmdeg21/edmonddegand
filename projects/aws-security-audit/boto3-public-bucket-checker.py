import boto3

s3 = boto3.client('s3')

def check_public_buckets():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl['Grants']:
            if 'AllUsers' in str(grant['Grantee']):
                print(f"⚠️ Public Bucket Found: {bucket_name}")

if __name__ == "__main__":
    check_public_buckets()

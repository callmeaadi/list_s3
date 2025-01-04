import boto3
from botocore.exceptions import ClientError
import os

bucket_name = os.environ["BUCKET_NAME"]

def lambda_handler(event, context):

    raw_path = event["rawPath"]
    try:
        if raw_path == "" or raw_path == "/":
            conn = boto3.client('s3')  
            response_from_s3 = conn.list_objects_v2(Bucket=bucket_name, Prefix=raw_path[1:],Delimiter='/')
    

            if "CommonPrefixes" in response_from_s3:
                prefixes = [prefix['Prefix'] for prefix in response_from_s3['CommonPrefixes']]
                result = {"content": prefixes}
                print(result)
                return(result)
            else:
                print({"content": []})
                return({"content": []})
        else:
            conn = boto3.client('s3')  
            response_from_s3 = conn.list_objects(Bucket=bucket_name, Prefix=raw_path[1:])
            #print(response_from_s3)
            if "Contents" in response_from_s3:
                prefixes = [prefix['Key'].split('/')[-1] for prefix in response_from_s3['Contents']]
                result = {"content": prefixes[1:]}
                print(result)
                return(result)
            else:
                print({"content": ["not found"]})
                return({"content": ["not found"]})
    except ClientError as e:
        print({"error":e})
        return({"error":f'{e}'})
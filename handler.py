import boto3
from botocore.exceptions import ClientError

def generate_presigned_url(bucket_name, object_name):
    print(f"--- Attempting to generate link for {object_name} in {bucket_name} ---")
    s3_client = boto3.client('s3')
    try:
        url = s3_client.generate_presigned_url('get_object',
                                              Params={'Bucket': bucket_name, 'Key': object_name},
                                              ExpiresIn=3600)
        return url
    except Exception as e:
        print(f"--- ERROR: {e} ---")
        return None

if __name__ == "__main__":
    # Ensure this matches the bucket you saw in the AWS Console!
    MY_BUCKET = "YOUR-BUCKET-NAME-HERE" 
    MY_FILE = "test.mp3"
    
    generated_link = generate_presigned_url(MY_BUCKET, MY_FILE)
    
    if generated_link:
        print("\n✅ SUCCESS! COPY THIS LINK:")
        print(generated_link)
        print("\n")
    else:
        print("\n❌ FAILED to create link.")

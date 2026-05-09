import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET


def _get_s3_client():
    """Create S3 client. Returns None if credentials are not configured."""
    if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
        return None
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION,
    )


def upload_to_s3(file_path, key):
    """Upload a file to S3. Skips silently if credentials are missing."""
    s3 = _get_s3_client()
    if s3 is None:
        print("S3 upload skipped: AWS credentials not configured.")
        return
    try:
        s3.upload_file(file_path, S3_BUCKET, key)
        print(f"Uploaded {file_path} → s3://{S3_BUCKET}/{key}")
    except (NoCredentialsError, ClientError) as e:
        print(f"S3 upload failed: {e}")


def download_from_s3(key, local_path):
    """Download a file from S3. Skips silently if credentials are missing."""
    s3 = _get_s3_client()
    if s3 is None:
        print("S3 download skipped: AWS credentials not configured.")
        return
    try:
        s3.download_file(S3_BUCKET, key, local_path)
        print(f"Downloaded s3://{S3_BUCKET}/{key} → {local_path}")
    except (NoCredentialsError, ClientError) as e:
        print(f"S3 download failed: {e}")



# CanaryCodeInput

Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script was passed into the canary directly, the script code is contained in the value of <code>Zipfile</code>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**s3Bucket** | [**String**](String.md) |  |  [optional] |
|**s3Key** | [**String**](String.md) |  |  [optional] |
|**s3Version** | [**String**](String.md) |  |  [optional] |
|**zipFile** | [**String**](String.md) |  |  [optional] |
|**handler** | [**String**](String.md) |  |  |




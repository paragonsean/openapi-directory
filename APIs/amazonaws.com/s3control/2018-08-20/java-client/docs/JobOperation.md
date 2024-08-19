

# JobOperation

The operation that you want this job to perform on every object listed in the manifest. For more information about the available operations, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html\">Operations</a> in the <i>Amazon S3 User Guide</i>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lambdaInvoke** | [**CreateJobRequestOperationLambdaInvoke**](CreateJobRequestOperationLambdaInvoke.md) |  |  [optional] |
|**s3PutObjectCopy** | [**CreateJobRequestOperationS3PutObjectCopy**](CreateJobRequestOperationS3PutObjectCopy.md) |  |  [optional] |
|**s3PutObjectAcl** | [**CreateJobRequestOperationS3PutObjectAcl**](CreateJobRequestOperationS3PutObjectAcl.md) |  |  [optional] |
|**s3PutObjectTagging** | [**CreateJobRequestOperationS3PutObjectTagging**](CreateJobRequestOperationS3PutObjectTagging.md) |  |  [optional] |
|**s3DeleteObjectTagging** | [**Object**](Object.md) |  |  [optional] |
|**s3InitiateRestoreObject** | [**CreateJobRequestOperationS3InitiateRestoreObject**](CreateJobRequestOperationS3InitiateRestoreObject.md) |  |  [optional] |
|**s3PutObjectLegalHold** | [**S3SetObjectLegalHoldOperation**](S3SetObjectLegalHoldOperation.md) |  |  [optional] |
|**s3PutObjectRetention** | [**S3SetObjectRetentionOperation**](S3SetObjectRetentionOperation.md) |  |  [optional] |
|**s3ReplicateObject** | [**Object**](Object.md) |  |  [optional] |




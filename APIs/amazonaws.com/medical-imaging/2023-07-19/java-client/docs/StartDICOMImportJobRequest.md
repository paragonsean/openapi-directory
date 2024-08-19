

# StartDICOMImportJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobName** | **String** | The import job name. |  [optional] |
|**dataAccessRoleArn** | **String** | The Amazon Resource Name (ARN) of the IAM role that grants permission to access medical imaging resources. |  |
|**clientToken** | **String** | A unique identifier for API idempotency. |  |
|**inputS3Uri** | **String** | The input prefix path for the S3 bucket that contains the DICOM files to be imported. |  |
|**outputS3Uri** | **String** | The output prefix of the S3 bucket to upload the results of the DICOM import job. |  |




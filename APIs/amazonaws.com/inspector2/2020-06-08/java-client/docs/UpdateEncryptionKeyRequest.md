

# UpdateEncryptionKeyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKeyId** | **String** | A KMS key ID for the encryption key. |  |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | The resource type for the encryption key. |  |
|**scanType** | [**ScanTypeEnum**](#ScanTypeEnum) | The scan type for the encryption key. |  |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| EC2_INSTANCE | &quot;AWS_EC2_INSTANCE&quot; |
| ECR_CONTAINER_IMAGE | &quot;AWS_ECR_CONTAINER_IMAGE&quot; |
| ECR_REPOSITORY | &quot;AWS_ECR_REPOSITORY&quot; |
| LAMBDA_FUNCTION | &quot;AWS_LAMBDA_FUNCTION&quot; |



## Enum: ScanTypeEnum

| Name | Value |
|---- | -----|
| NETWORK | &quot;NETWORK&quot; |
| PACKAGE | &quot;PACKAGE&quot; |
| CODE | &quot;CODE&quot; |




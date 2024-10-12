# Inspector2.UpdateEncryptionKeyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kmsKeyId** | **String** | A KMS key ID for the encryption key. | 
**resourceType** | **String** | The resource type for the encryption key. | 
**scanType** | **String** | The scan type for the encryption key. | 



## Enum: ResourceTypeEnum


* `EC2_INSTANCE` (value: `"AWS_EC2_INSTANCE"`)

* `ECR_CONTAINER_IMAGE` (value: `"AWS_ECR_CONTAINER_IMAGE"`)

* `ECR_REPOSITORY` (value: `"AWS_ECR_REPOSITORY"`)

* `LAMBDA_FUNCTION` (value: `"AWS_LAMBDA_FUNCTION"`)





## Enum: ScanTypeEnum


* `NETWORK` (value: `"NETWORK"`)

* `PACKAGE` (value: `"PACKAGE"`)

* `CODE` (value: `"CODE"`)





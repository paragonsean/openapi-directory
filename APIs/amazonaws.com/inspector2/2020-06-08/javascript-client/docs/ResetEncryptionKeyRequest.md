# Inspector2.ResetEncryptionKeyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceType** | **String** | The resource type the key encrypts. | 
**scanType** | **String** | The scan type the key encrypts. | 



## Enum: ResourceTypeEnum


* `EC2_INSTANCE` (value: `"AWS_EC2_INSTANCE"`)

* `ECR_CONTAINER_IMAGE` (value: `"AWS_ECR_CONTAINER_IMAGE"`)

* `ECR_REPOSITORY` (value: `"AWS_ECR_REPOSITORY"`)

* `LAMBDA_FUNCTION` (value: `"AWS_LAMBDA_FUNCTION"`)





## Enum: ScanTypeEnum


* `NETWORK` (value: `"NETWORK"`)

* `PACKAGE` (value: `"PACKAGE"`)

* `CODE` (value: `"CODE"`)





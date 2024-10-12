# CloudSpannerApi.EncryptionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionStatus** | [**Status**](Status.md) |  | [optional] 
**encryptionType** | **String** | Output only. The type of encryption. | [optional] [readonly] 
**kmsKeyVersion** | **String** | Output only. A Cloud KMS key version that is being used to protect the database or backup. | [optional] [readonly] 



## Enum: EncryptionTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `GOOGLE_DEFAULT_ENCRYPTION` (value: `"GOOGLE_DEFAULT_ENCRYPTION"`)

* `CUSTOMER_MANAGED_ENCRYPTION` (value: `"CUSTOMER_MANAGED_ENCRYPTION"`)





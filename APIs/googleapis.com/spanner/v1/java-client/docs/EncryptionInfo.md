

# EncryptionInfo

Encryption information for a Cloud Spanner database or backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionStatus** | [**Status**](Status.md) |  |  [optional] |
|**encryptionType** | [**EncryptionTypeEnum**](#EncryptionTypeEnum) | Output only. The type of encryption. |  [optional] [readonly] |
|**kmsKeyVersion** | **String** | Output only. A Cloud KMS key version that is being used to protect the database or backup. |  [optional] [readonly] |



## Enum: EncryptionTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| GOOGLE_DEFAULT_ENCRYPTION | &quot;GOOGLE_DEFAULT_ENCRYPTION&quot; |
| CUSTOMER_MANAGED_ENCRYPTION | &quot;CUSTOMER_MANAGED_ENCRYPTION&quot; |




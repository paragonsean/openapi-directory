

# EncryptionInfo

EncryptionInfo describes the encryption information of a cluster or a backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionType** | [**EncryptionTypeEnum**](#EncryptionTypeEnum) | Output only. Type of encryption. |  [optional] [readonly] |
|**kmsKeyVersions** | **List&lt;String&gt;** | Output only. Cloud KMS key versions that are being used to protect the database or the backup. |  [optional] [readonly] |



## Enum: EncryptionTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| GOOGLE_DEFAULT_ENCRYPTION | &quot;GOOGLE_DEFAULT_ENCRYPTION&quot; |
| CUSTOMER_MANAGED_ENCRYPTION | &quot;CUSTOMER_MANAGED_ENCRYPTION&quot; |




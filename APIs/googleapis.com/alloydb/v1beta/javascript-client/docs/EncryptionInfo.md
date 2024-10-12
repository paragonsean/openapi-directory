# AlloyDbApi.EncryptionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionType** | **String** | Output only. Type of encryption. | [optional] [readonly] 
**kmsKeyVersions** | **[String]** | Output only. Cloud KMS key versions that are being used to protect the database or the backup. | [optional] [readonly] 



## Enum: EncryptionTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `GOOGLE_DEFAULT_ENCRYPTION` (value: `"GOOGLE_DEFAULT_ENCRYPTION"`)

* `CUSTOMER_MANAGED_ENCRYPTION` (value: `"CUSTOMER_MANAGED_ENCRYPTION"`)





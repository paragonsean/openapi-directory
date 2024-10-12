# CloudSpannerApi.RestoreDatabaseEncryptionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionType** | **String** | Required. The encryption type of the restored database. | [optional] 
**kmsKeyName** | **String** | Optional. The Cloud KMS key that will be used to encrypt/decrypt the restored database. This field should be set only when encryption_type is &#x60;CUSTOMER_MANAGED_ENCRYPTION&#x60;. Values are of the form &#x60;projects//locations//keyRings//cryptoKeys/&#x60;. | [optional] 



## Enum: EncryptionTypeEnum


* `ENCRYPTION_TYPE_UNSPECIFIED` (value: `"ENCRYPTION_TYPE_UNSPECIFIED"`)

* `USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION` (value: `"USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION"`)

* `GOOGLE_DEFAULT_ENCRYPTION` (value: `"GOOGLE_DEFAULT_ENCRYPTION"`)

* `CUSTOMER_MANAGED_ENCRYPTION` (value: `"CUSTOMER_MANAGED_ENCRYPTION"`)





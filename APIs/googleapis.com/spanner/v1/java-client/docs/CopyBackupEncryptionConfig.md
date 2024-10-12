

# CopyBackupEncryptionConfig

Encryption configuration for the copied backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionType** | [**EncryptionTypeEnum**](#EncryptionTypeEnum) | Required. The encryption type of the backup. |  [optional] |
|**kmsKeyName** | **String** | Optional. The Cloud KMS key that will be used to protect the backup. This field should be set only when encryption_type is &#x60;CUSTOMER_MANAGED_ENCRYPTION&#x60;. Values are of the form &#x60;projects//locations//keyRings//cryptoKeys/&#x60;. |  [optional] |



## Enum: EncryptionTypeEnum

| Name | Value |
|---- | -----|
| ENCRYPTION_TYPE_UNSPECIFIED | &quot;ENCRYPTION_TYPE_UNSPECIFIED&quot; |
| USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION | &quot;USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION&quot; |
| GOOGLE_DEFAULT_ENCRYPTION | &quot;GOOGLE_DEFAULT_ENCRYPTION&quot; |
| CUSTOMER_MANAGED_ENCRYPTION | &quot;CUSTOMER_MANAGED_ENCRYPTION&quot; |






# StorageDomainProperties

The storage domain properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionKey** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  |  [optional] |
|**encryptionStatus** | [**EncryptionStatusEnum**](#EncryptionStatusEnum) | The encryption status \&quot;Enabled | Disabled\&quot;. |  |
|**storageAccountCredentialIds** | **List&lt;String&gt;** | The storage account credentials. |  |



## Enum: EncryptionStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |




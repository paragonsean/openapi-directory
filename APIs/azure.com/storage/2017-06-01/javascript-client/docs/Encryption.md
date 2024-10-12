# StorageManagement.Encryption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keySource** | **String** | The encryption keySource (provider). Possible values (case-insensitive):  Microsoft.Storage, Microsoft.Keyvault | [default to &#39;Microsoft.Storage&#39;]
**keyvaultproperties** | [**KeyVaultProperties**](KeyVaultProperties.md) |  | [optional] 
**services** | [**EncryptionServices**](EncryptionServices.md) |  | [optional] 



## Enum: KeySourceEnum


* `Storage` (value: `"Microsoft.Storage"`)

* `Keyvault` (value: `"Microsoft.Keyvault"`)





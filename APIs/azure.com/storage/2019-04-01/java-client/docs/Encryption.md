

# Encryption

The encryption settings on the storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keySource** | [**KeySourceEnum**](#KeySourceEnum) | The encryption keySource (provider). Possible values (case-insensitive):  Microsoft.Storage, Microsoft.Keyvault |  |
|**keyvaultproperties** | [**KeyVaultProperties**](KeyVaultProperties.md) |  |  [optional] |
|**services** | [**EncryptionServices**](EncryptionServices.md) |  |  [optional] |



## Enum: KeySourceEnum

| Name | Value |
|---- | -----|
| STORAGE | &quot;Microsoft.Storage&quot; |
| KEYVAULT | &quot;Microsoft.Keyvault&quot; |




# KeyVaultClient.StorageAccountCreateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeKeyName** | **String** | Current active storage account key name. | 
**attributes** | [**StorageAccountAttributes**](StorageAccountAttributes.md) |  | [optional] 
**autoRegenerateKey** | **Boolean** | whether keyvault should manage the storage account for the user. | 
**regenerationPeriod** | **String** | The key regeneration time duration specified in ISO-8601 format. | [optional] 
**resourceId** | **String** | Storage account resource id. | 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs. | [optional] 



# KeyVaultClient.DeletedStorageBundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletedDate** | **Number** | The time when the storage account was deleted, in UTC | [optional] [readonly] 
**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted storage account. | [optional] 
**scheduledPurgeDate** | **Number** | The time when the storage account is scheduled to be purged, in UTC | [optional] [readonly] 
**activeKeyName** | **String** | The current active storage account key name. | [optional] [readonly] 
**attributes** | [**StorageAccountAttributes**](StorageAccountAttributes.md) |  | [optional] 
**autoRegenerateKey** | **Boolean** | whether keyvault should manage the storage account for the user. | [optional] [readonly] 
**id** | **String** | The storage account id. | [optional] [readonly] 
**regenerationPeriod** | **String** | The key regeneration time duration specified in ISO-8601 format. | [optional] [readonly] 
**resourceId** | **String** | The storage account resource id. | [optional] [readonly] 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs | [optional] [readonly] 



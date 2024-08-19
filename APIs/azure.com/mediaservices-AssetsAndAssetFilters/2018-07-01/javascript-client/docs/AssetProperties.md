# AzureMediaServices.AssetProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateId** | **String** | The alternate ID of the Asset. | [optional] 
**assetId** | **String** | The Asset ID. | [optional] [readonly] 
**container** | **String** | The name of the asset blob container. | [optional] 
**created** | **Date** | The creation date of the Asset. | [optional] [readonly] 
**description** | **String** | The Asset description. | [optional] 
**lastModified** | **Date** | The last modified date of the Asset. | [optional] [readonly] 
**storageAccountName** | **String** | The name of the storage account. | [optional] 
**storageEncryptionFormat** | **String** | The Asset encryption format. One of None or MediaStorageEncryption. | [optional] [readonly] 



## Enum: StorageEncryptionFormatEnum


* `None` (value: `"None"`)

* `MediaStorageClientEncryption` (value: `"MediaStorageClientEncryption"`)





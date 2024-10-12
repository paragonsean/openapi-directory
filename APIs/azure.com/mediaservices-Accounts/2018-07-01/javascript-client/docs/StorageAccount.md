# AzureMediaServices.StorageAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The ID of the storage account resource. Media Services relies on tables and queues as well as blobs, so the primary storage account must be a Standard Storage account (either Microsoft.ClassicStorage or Microsoft.Storage). Blob only storage accounts can be added as secondary storage accounts. | [optional] 
**type** | **String** | The type of the storage account. | 



## Enum: TypeEnum


* `Primary` (value: `"Primary"`)

* `Secondary` (value: `"Secondary"`)





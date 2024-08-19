# DiskResourceProviderClient.CreationData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createOption** | **String** | This enumerates the possible sources of a disk&#39;s creation. | 
**imageReference** | [**ImageDiskReference**](ImageDiskReference.md) |  | [optional] 
**sourceResourceId** | **String** | If createOption is Copy, this is the ARM id of the source snapshot or disk. | [optional] 
**sourceUri** | **String** | If createOption is Import, this is the URI of a blob to be imported into a managed disk. | [optional] 
**storageAccountId** | **String** | If createOption is Import, the Azure Resource Manager identifier of the storage account containing the blob to import as a disk. Required only if the blob is in a different subscription | [optional] 



## Enum: CreateOptionEnum


* `Empty` (value: `"Empty"`)

* `Attach` (value: `"Attach"`)

* `FromImage` (value: `"FromImage"`)

* `Import` (value: `"Import"`)

* `Copy` (value: `"Copy"`)

* `Restore` (value: `"Restore"`)





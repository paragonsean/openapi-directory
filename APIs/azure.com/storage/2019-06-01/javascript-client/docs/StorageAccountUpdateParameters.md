# StorageManagementClient.StorageAccountUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**Identity**](Identity.md) |  | [optional] 
**kind** | **String** | Optional. Indicates the type of storage account. Currently only StorageV2 value supported by server. | [optional] 
**properties** | [**StorageAccountPropertiesUpdateParameters**](StorageAccountPropertiesUpdateParameters.md) |  | [optional] 
**sku** | [**StorageAccountCreateParametersSku**](StorageAccountCreateParametersSku.md) |  | [optional] 
**tags** | **{String: String}** | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. | [optional] 



## Enum: KindEnum


* `Storage` (value: `"Storage"`)

* `StorageV2` (value: `"StorageV2"`)

* `BlobStorage` (value: `"BlobStorage"`)

* `FileStorage` (value: `"FileStorage"`)

* `BlockBlobStorage` (value: `"BlockBlobStorage"`)





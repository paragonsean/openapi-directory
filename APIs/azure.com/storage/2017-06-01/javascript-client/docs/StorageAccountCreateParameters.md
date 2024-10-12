# StorageManagement.StorageAccountCreateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**Identity**](Identity.md) |  | [optional] 
**kind** | **String** | Required. Indicates the type of storage account. | 
**location** | **String** | Required. Gets or sets the location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo region is specified on update, the request will succeed. | 
**properties** | [**StorageAccountPropertiesCreateParameters**](StorageAccountPropertiesCreateParameters.md) |  | [optional] 
**sku** | [**Sku**](Sku.md) |  | 
**tags** | **{String: String}** | Gets or sets a list of key value pairs that describe the resource. These tags can be used for viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key with a length no greater than 128 characters and a value with a length no greater than 256 characters. | [optional] 



## Enum: KindEnum


* `Storage` (value: `"Storage"`)

* `BlobStorage` (value: `"BlobStorage"`)





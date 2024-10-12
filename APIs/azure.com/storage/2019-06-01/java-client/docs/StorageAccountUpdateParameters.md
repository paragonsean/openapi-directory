

# StorageAccountUpdateParameters

The parameters that can be provided when updating the storage account properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identity** | [**Identity**](Identity.md) |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Optional. Indicates the type of storage account. Currently only StorageV2 value supported by server. |  [optional] |
|**properties** | [**StorageAccountPropertiesUpdateParameters**](StorageAccountPropertiesUpdateParameters.md) |  |  [optional] |
|**sku** | [**StorageAccountCreateParametersSku**](StorageAccountCreateParametersSku.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| STORAGE | &quot;Storage&quot; |
| STORAGE_V2 | &quot;StorageV2&quot; |
| BLOB_STORAGE | &quot;BlobStorage&quot; |
| FILE_STORAGE | &quot;FileStorage&quot; |
| BLOCK_BLOB_STORAGE | &quot;BlockBlobStorage&quot; |




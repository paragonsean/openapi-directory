

# StorageAccount

The storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identity** | [**Identity**](Identity.md) |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Gets the Kind. |  [optional] [readonly] |
|**properties** | [**StorageAccountProperties**](StorageAccountProperties.md) |  |  [optional] |
|**sku** | [**Sku**](Sku.md) |  |  [optional] |
|**id** | **String** | Resource Id |  [optional] [readonly] |
|**location** | **String** | Resource location |  [optional] |
|**name** | **String** | Resource name |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Tags assigned to a resource; can be used for viewing and grouping a resource (across resource groups). |  [optional] |
|**type** | **String** | Resource type |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| STORAGE | &quot;Storage&quot; |
| STORAGE_V2 | &quot;StorageV2&quot; |
| BLOB_STORAGE | &quot;BlobStorage&quot; |




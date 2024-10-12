

# StorageAccount

The storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identity** | [**Identity**](Identity.md) |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Gets the Kind. |  [optional] [readonly] |
|**properties** | [**StorageAccountProperties**](StorageAccountProperties.md) |  |  [optional] |
|**sku** | [**Sku**](Sku.md) |  |  [optional] |
|**location** | **String** | The geo-location where the resource lives |  |
|**tags** | **Map&lt;String, String&gt;** | Resource tags. |  [optional] |
|**id** | **String** | Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |  [optional] [readonly] |
|**name** | **String** | The name of the resource |  [optional] [readonly] |
|**type** | **String** | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| STORAGE | &quot;Storage&quot; |
| STORAGE_V2 | &quot;StorageV2&quot; |
| BLOB_STORAGE | &quot;BlobStorage&quot; |
| FILE_STORAGE | &quot;FileStorage&quot; |
| BLOCK_BLOB_STORAGE | &quot;BlockBlobStorage&quot; |




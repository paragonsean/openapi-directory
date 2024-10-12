# StorageManagementClient.StorageAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**Identity**](Identity.md) |  | [optional] 
**kind** | **String** | Gets the Kind. | [optional] [readonly] 
**properties** | [**StorageAccountProperties**](StorageAccountProperties.md) |  | [optional] 
**sku** | [**Sku**](Sku.md) |  | [optional] 
**location** | **String** | The geo-location where the resource lives | 
**tags** | **{String: String}** | Resource tags. | [optional] 
**id** | **String** | Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} | [optional] [readonly] 
**name** | **String** | The name of the resource | [optional] [readonly] 
**type** | **String** | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. | [optional] [readonly] 



## Enum: KindEnum


* `Storage` (value: `"Storage"`)

* `StorageV2` (value: `"StorageV2"`)

* `BlobStorage` (value: `"BlobStorage"`)

* `FileStorage` (value: `"FileStorage"`)

* `BlockBlobStorage` (value: `"BlockBlobStorage"`)





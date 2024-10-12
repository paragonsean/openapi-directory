# VertexAiSearchForRetailApi.GoogleCloudRetailV2alphaAddLocalInventoriesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addMask** | **String** | Indicates which inventory fields in the provided list of LocalInventory to update. The field is updated to the provided value. If a field is set while the place does not have a previous local inventory, the local inventory at that store is created. If a field is set while the value of that field is not provided, the original field value, if it exists, is deleted. If the mask is not set or set with empty paths, all inventory fields will be updated. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored. | [optional] 
**addTime** | **String** | The time when the inventory updates are issued. Used to prevent out-of-order updates on local inventory fields. If not provided, the internal system time will be used. | [optional] 
**allowMissing** | **Boolean** | If set to true, and the Product is not found, the local inventory will still be processed and retained for at most 1 day and processed once the Product is created. If set to false, a NOT_FOUND error is returned if the Product is not found. | [optional] 
**localInventories** | [**[GoogleCloudRetailV2alphaLocalInventory]**](GoogleCloudRetailV2alphaLocalInventory.md) | Required. A list of inventory information at difference places. Each place is identified by its place ID. At most 3000 inventories are allowed per request. | [optional] 



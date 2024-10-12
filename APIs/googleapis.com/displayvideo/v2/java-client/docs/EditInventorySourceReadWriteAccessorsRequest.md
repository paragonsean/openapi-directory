

# EditInventorySourceReadWriteAccessorsRequest

Request message for InventorySourceService.EditInventorySourceReadWriteAccessors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertisersUpdate** | [**EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdate**](EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdate.md) |  |  [optional] |
|**assignPartner** | **Boolean** | Set the partner context as read/write accessor of the inventory source. This will remove all other current read/write advertiser accessors. |  [optional] |
|**partnerId** | **String** | Required. The partner context by which the accessors change is being made. |  [optional] |




# SquareConnectApi.InventoryChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment** | [**InventoryAdjustment**](InventoryAdjustment.md) |  | [optional] 
**measurementUnit** | [**CatalogMeasurementUnit**](CatalogMeasurementUnit.md) |  | [optional] 
**measurementUnitId** | **String** | The ID of the [CatalogMeasurementUnit](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogMeasurementUnit) object representing the catalog measurement unit associated with the inventory change. | [optional] 
**physicalCount** | [**InventoryPhysicalCount**](InventoryPhysicalCount.md) |  | [optional] 
**transfer** | [**InventoryTransfer**](InventoryTransfer.md) |  | [optional] 
**type** | **String** | Indicates how the inventory change is applied. See [InventoryChangeType](https://developer.squareup.com/reference/square_2021-08-18/enums/InventoryChangeType) for all possible values. | [optional] 



# SquareConnectApi.InventoryPhysicalCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogObjectId** | **String** | The Square-generated ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) being tracked. | [optional] 
**catalogObjectType** | **String** | The [type](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) being tracked. Tracking is only supported for the &#x60;ITEM_VARIATION&#x60; type. | [optional] 
**createdAt** | **String** | An RFC 3339-formatted timestamp that indicates when the physical count is received. | [optional] 
**employeeId** | **String** | The Square-generated ID of the [Employee](https://developer.squareup.com/reference/square_2021-08-18/objects/Employee) responsible for the physical count. | [optional] 
**id** | **String** | A unique Square-generated ID for the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount). | [optional] 
**locationId** | **String** | The Square-generated ID of the [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the related quantity of items is being tracked. | [optional] 
**occurredAt** | **String** | A client-generated RFC 3339-formatted timestamp that indicates when the physical count was examined. For physical count updates, the &#x60;occurred_at&#x60; timestamp cannot be older than 24 hours or in the future relative to the time of the request. | [optional] 
**quantity** | **String** | The number of items affected by the physical count as a decimal string. The number can support up to 5 digits after the decimal point. | [optional] 
**referenceId** | **String** | An optional ID provided by the application to tie the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to an external system. | [optional] 
**source** | [**SourceApplication**](SourceApplication.md) |  | [optional] 
**state** | **String** | The current [inventory state](https://developer.squareup.com/reference/square_2021-08-18/enums/InventoryState) for the related quantity of items. | [optional] 



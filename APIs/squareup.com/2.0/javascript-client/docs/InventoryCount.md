# SquareConnectApi.InventoryCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculatedAt** | **String** | An RFC 3339-formatted timestamp that indicates when the most recent physical count or adjustment affecting the estimated count is received. | [optional] 
**catalogObjectId** | **String** | The Square-generated ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) being tracked. | [optional] 
**catalogObjectType** | **String** | The [type](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) being tracked. Tracking is only supported for the &#x60;ITEM_VARIATION&#x60; type. | [optional] 
**isEstimated** | **Boolean** | Whether the inventory count is for composed variation (TRUE) or not (FALSE). If true, the inventory count will not be present in the response of any of these endpoints: [BatchChangeInventory](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-change-inventory),  [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes),  [BatchRetrieveInventoryCounts](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-counts), and  [RetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-changes). | [optional] 
**locationId** | **String** | The Square-generated ID of the [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the related quantity of items is being tracked. | [optional] 
**quantity** | **String** | The number of items affected by the estimated count as a decimal string. Can support up to 5 digits after the decimal point. | [optional] 
**state** | **String** | The current [inventory state](https://developer.squareup.com/reference/square_2021-08-18/enums/InventoryState) for the related quantity of items. | [optional] 



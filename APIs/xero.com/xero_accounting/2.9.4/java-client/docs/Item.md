

# Item


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | User defined item code (max length &#x3D; 30) |  |
|**description** | **String** | The sales description of the item (max length &#x3D; 4000) |  [optional] |
|**inventoryAssetAccountCode** | **String** | The inventory asset account for the item. The account must be of type INVENTORY. The  COGSAccountCode in PurchaseDetails is also required to create a tracked item |  [optional] |
|**isPurchased** | **Boolean** | Boolean value, defaults to true. When IsPurchased is true the item is available for purchase transactions in the Xero UI. If IsPurchased is updated to false then PurchaseDescription and PurchaseDetails values will be nulled. |  [optional] |
|**isSold** | **Boolean** | Boolean value, defaults to true. When IsSold is true the item will be available on sales transactions in the Xero UI. If IsSold is updated to false then Description and SalesDetails values will be nulled. |  [optional] |
|**isTrackedAsInventory** | **Boolean** | True for items that are tracked as inventory. An item will be tracked as inventory if the InventoryAssetAccountCode and COGSAccountCode are set. |  [optional] |
|**itemID** | **UUID** | The Xero identifier for an Item |  [optional] |
|**name** | **String** | The name of the item (max length &#x3D; 50) |  [optional] |
|**purchaseDescription** | **String** | The purchase description of the item (max length &#x3D; 4000) |  [optional] |
|**purchaseDetails** | [**Purchase**](Purchase.md) |  |  [optional] |
|**quantityOnHand** | **Double** | The quantity of the item on hand |  [optional] |
|**salesDetails** | [**Purchase**](Purchase.md) |  |  [optional] |
|**statusAttributeString** | **String** | Status of object |  [optional] |
|**totalCostPool** | **Double** | The value of the item on hand. Calculated using average cost accounting. |  [optional] |
|**updatedDateUTC** | **String** | Last modified date in UTC format |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |




# AccountingApi.InvoiceItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** |  | [optional] 
**assetAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**code** | **String** | User defined item code | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**description** | **String** | A short description of the item | [optional] 
**expenseAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**id** | **String** | The ID of the item. | [optional] [readonly] 
**incomeAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**inventoryDate** | **Date** | The date of opening balance if inventory item is tracked - YYYY-MM-DD. | [optional] 
**name** | **String** | Item name | [optional] 
**purchaseDetails** | [**InvoiceItemPurchaseDetails**](InvoiceItemPurchaseDetails.md) |  | [optional] 
**purchased** | **Boolean** | Item is available for purchase transactions | [optional] 
**quantity** | **Number** |  | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**salesDetails** | [**InvoiceItemPurchaseDetails**](InvoiceItemPurchaseDetails.md) |  | [optional] 
**sold** | **Boolean** | Item will be available on sales transactions | [optional] 
**taxable** | **Boolean** | If true, transactions for this item are taxable | [optional] 
**tracked** | **Boolean** | Item is inventoried | [optional] 
**trackingCategory** | [**LinkedTrackingCategory**](LinkedTrackingCategory.md) |  | [optional] 
**type** | **String** | Item type | [optional] 
**unitPrice** | **Number** |  | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: TypeEnum


* `inventory` (value: `"inventory"`)

* `service` (value: `"service"`)

* `other` (value: `"other"`)





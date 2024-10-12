# AccountingApi.BillLineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | User defined item code | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**departmentId** | **String** | Department id | [optional] 
**description** | **String** | User defined description | [optional] 
**discountAmount** | **Number** | Discount amount applied to the line item when supported downstream. | [optional] 
**discountPercentage** | **Number** | Discount percentage applied to the line item when supported downstream. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**item** | [**LinkedInvoiceItem**](LinkedInvoiceItem.md) |  | [optional] 
**ledgerAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**lineNumber** | **Number** | Line number in the invoice | [optional] 
**locationId** | **String** | Location id | [optional] 
**quantity** | **Number** |  | [optional] 
**rowId** | **String** | Row ID | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**taxAmount** | **Number** | Tax amount | [optional] 
**taxRate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**totalAmount** | **Number** | Total amount of the line item | [optional] 
**type** | **String** | Bill Line Item type | [optional] 
**unitOfMeasure** | **String** | Description of the unit type the item is sold as, ie: kg, hour. | [optional] 
**unitPrice** | **Number** |  | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: TypeEnum


* `item` (value: `"expense_item"`)

* `account` (value: `"expense_account"`)





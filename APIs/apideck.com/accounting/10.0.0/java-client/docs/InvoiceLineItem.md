

# InvoiceLineItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | User defined item code |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**departmentId** | **String** | Department id |  [optional] |
|**description** | **String** | User defined description |  [optional] |
|**discountAmount** | **BigDecimal** | Discount amount applied to the line item when supported downstream. |  [optional] |
|**discountPercentage** | **BigDecimal** | Discount percentage applied to the line item when supported downstream. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**item** | [**LinkedInvoiceItem**](LinkedInvoiceItem.md) |  |  [optional] |
|**ledgerAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  |  [optional] |
|**lineNumber** | **Integer** | Line number in the invoice |  [optional] |
|**locationId** | **String** | Location id |  [optional] |
|**quantity** | **BigDecimal** |  |  [optional] |
|**rowId** | **String** | Row ID |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**taxAmount** | **BigDecimal** | Tax amount |  [optional] |
|**taxRate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  |  [optional] |
|**totalAmount** | **BigDecimal** | Total amount of the line item |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Item type |  [optional] |
|**unitOfMeasure** | **String** | Description of the unit type the item is sold as, ie: kg, hour. |  [optional] |
|**unitPrice** | **BigDecimal** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SALES_ITEM | &quot;sales_item&quot; |
| DISCOUNT | &quot;discount&quot; |
| INFO | &quot;info&quot; |
| SUB_TOTAL | &quot;sub_total&quot; |




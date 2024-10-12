

# PurchaseOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountingByRow** | **Boolean** | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row. |  [optional] |
|**bankAccount** | [**BankAccount**](BankAccount.md) |  |  [optional] |
|**channel** | **String** | The channel through which the transaction is processed. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**currencyRate** | **BigDecimal** | Currency Exchange Rate at the time entity was recorded/generated. |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**deliveryDate** | **LocalDate** | The date on which the purchase order is to be delivered - YYYY-MM-DD. |  [optional] |
|**discountPercentage** | **BigDecimal** | Discount percentage applied to this transaction. |  [optional] |
|**downstreamId** | **String** | The third-party API ID of original entity |  [optional] [readonly] |
|**dueDate** | **LocalDate** | The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD. |  [optional] |
|**expectedArrivalDate** | **LocalDate** | The date on which the order is expected to arrive - YYYY-MM-DD. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**issuedDate** | **LocalDate** | Date purchase order was issued - YYYY-MM-DD. |  [optional] |
|**ledgerAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  |  [optional] |
|**lineItems** | [**List&lt;InvoiceLineItem&gt;**](InvoiceLineItem.md) |  |  [optional] |
|**memo** | **String** | Message for the supplier. This text appears on the Purchase Order. |  [optional] |
|**paymentMethod** | **String** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check |  [optional] |
|**poNumber** | **String** | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. |  [optional] |
|**reference** | **String** | Optional purchase order reference. |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**shippingAddress** | [**Address**](Address.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**subTotal** | **BigDecimal** | Sub-total amount, normally before tax. |  [optional] |
|**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  |  [optional] |
|**taxCode** | **String** | Applicable tax id/code override if tax is not supplied on a line item basis. |  [optional] |
|**taxInclusive** | **Boolean** | Amounts are including tax |  [optional] |
|**templateId** | **String** | Optional purchase order template |  [optional] |
|**total** | **BigDecimal** | Total amount of invoice, including tax. |  [optional] |
|**totalTax** | **BigDecimal** | Total tax amount applied to this invoice. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| OPEN | &quot;open&quot; |
| CLOSED | &quot;closed&quot; |
| DELETED | &quot;deleted&quot; |
| BILLED | &quot;billed&quot; |
| OTHER | &quot;other&quot; |




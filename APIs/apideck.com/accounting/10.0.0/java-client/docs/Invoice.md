

# Invoice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountingByRow** | **Boolean** | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row. |  [optional] |
|**balance** | **BigDecimal** | Balance of invoice due. |  [optional] |
|**bankAccount** | [**BankAccount**](BankAccount.md) |  |  [optional] |
|**billingAddress** | [**Address**](Address.md) |  |  [optional] |
|**channel** | **String** | The channel through which the transaction is processed. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**currencyRate** | **BigDecimal** | Currency Exchange Rate at the time entity was recorded/generated. |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  |  [optional] |
|**customerMemo** | **String** | Customer memo |  [optional] |
|**deposit** | **BigDecimal** | Amount of deposit made to this invoice. |  [optional] |
|**discountAmount** | **BigDecimal** | Discount amount applied to this invoice. |  [optional] |
|**discountPercentage** | **BigDecimal** | Discount percentage applied to this invoice. |  [optional] |
|**downstreamId** | **String** | The third-party API ID of original entity |  [optional] [readonly] |
|**dueDate** | **LocalDate** | The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**invoiceDate** | **LocalDate** | Date invoice was issued - YYYY-MM-DD. |  [optional] |
|**invoiceSent** | **Boolean** | Invoice sent to contact/customer. |  [optional] |
|**language** | **String** | language code according to ISO 639-1. For the United States - EN |  [optional] |
|**ledgerAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  |  [optional] |
|**lineItems** | [**List&lt;InvoiceLineItem&gt;**](InvoiceLineItem.md) |  |  [optional] |
|**number** | **String** | Invoice number. |  [optional] |
|**paymentMethod** | **String** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check |  [optional] |
|**poNumber** | **String** | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order. |  [optional] |
|**reference** | **String** | Optional invoice reference. |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**shippingAddress** | [**Address**](Address.md) |  |  [optional] |
|**sourceDocumentUrl** | **String** | URL link to a source document - shown as &#39;Go to [appName]&#39; in the downstream app. Currently only supported for Xero. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Invoice status |  [optional] |
|**subTotal** | **BigDecimal** | Sub-total amount, normally before tax. |  [optional] |
|**taxCode** | **String** | Applicable tax id/code override if tax is not supplied on a line item basis. |  [optional] |
|**taxInclusive** | **Boolean** | Amounts are including tax |  [optional] |
|**templateId** | **String** | Optional invoice template |  [optional] |
|**terms** | **String** | Terms of payment. |  [optional] |
|**total** | **BigDecimal** | Total amount of invoice, including tax. |  [optional] |
|**totalTax** | **BigDecimal** | Total tax amount applied to this invoice. |  [optional] |
|**trackingCategory** | [**LinkedTrackingCategory**](LinkedTrackingCategory.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Invoice type |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| SUBMITTED | &quot;submitted&quot; |
| AUTHORISED | &quot;authorised&quot; |
| PARTIALLY_PAID | &quot;partially_paid&quot; |
| PAID | &quot;paid&quot; |
| VOID | &quot;void&quot; |
| CREDIT | &quot;credit&quot; |
| DELETED | &quot;deleted&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |
| CREDIT | &quot;credit&quot; |
| SERVICE | &quot;service&quot; |
| PRODUCT | &quot;product&quot; |
| SUPPLIER | &quot;supplier&quot; |
| OTHER | &quot;other&quot; |




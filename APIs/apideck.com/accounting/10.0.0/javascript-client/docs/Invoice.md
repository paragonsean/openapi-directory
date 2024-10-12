# AccountingApi.Invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountingByRow** | **Boolean** | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row. | [optional] 
**balance** | **Number** | Balance of invoice due. | [optional] 
**bankAccount** | [**BankAccount**](BankAccount.md) |  | [optional] 
**billingAddress** | [**Address**](Address.md) |  | [optional] 
**channel** | **String** | The channel through which the transaction is processed. | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currencyRate** | **Number** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  | [optional] 
**customerMemo** | **String** | Customer memo | [optional] 
**deposit** | **Number** | Amount of deposit made to this invoice. | [optional] 
**discountAmount** | **Number** | Discount amount applied to this invoice. | [optional] 
**discountPercentage** | **Number** | Discount percentage applied to this invoice. | [optional] 
**downstreamId** | **String** | The third-party API ID of original entity | [optional] [readonly] 
**dueDate** | **Date** | The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**invoiceDate** | **Date** | Date invoice was issued - YYYY-MM-DD. | [optional] 
**invoiceSent** | **Boolean** | Invoice sent to contact/customer. | [optional] 
**language** | **String** | language code according to ISO 639-1. For the United States - EN | [optional] 
**ledgerAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**lineItems** | [**[InvoiceLineItem]**](InvoiceLineItem.md) |  | [optional] 
**number** | **String** | Invoice number. | [optional] 
**paymentMethod** | **String** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check | [optional] 
**poNumber** | **String** | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order. | [optional] 
**reference** | **String** | Optional invoice reference. | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**shippingAddress** | [**Address**](Address.md) |  | [optional] 
**sourceDocumentUrl** | **String** | URL link to a source document - shown as &#39;Go to [appName]&#39; in the downstream app. Currently only supported for Xero. | [optional] 
**status** | **String** | Invoice status | [optional] 
**subTotal** | **Number** | Sub-total amount, normally before tax. | [optional] 
**taxCode** | **String** | Applicable tax id/code override if tax is not supplied on a line item basis. | [optional] 
**taxInclusive** | **Boolean** | Amounts are including tax | [optional] 
**templateId** | **String** | Optional invoice template | [optional] 
**terms** | **String** | Terms of payment. | [optional] 
**total** | **Number** | Total amount of invoice, including tax. | [optional] 
**totalTax** | **Number** | Total tax amount applied to this invoice. | [optional] 
**trackingCategory** | [**LinkedTrackingCategory**](LinkedTrackingCategory.md) |  | [optional] 
**type** | **String** | Invoice type | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: StatusEnum


* `draft` (value: `"draft"`)

* `submitted` (value: `"submitted"`)

* `authorised` (value: `"authorised"`)

* `partially_paid` (value: `"partially_paid"`)

* `paid` (value: `"paid"`)

* `void` (value: `"void"`)

* `credit` (value: `"credit"`)

* `deleted` (value: `"deleted"`)





## Enum: TypeEnum


* `standard` (value: `"standard"`)

* `credit` (value: `"credit"`)

* `service` (value: `"service"`)

* `product` (value: `"product"`)

* `supplier` (value: `"supplier"`)

* `other` (value: `"other"`)





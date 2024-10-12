# AccountingApi.Bill

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountingByRow** | **Boolean** | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row. | [optional] 
**balance** | **Number** | Balance of bill due. | [optional] 
**bankAccount** | [**BankAccount**](BankAccount.md) |  | [optional] 
**billDate** | **Date** | Date bill was issued - YYYY-MM-DD. | [optional] 
**billNumber** | **String** | Reference to supplier bill number | [optional] 
**channel** | **String** | The channel through which the transaction is processed. | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currencyRate** | **Number** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**deposit** | **Number** | Amount of deposit made to this bill. | [optional] 
**discountPercentage** | **Number** | Discount percentage applied to this transaction. | [optional] 
**downstreamId** | **String** | The third-party API ID of original entity | [optional] [readonly] 
**dueDate** | **Date** | The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**language** | **String** | language code according to ISO 639-1. For the United States - EN | [optional] 
**ledgerAccount** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**lineItems** | [**[BillLineItem]**](BillLineItem.md) |  | [optional] 
**notes** | **String** |  | [optional] 
**paidDate** | **Date** | The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD. | [optional] 
**paymentMethod** | **String** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check | [optional] 
**poNumber** | **String** | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order. | [optional] 
**reference** | **String** | Optional bill reference. | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**status** | **String** | Invoice status | [optional] 
**subTotal** | **Number** | Sub-total amount, normally before tax. | [optional] 
**supplier** | [**LinkedSupplier**](LinkedSupplier.md) |  | [optional] 
**taxCode** | **String** | Applicable tax id/code override if tax is not supplied on a line item basis. | [optional] 
**taxInclusive** | **Boolean** | Amounts are including tax | [optional] 
**terms** | **String** | Terms of payment. | [optional] 
**total** | **Number** | Total amount of bill, including tax. | [optional] 
**totalTax** | **Number** | Total tax amount applied to this bill. | [optional] 
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





# AccountingApi.CreditNote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**allocations** | [**[CreditNoteAllocationsInner]**](CreditNoteAllocationsInner.md) |  | [optional] 
**balance** | **Number** | The balance reflecting any payments made against the transaction. | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**currencyRate** | **Number** | Currency Exchange Rate at the time entity was recorded/generated. | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  | [optional] 
**dateIssued** | **Date** | Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD | [optional] 
**datePaid** | **Date** | Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD | [optional] 
**id** | **String** | Unique identifier representing the entity | [readonly] 
**lineItems** | [**[InvoiceLineItem]**](InvoiceLineItem.md) |  | [optional] 
**note** | **String** | Optional note to be associated with the credit note. | [optional] 
**number** | **String** | Credit note number. | [optional] 
**reference** | **String** | Optional reference message ie: Debit remittance detail. | [optional] 
**remainingCredit** | **Number** | Indicates the total credit amount still available to apply towards the payment. | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**status** | **String** | Status of credit notes | [optional] 
**subTotal** | **Number** | Sub-total amount, normally before tax. | [optional] 
**taxCode** | **String** | Applicable tax id/code override if tax is not supplied on a line item basis. | [optional] 
**taxInclusive** | **Boolean** | Amounts are including tax | [optional] 
**terms** | **String** | Optional terms to be associated with the credit note. | [optional] 
**totalAmount** | **Number** | Amount of transaction | 
**totalTax** | **Number** | Total tax amount applied to this invoice. | [optional] 
**type** | **String** | Type of payment | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: StatusEnum


* `draft` (value: `"draft"`)

* `authorised` (value: `"authorised"`)

* `paid` (value: `"paid"`)

* `voided` (value: `"voided"`)

* `deleted` (value: `"deleted"`)





## Enum: TypeEnum


* `receivable_credit` (value: `"accounts_receivable_credit"`)

* `payable_credit` (value: `"accounts_payable_credit"`)





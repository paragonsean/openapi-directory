

# CreditNote


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  |  [optional] |
|**allocations** | [**List&lt;CreditNoteAllocationsInner&gt;**](CreditNoteAllocationsInner.md) |  |  [optional] |
|**balance** | **BigDecimal** | The balance reflecting any payments made against the transaction. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**currencyRate** | **BigDecimal** | Currency Exchange Rate at the time entity was recorded/generated. |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**customer** | [**LinkedCustomer**](LinkedCustomer.md) |  |  [optional] |
|**dateIssued** | **OffsetDateTime** | Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD |  [optional] |
|**datePaid** | **OffsetDateTime** | Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD |  [optional] |
|**id** | **String** | Unique identifier representing the entity |  [readonly] |
|**lineItems** | [**List&lt;InvoiceLineItem&gt;**](InvoiceLineItem.md) |  |  [optional] |
|**note** | **String** | Optional note to be associated with the credit note. |  [optional] |
|**number** | **String** | Credit note number. |  [optional] |
|**reference** | **String** | Optional reference message ie: Debit remittance detail. |  [optional] |
|**remainingCredit** | **BigDecimal** | Indicates the total credit amount still available to apply towards the payment. |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of credit notes |  [optional] |
|**subTotal** | **BigDecimal** | Sub-total amount, normally before tax. |  [optional] |
|**taxCode** | **String** | Applicable tax id/code override if tax is not supplied on a line item basis. |  [optional] |
|**taxInclusive** | **Boolean** | Amounts are including tax |  [optional] |
|**terms** | **String** | Optional terms to be associated with the credit note. |  [optional] |
|**totalAmount** | **BigDecimal** | Amount of transaction |  |
|**totalTax** | **BigDecimal** | Total tax amount applied to this invoice. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of payment |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| AUTHORISED | &quot;authorised&quot; |
| PAID | &quot;paid&quot; |
| VOIDED | &quot;voided&quot; |
| DELETED | &quot;deleted&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RECEIVABLE_CREDIT | &quot;accounts_receivable_credit&quot; |
| PAYABLE_CREDIT | &quot;accounts_payable_credit&quot; |




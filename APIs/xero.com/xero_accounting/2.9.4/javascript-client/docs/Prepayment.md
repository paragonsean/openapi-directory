# XeroAccountingApi.Prepayment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocations** | [**[Allocation]**](Allocation.md) | See Allocations | [optional] 
**appliedAmount** | **Number** | The amount of applied to an invoice | [optional] 
**attachments** | [**[Attachment]**](Attachment.md) | See Attachments | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**currencyCode** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currencyRate** | **Number** | The currency rate for a multicurrency prepayment. If no rate is specified, the XE.com day rate is used | [optional] 
**date** | **String** | The date the prepayment is created YYYY-MM-DD | [optional] 
**hasAttachments** | **Boolean** | boolean to indicate if a prepayment has an attachment | [optional] [readonly] [default to false]
**lineAmountTypes** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | See Prepayment Line Items | [optional] 
**prepaymentID** | **String** | Xero generated unique identifier | [optional] 
**reference** | **String** | Returns Invoice number field. Reference field isn&#39;t available. | [optional] [readonly] 
**remainingCredit** | **Number** | The remaining credit balance on the prepayment | [optional] 
**status** | **String** | See Prepayment Status Codes | [optional] 
**subTotal** | **Number** | The subtotal of the prepayment excluding taxes | [optional] 
**total** | **Number** | The total of the prepayment(subtotal + total tax) | [optional] 
**totalTax** | **Number** | The total tax on the prepayment | [optional] 
**type** | **String** | See Prepayment Types | [optional] 
**updatedDateUTC** | **String** | UTC timestamp of last update to the prepayment | [optional] [readonly] 



## Enum: StatusEnum


* `AUTHORISED` (value: `"AUTHORISED"`)

* `PAID` (value: `"PAID"`)

* `VOIDED` (value: `"VOIDED"`)





## Enum: TypeEnum


* `RECEIVE-PREPAYMENT` (value: `"RECEIVE-PREPAYMENT"`)

* `SPEND-PREPAYMENT` (value: `"SPEND-PREPAYMENT"`)

* `ARPREPAYMENT` (value: `"ARPREPAYMENT"`)

* `APPREPAYMENT` (value: `"APPREPAYMENT"`)





# XeroAccountingApi.Overpayment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocations** | [**[Allocation]**](Allocation.md) | See Allocations | [optional] 
**appliedAmount** | **Number** | The amount of applied to an invoice | [optional] 
**attachments** | [**[Attachment]**](Attachment.md) | See Attachments | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**currencyCode** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currencyRate** | **Number** | The currency rate for a multicurrency overpayment. If no rate is specified, the XE.com day rate is used | [optional] 
**date** | **String** | The date the overpayment is created YYYY-MM-DD | [optional] 
**hasAttachments** | **Boolean** | boolean to indicate if a overpayment has an attachment | [optional] [readonly] [default to false]
**lineAmountTypes** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | See Overpayment Line Items | [optional] 
**overpaymentID** | **String** | Xero generated unique identifier | [optional] 
**payments** | [**[Payment]**](Payment.md) | See Payments | [optional] 
**remainingCredit** | **Number** | The remaining credit balance on the overpayment | [optional] 
**status** | **String** | See Overpayment Status Codes | [optional] 
**subTotal** | **Number** | The subtotal of the overpayment excluding taxes | [optional] 
**total** | **Number** | The total of the overpayment (subtotal + total tax) | [optional] 
**totalTax** | **Number** | The total tax on the overpayment | [optional] 
**type** | **String** | See Overpayment Types | [optional] 
**updatedDateUTC** | **String** | UTC timestamp of last update to the overpayment | [optional] [readonly] 



## Enum: StatusEnum


* `AUTHORISED` (value: `"AUTHORISED"`)

* `PAID` (value: `"PAID"`)

* `VOIDED` (value: `"VOIDED"`)





## Enum: TypeEnum


* `RECEIVE-OVERPAYMENT` (value: `"RECEIVE-OVERPAYMENT"`)

* `SPEND-OVERPAYMENT` (value: `"SPEND-OVERPAYMENT"`)

* `AROVERPAYMENT` (value: `"AROVERPAYMENT"`)





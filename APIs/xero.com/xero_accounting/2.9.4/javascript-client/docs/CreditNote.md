# XeroAccountingApi.CreditNote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocations** | [**[Allocation]**](Allocation.md) | See Allocations | [optional] 
**appliedAmount** | **Number** | The amount of applied to an invoice | [optional] 
**brandingThemeID** | **String** | See BrandingThemes | [optional] 
**cISDeduction** | **Number** | CIS deduction for UK contractors | [optional] [readonly] 
**cISRate** | **Number** | CIS Deduction rate for the organisation | [optional] [readonly] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**creditNoteID** | **String** | Xero generated unique identifier | [optional] 
**creditNoteNumber** | **String** | ACCRECCREDIT – Unique alpha numeric code identifying credit note (when missing will auto-generate from your Organisation Invoice Settings) | [optional] 
**currencyCode** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currencyRate** | **Number** | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used | [optional] 
**date** | **String** | The date the credit note is issued YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation | [optional] 
**dueDate** | **String** | Date invoice is due – YYYY-MM-DD | [optional] 
**fullyPaidOnDate** | **String** | Date when credit note was fully paid(UTC format) | [optional] 
**hasAttachments** | **Boolean** | boolean to indicate if a credit note has an attachment | [optional] [default to false]
**hasErrors** | **Boolean** | A boolean to indicate if a credit note has an validation errors | [optional] [default to false]
**lineAmountTypes** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | See Invoice Line Items | [optional] 
**payments** | [**[Payment]**](Payment.md) | See Payments | [optional] 
**reference** | **String** | ACCRECCREDIT only – additional reference number | [optional] 
**remainingCredit** | **Number** | The remaining credit balance on the Credit Note | [optional] 
**sentToContact** | **Boolean** | boolean to indicate if a credit note has been sent to a contact via  the Xero app (currently read only) | [optional] [readonly] 
**status** | **String** | See Credit Note Status Codes | [optional] 
**statusAttributeString** | **String** | A string to indicate if a invoice status | [optional] 
**subTotal** | **Number** | The subtotal of the credit note excluding taxes | [optional] 
**total** | **Number** | The total of the Credit Note(subtotal + total tax) | [optional] 
**totalTax** | **Number** | The total tax on the credit note | [optional] 
**type** | **String** | See Credit Note Types | [optional] 
**updatedDateUTC** | **String** | UTC timestamp of last update to the credit note | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 



## Enum: StatusEnum


* `DRAFT` (value: `"DRAFT"`)

* `SUBMITTED` (value: `"SUBMITTED"`)

* `DELETED` (value: `"DELETED"`)

* `AUTHORISED` (value: `"AUTHORISED"`)

* `PAID` (value: `"PAID"`)

* `VOIDED` (value: `"VOIDED"`)





## Enum: TypeEnum


* `ACCPAYCREDIT` (value: `"ACCPAYCREDIT"`)

* `ACCRECCREDIT` (value: `"ACCRECCREDIT"`)





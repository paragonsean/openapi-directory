

# CreditNote


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocations** | [**List&lt;Allocation&gt;**](Allocation.md) | See Allocations |  [optional] |
|**appliedAmount** | **Double** | The amount of applied to an invoice |  [optional] |
|**brandingThemeID** | **UUID** | See BrandingThemes |  [optional] |
|**ciSDeduction** | **Double** | CIS deduction for UK contractors |  [optional] [readonly] |
|**ciSRate** | **Double** | CIS Deduction rate for the organisation |  [optional] [readonly] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**creditNoteID** | **UUID** | Xero generated unique identifier |  [optional] |
|**creditNoteNumber** | **String** | ACCRECCREDIT – Unique alpha numeric code identifying credit note (when missing will auto-generate from your Organisation Invoice Settings) |  [optional] |
|**currencyCode** | **CurrencyCode** |  |  [optional] |
|**currencyRate** | **Double** | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used |  [optional] |
|**date** | **String** | The date the credit note is issued YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation |  [optional] |
|**dueDate** | **String** | Date invoice is due – YYYY-MM-DD |  [optional] |
|**fullyPaidOnDate** | **String** | Date when credit note was fully paid(UTC format) |  [optional] |
|**hasAttachments** | **Boolean** | boolean to indicate if a credit note has an attachment |  [optional] |
|**hasErrors** | **Boolean** | A boolean to indicate if a credit note has an validation errors |  [optional] |
|**lineAmountTypes** | **LineAmountTypes** |  |  [optional] |
|**lineItems** | [**List&lt;LineItem&gt;**](LineItem.md) | See Invoice Line Items |  [optional] |
|**payments** | [**List&lt;Payment&gt;**](Payment.md) | See Payments |  [optional] |
|**reference** | **String** | ACCRECCREDIT only – additional reference number |  [optional] |
|**remainingCredit** | **Double** | The remaining credit balance on the Credit Note |  [optional] |
|**sentToContact** | **Boolean** | boolean to indicate if a credit note has been sent to a contact via  the Xero app (currently read only) |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | See Credit Note Status Codes |  [optional] |
|**statusAttributeString** | **String** | A string to indicate if a invoice status |  [optional] |
|**subTotal** | **Double** | The subtotal of the credit note excluding taxes |  [optional] |
|**total** | **Double** | The total of the Credit Note(subtotal + total tax) |  [optional] |
|**totalTax** | **Double** | The total tax on the credit note |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | See Credit Note Types |  [optional] |
|**updatedDateUTC** | **String** | UTC timestamp of last update to the credit note |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |
|**warnings** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of warning messages from the API |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;DRAFT&quot; |
| SUBMITTED | &quot;SUBMITTED&quot; |
| DELETED | &quot;DELETED&quot; |
| AUTHORISED | &quot;AUTHORISED&quot; |
| PAID | &quot;PAID&quot; |
| VOIDED | &quot;VOIDED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCPAYCREDIT | &quot;ACCPAYCREDIT&quot; |
| ACCRECCREDIT | &quot;ACCRECCREDIT&quot; |




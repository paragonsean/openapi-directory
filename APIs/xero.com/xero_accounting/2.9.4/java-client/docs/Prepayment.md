

# Prepayment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocations** | [**List&lt;Allocation&gt;**](Allocation.md) | See Allocations |  [optional] |
|**appliedAmount** | **Double** | The amount of applied to an invoice |  [optional] |
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | See Attachments |  [optional] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**currencyCode** | **CurrencyCode** |  |  [optional] |
|**currencyRate** | **Double** | The currency rate for a multicurrency prepayment. If no rate is specified, the XE.com day rate is used |  [optional] |
|**date** | **String** | The date the prepayment is created YYYY-MM-DD |  [optional] |
|**hasAttachments** | **Boolean** | boolean to indicate if a prepayment has an attachment |  [optional] [readonly] |
|**lineAmountTypes** | **LineAmountTypes** |  |  [optional] |
|**lineItems** | [**List&lt;LineItem&gt;**](LineItem.md) | See Prepayment Line Items |  [optional] |
|**prepaymentID** | **UUID** | Xero generated unique identifier |  [optional] |
|**reference** | **String** | Returns Invoice number field. Reference field isn&#39;t available. |  [optional] [readonly] |
|**remainingCredit** | **Double** | The remaining credit balance on the prepayment |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | See Prepayment Status Codes |  [optional] |
|**subTotal** | **Double** | The subtotal of the prepayment excluding taxes |  [optional] |
|**total** | **Double** | The total of the prepayment(subtotal + total tax) |  [optional] |
|**totalTax** | **Double** | The total tax on the prepayment |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | See Prepayment Types |  [optional] |
|**updatedDateUTC** | **String** | UTC timestamp of last update to the prepayment |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AUTHORISED | &quot;AUTHORISED&quot; |
| PAID | &quot;PAID&quot; |
| VOIDED | &quot;VOIDED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RECEIVE_PREPAYMENT | &quot;RECEIVE-PREPAYMENT&quot; |
| SPEND_PREPAYMENT | &quot;SPEND-PREPAYMENT&quot; |
| ARPREPAYMENT | &quot;ARPREPAYMENT&quot; |
| APPREPAYMENT | &quot;APPREPAYMENT&quot; |




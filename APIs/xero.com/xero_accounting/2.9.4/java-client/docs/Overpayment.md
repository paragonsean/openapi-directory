

# Overpayment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocations** | [**List&lt;Allocation&gt;**](Allocation.md) | See Allocations |  [optional] |
|**appliedAmount** | **Double** | The amount of applied to an invoice |  [optional] |
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | See Attachments |  [optional] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**currencyCode** | **CurrencyCode** |  |  [optional] |
|**currencyRate** | **Double** | The currency rate for a multicurrency overpayment. If no rate is specified, the XE.com day rate is used |  [optional] |
|**date** | **String** | The date the overpayment is created YYYY-MM-DD |  [optional] |
|**hasAttachments** | **Boolean** | boolean to indicate if a overpayment has an attachment |  [optional] [readonly] |
|**lineAmountTypes** | **LineAmountTypes** |  |  [optional] |
|**lineItems** | [**List&lt;LineItem&gt;**](LineItem.md) | See Overpayment Line Items |  [optional] |
|**overpaymentID** | **UUID** | Xero generated unique identifier |  [optional] |
|**payments** | [**List&lt;Payment&gt;**](Payment.md) | See Payments |  [optional] |
|**remainingCredit** | **Double** | The remaining credit balance on the overpayment |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | See Overpayment Status Codes |  [optional] |
|**subTotal** | **Double** | The subtotal of the overpayment excluding taxes |  [optional] |
|**total** | **Double** | The total of the overpayment (subtotal + total tax) |  [optional] |
|**totalTax** | **Double** | The total tax on the overpayment |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | See Overpayment Types |  [optional] |
|**updatedDateUTC** | **String** | UTC timestamp of last update to the overpayment |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AUTHORISED | &quot;AUTHORISED&quot; |
| PAID | &quot;PAID&quot; |
| VOIDED | &quot;VOIDED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RECEIVE_OVERPAYMENT | &quot;RECEIVE-OVERPAYMENT&quot; |
| SPEND_OVERPAYMENT | &quot;SPEND-OVERPAYMENT&quot; |
| AROVERPAYMENT | &quot;AROVERPAYMENT&quot; |




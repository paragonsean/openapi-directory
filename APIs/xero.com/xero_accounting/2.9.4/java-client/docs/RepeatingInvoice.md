

# RepeatingInvoice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Displays array of attachments from the API |  [optional] |
|**brandingThemeID** | **UUID** | See BrandingThemes |  [optional] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**currencyCode** | **CurrencyCode** |  |  [optional] |
|**hasAttachments** | **Boolean** | boolean to indicate if an invoice has an attachment |  [optional] [readonly] |
|**ID** | **UUID** | Xero generated unique identifier for repeating invoice template |  [optional] |
|**lineAmountTypes** | **LineAmountTypes** |  |  [optional] |
|**lineItems** | [**List&lt;LineItem&gt;**](LineItem.md) | See LineItems |  [optional] |
|**reference** | **String** | ACCREC only – additional reference number |  [optional] |
|**repeatingInvoiceID** | **UUID** | Xero generated unique identifier for repeating invoice template |  [optional] |
|**schedule** | [**Schedule**](Schedule.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | One of the following - DRAFT or AUTHORISED – See Invoice Status Codes |  [optional] |
|**subTotal** | **Double** | Total of invoice excluding taxes |  [optional] |
|**total** | **Double** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax) |  [optional] |
|**totalTax** | **Double** | Total tax on invoice |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | See Invoice Types |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;DRAFT&quot; |
| AUTHORISED | &quot;AUTHORISED&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCPAY | &quot;ACCPAY&quot; |
| ACCREC | &quot;ACCREC&quot; |




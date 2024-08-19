

# Receipt


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Displays array of attachments from the API |  [optional] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**date** | **String** | Date of receipt – YYYY-MM-DD |  [optional] |
|**hasAttachments** | **Boolean** | boolean to indicate if a receipt has an attachment |  [optional] [readonly] |
|**lineAmountTypes** | **LineAmountTypes** |  |  [optional] |
|**lineItems** | [**List&lt;LineItem&gt;**](LineItem.md) |  |  [optional] |
|**receiptID** | **UUID** | Xero generated unique identifier for receipt |  [optional] |
|**receiptNumber** | **String** | Xero generated sequence number for receipt in current claim for a given user |  [optional] [readonly] |
|**reference** | **String** | Additional reference number |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of receipt – see status types |  [optional] |
|**subTotal** | **Double** | Total of receipt excluding taxes |  [optional] |
|**total** | **Double** | Total of receipt tax inclusive (i.e. SubTotal + TotalTax) |  [optional] |
|**totalTax** | **Double** | Total tax on receipt |  [optional] |
|**updatedDateUTC** | **String** | Last modified date UTC format |  [optional] [readonly] |
|**url** | **String** | URL link to a source document – shown as “Go to [appName]” in the Xero app |  [optional] [readonly] |
|**user** | [**User**](User.md) |  |  [optional] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |
|**warnings** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of warning messages from the API |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;DRAFT&quot; |
| SUBMITTED | &quot;SUBMITTED&quot; |
| AUTHORISED | &quot;AUTHORISED&quot; |
| DECLINED | &quot;DECLINED&quot; |
| VOIDED | &quot;VOIDED&quot; |




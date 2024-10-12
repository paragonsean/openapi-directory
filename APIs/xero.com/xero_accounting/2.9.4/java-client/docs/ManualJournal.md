

# ManualJournal


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Displays array of attachments from the API |  [optional] |
|**date** | **String** | Date journal was posted – YYYY-MM-DD |  [optional] |
|**hasAttachments** | **Boolean** | Boolean to indicate if a manual journal has an attachment |  [optional] [readonly] |
|**journalLines** | [**List&lt;ManualJournalLine&gt;**](ManualJournalLine.md) | See JournalLines |  [optional] |
|**lineAmountTypes** | **LineAmountTypes** |  |  [optional] |
|**manualJournalID** | **UUID** | The Xero identifier for a Manual Journal |  [optional] |
|**narration** | **String** | Description of journal being posted |  |
|**showOnCashBasisReports** | **Boolean** | Boolean – default is true if not specified |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | See Manual Journal Status Codes |  [optional] |
|**statusAttributeString** | **String** | A string to indicate if a invoice status |  [optional] |
|**updatedDateUTC** | **String** | Last modified date UTC format |  [optional] [readonly] |
|**url** | **String** | Url link to a source document – shown as “Go to [appName]” in the Xero app |  [optional] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |
|**warnings** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of warning messages from the API |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;DRAFT&quot; |
| POSTED | &quot;POSTED&quot; |
| DELETED | &quot;DELETED&quot; |
| VOIDED | &quot;VOIDED&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |




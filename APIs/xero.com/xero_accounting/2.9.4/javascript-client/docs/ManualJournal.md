# XeroAccountingApi.ManualJournal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**date** | **String** | Date journal was posted – YYYY-MM-DD | [optional] 
**hasAttachments** | **Boolean** | Boolean to indicate if a manual journal has an attachment | [optional] [readonly] [default to false]
**journalLines** | [**[ManualJournalLine]**](ManualJournalLine.md) | See JournalLines | [optional] 
**lineAmountTypes** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**manualJournalID** | **String** | The Xero identifier for a Manual Journal | [optional] 
**narration** | **String** | Description of journal being posted | 
**showOnCashBasisReports** | **Boolean** | Boolean – default is true if not specified | [optional] 
**status** | **String** | See Manual Journal Status Codes | [optional] 
**statusAttributeString** | **String** | A string to indicate if a invoice status | [optional] 
**updatedDateUTC** | **String** | Last modified date UTC format | [optional] [readonly] 
**url** | **String** | Url link to a source document – shown as “Go to [appName]” in the Xero app | [optional] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 



## Enum: StatusEnum


* `DRAFT` (value: `"DRAFT"`)

* `POSTED` (value: `"POSTED"`)

* `DELETED` (value: `"DELETED"`)

* `VOIDED` (value: `"VOIDED"`)

* `ARCHIVED` (value: `"ARCHIVED"`)





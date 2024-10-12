# XeroAccountingApi.Receipt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**date** | **String** | Date of receipt – YYYY-MM-DD | [optional] 
**hasAttachments** | **Boolean** | boolean to indicate if a receipt has an attachment | [optional] [readonly] [default to false]
**lineAmountTypes** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) |  | [optional] 
**receiptID** | **String** | Xero generated unique identifier for receipt | [optional] 
**receiptNumber** | **String** | Xero generated sequence number for receipt in current claim for a given user | [optional] [readonly] 
**reference** | **String** | Additional reference number | [optional] 
**status** | **String** | Current status of receipt – see status types | [optional] 
**subTotal** | **Number** | Total of receipt excluding taxes | [optional] 
**total** | **Number** | Total of receipt tax inclusive (i.e. SubTotal + TotalTax) | [optional] 
**totalTax** | **Number** | Total tax on receipt | [optional] 
**updatedDateUTC** | **String** | Last modified date UTC format | [optional] [readonly] 
**url** | **String** | URL link to a source document – shown as “Go to [appName]” in the Xero app | [optional] [readonly] 
**user** | [**User**](User.md) |  | [optional] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 



## Enum: StatusEnum


* `DRAFT` (value: `"DRAFT"`)

* `SUBMITTED` (value: `"SUBMITTED"`)

* `AUTHORISED` (value: `"AUTHORISED"`)

* `DECLINED` (value: `"DECLINED"`)

* `VOIDED` (value: `"VOIDED"`)





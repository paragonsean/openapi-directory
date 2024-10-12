# XeroAccountingApi.LinkedTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactID** | **String** | Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID&#x3D;4bb34b03-3378-4bb2-a0ed-6345abf3224e&amp;Status&#x3D;APPROVED. | [optional] 
**linkedTransactionID** | **String** | The Xero identifier for an Linked Transaction e.g./LinkedTransactions/297c2dc5-cc47-4afd-8ec8-74990b8761e9 | [optional] 
**sourceLineItemID** | **String** | The line item identifier from the source transaction. | [optional] 
**sourceTransactionID** | **String** | Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice | [optional] 
**sourceTransactionTypeCode** | **String** | The Type of the source tranasction. This will be ACCPAY if the linked transaction was created from an invoice and SPEND if it was created from a bank transaction. | [optional] 
**status** | **String** | Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID&#x3D;4bb34b03-3378-4bb2-a0ed-6345abf3224e&amp;Status&#x3D;APPROVED. | [optional] 
**targetLineItemID** | **String** | The line item identifier from the target transaction. It is possible  to link multiple billable expenses to the same TargetLineItemID. | [optional] 
**targetTransactionID** | **String** | Filter by the TargetTransactionID. Get all the linked transactions  allocated to a particular ACCREC invoice | [optional] 
**type** | **String** | This will always be BILLABLEEXPENSE. More types may be added in future. | [optional] 
**updatedDateUTC** | **String** | The last modified date in UTC format | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 



## Enum: SourceTransactionTypeCodeEnum


* `ACCPAY` (value: `"ACCPAY"`)

* `SPEND` (value: `"SPEND"`)





## Enum: StatusEnum


* `APPROVED` (value: `"APPROVED"`)

* `DRAFT` (value: `"DRAFT"`)

* `ONDRAFT` (value: `"ONDRAFT"`)

* `BILLED` (value: `"BILLED"`)

* `VOIDED` (value: `"VOIDED"`)





## Enum: TypeEnum


* `BILLABLEEXPENSE` (value: `"BILLABLEEXPENSE"`)





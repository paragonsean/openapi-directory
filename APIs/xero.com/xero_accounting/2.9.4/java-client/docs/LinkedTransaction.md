

# LinkedTransaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contactID** | **UUID** | Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID&#x3D;4bb34b03-3378-4bb2-a0ed-6345abf3224e&amp;Status&#x3D;APPROVED. |  [optional] |
|**linkedTransactionID** | **UUID** | The Xero identifier for an Linked Transaction e.g./LinkedTransactions/297c2dc5-cc47-4afd-8ec8-74990b8761e9 |  [optional] |
|**sourceLineItemID** | **UUID** | The line item identifier from the source transaction. |  [optional] |
|**sourceTransactionID** | **UUID** | Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice |  [optional] |
|**sourceTransactionTypeCode** | [**SourceTransactionTypeCodeEnum**](#SourceTransactionTypeCodeEnum) | The Type of the source tranasction. This will be ACCPAY if the linked transaction was created from an invoice and SPEND if it was created from a bank transaction. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID&#x3D;4bb34b03-3378-4bb2-a0ed-6345abf3224e&amp;Status&#x3D;APPROVED. |  [optional] |
|**targetLineItemID** | **UUID** | The line item identifier from the target transaction. It is possible  to link multiple billable expenses to the same TargetLineItemID. |  [optional] |
|**targetTransactionID** | **UUID** | Filter by the TargetTransactionID. Get all the linked transactions  allocated to a particular ACCREC invoice |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | This will always be BILLABLEEXPENSE. More types may be added in future. |  [optional] |
|**updatedDateUTC** | **String** | The last modified date in UTC format |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



## Enum: SourceTransactionTypeCodeEnum

| Name | Value |
|---- | -----|
| ACCPAY | &quot;ACCPAY&quot; |
| SPEND | &quot;SPEND&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;APPROVED&quot; |
| DRAFT | &quot;DRAFT&quot; |
| ONDRAFT | &quot;ONDRAFT&quot; |
| BILLED | &quot;BILLED&quot; |
| VOIDED | &quot;VOIDED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BILLABLEEXPENSE | &quot;BILLABLEEXPENSE&quot; |




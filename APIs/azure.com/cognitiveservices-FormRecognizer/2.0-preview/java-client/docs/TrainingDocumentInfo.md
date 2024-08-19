

# TrainingDocumentInfo

Report for a custom model training document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentName** | **String** | Training document name. |  |
|**errors** | [**List&lt;ErrorInformation&gt;**](ErrorInformation.md) | List of errors. |  |
|**pages** | **Integer** | Total number of pages trained. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the training operation. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;succeeded&quot; |
| PARTIALLY_SUCCEEDED | &quot;partiallySucceeded&quot; |
| FAILED | &quot;failed&quot; |




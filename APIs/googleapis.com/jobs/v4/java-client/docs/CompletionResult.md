

# CompletionResult

Resource that represents completion results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageUri** | **String** | The URI of the company image for COMPANY_NAME. |  [optional] |
|**suggestion** | **String** | The suggestion for the query. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The completion topic. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMPLETION_TYPE_UNSPECIFIED | &quot;COMPLETION_TYPE_UNSPECIFIED&quot; |
| JOB_TITLE | &quot;JOB_TITLE&quot; |
| COMPANY_NAME | &quot;COMPANY_NAME&quot; |
| COMBINED | &quot;COMBINED&quot; |




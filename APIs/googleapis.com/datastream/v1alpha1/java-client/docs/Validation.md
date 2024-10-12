

# Validation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | A custom code identifying this validation. |  [optional] |
|**description** | **String** | A short description of the validation. |  [optional] |
|**message** | [**List&lt;ValidationMessage&gt;**](ValidationMessage.md) | Messages reflecting the validation results. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Validation execution status. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| NOT_EXECUTED | &quot;NOT_EXECUTED&quot; |
| FAILED | &quot;FAILED&quot; |
| PASSED | &quot;PASSED&quot; |




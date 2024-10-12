

# Validation

A validation to perform on a stream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | A custom code identifying this validation. |  [optional] |
|**description** | **String** | A short description of the validation. |  [optional] |
|**message** | [**List&lt;ValidationMessage&gt;**](ValidationMessage.md) | Messages reflecting the validation results. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Validation execution status. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| NOT_EXECUTED | &quot;NOT_EXECUTED&quot; |
| FAILED | &quot;FAILED&quot; |
| PASSED | &quot;PASSED&quot; |
| WARNING | &quot;WARNING&quot; |




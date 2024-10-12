

# ValidationCheckResult

ValidationCheckResult defines the details about the validation check.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | The category of the validation. |  [optional] |
|**description** | **String** | The description of the validation check. |  [optional] |
|**details** | **String** | Detailed failure information, which might be unformatted. |  [optional] |
|**reason** | **String** | A human-readable message of the check failure. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The validation check state. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;STATE_UNKNOWN&quot; |
| FAILURE | &quot;STATE_FAILURE&quot; |
| SKIPPED | &quot;STATE_SKIPPED&quot; |
| FATAL | &quot;STATE_FATAL&quot; |
| WARNING | &quot;STATE_WARNING&quot; |






# StateReason

The reason a spoke is inactive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | The code associated with this reason. |  [optional] |
|**message** | **String** | Human-readable details about this reason. |  [optional] |
|**userDetails** | **String** | Additional information provided by the user in the RejectSpoke call. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |
| REJECTED | &quot;REJECTED&quot; |
| PAUSED | &quot;PAUSED&quot; |
| FAILED | &quot;FAILED&quot; |




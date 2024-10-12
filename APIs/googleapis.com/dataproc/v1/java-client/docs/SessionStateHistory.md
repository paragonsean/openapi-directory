

# SessionStateHistory

Historical state information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the session at this point in the session history. |  [optional] [readonly] |
|**stateMessage** | **String** | Output only. Details about the state at this point in the session history. |  [optional] [readonly] |
|**stateStartTime** | **String** | Output only. The time when the session entered the historical state. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| TERMINATING | &quot;TERMINATING&quot; |
| TERMINATED | &quot;TERMINATED&quot; |
| FAILED | &quot;FAILED&quot; |






# StatusEvent

Status event

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the event. |  [optional] |
|**eventTime** | **String** | The time this event occurred. |  [optional] |
|**taskExecution** | [**TaskExecution**](TaskExecution.md) |  |  [optional] |
|**taskState** | [**TaskStateEnum**](#TaskStateEnum) | Task State |  [optional] |
|**type** | **String** | Type of the event. |  [optional] |



## Enum: TaskStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| ASSIGNED | &quot;ASSIGNED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FAILED | &quot;FAILED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| UNEXECUTED | &quot;UNEXECUTED&quot; |




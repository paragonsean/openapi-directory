

# SubtaskInformation

Information about an Azure Batch subtask.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | Gets or sets the time at which the subtask completed. This property is set only if the subtask is in the Completed state. |  [optional] |
|**exitCode** | **Integer** | Gets or sets the exit code of the subtask. This property is set only if the subtask is in the Completed state. |  [optional] |
|**id** | **Integer** | Gets or sets the id of the subtask. |  [optional] |
|**nodeInfo** | [**ComputeNodeInformation**](ComputeNodeInformation.md) |  |  [optional] |
|**previousState** | [**PreviousStateEnum**](#PreviousStateEnum) | Gets or sets the previous state of the subtask. This property is not set if the subtask is in its initial Active state. |  [optional] |
|**previousStateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the subtask entered its previous state. This property is not set if the subtask is in its initial Active state. |  [optional] |
|**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Gets or sets the time at which the subtask started running. If the subtask has been restarted or retried, this is the most recent time at which the subtask started running. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets the current state of the subtask. |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the subtask entered its current state. |  [optional] |



## Enum: PreviousStateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PREPARING | &quot;preparing&quot; |
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PREPARING | &quot;preparing&quot; |
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |




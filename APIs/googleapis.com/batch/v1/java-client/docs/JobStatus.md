

# JobStatus

Job status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**runDuration** | **String** | The duration of time that the Job spent in status RUNNING. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Job state |  [optional] |
|**statusEvents** | [**List&lt;StatusEvent&gt;**](StatusEvent.md) | Job status events |  [optional] |
|**taskGroups** | [**Map&lt;String, TaskGroupStatus&gt;**](TaskGroupStatus.md) | Aggregated task status for each TaskGroup in the Job. The map key is TaskGroup ID. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| QUEUED | &quot;QUEUED&quot; |
| SCHEDULED | &quot;SCHEDULED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETION_IN_PROGRESS | &quot;DELETION_IN_PROGRESS&quot; |




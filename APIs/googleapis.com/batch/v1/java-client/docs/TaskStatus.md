

# TaskStatus

Status of a task

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | Task state |  [optional] |
|**statusEvents** | [**List&lt;StatusEvent&gt;**](StatusEvent.md) | Detailed info about why the state is reached. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| ASSIGNED | &quot;ASSIGNED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FAILED | &quot;FAILED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| UNEXECUTED | &quot;UNEXECUTED&quot; |




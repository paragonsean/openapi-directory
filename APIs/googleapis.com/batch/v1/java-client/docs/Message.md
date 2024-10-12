

# Message

Message details. Describe the conditions under which messages will be sent. If no attribute is defined, no message will be sent by default. One message should specify either the job or the task level attributes, but not both. For example, job level: JOB_STATE_CHANGED and/or a specified new_job_state; task level: TASK_STATE_CHANGED and/or a specified new_task_state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**newJobState** | [**NewJobStateEnum**](#NewJobStateEnum) | The new job state. |  [optional] |
|**newTaskState** | [**NewTaskStateEnum**](#NewTaskStateEnum) | The new task state. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The message type. |  [optional] |



## Enum: NewJobStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| QUEUED | &quot;QUEUED&quot; |
| SCHEDULED | &quot;SCHEDULED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETION_IN_PROGRESS | &quot;DELETION_IN_PROGRESS&quot; |



## Enum: NewTaskStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| ASSIGNED | &quot;ASSIGNED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FAILED | &quot;FAILED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| UNEXECUTED | &quot;UNEXECUTED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| JOB_STATE_CHANGED | &quot;JOB_STATE_CHANGED&quot; |
| TASK_STATE_CHANGED | &quot;TASK_STATE_CHANGED&quot; |




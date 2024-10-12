

# NodeDisableSchedulingParameter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeDisableSchedulingOption** | [**NodeDisableSchedulingOptionEnum**](#NodeDisableSchedulingOptionEnum) | Values are:   requeue - Terminate running task processes and requeue the tasks. The tasks may run again on other compute nodes, or when task scheduling is re-enabled on this node. Enter offline state as soon as tasks have been terminated.  terminate - Terminate running tasks. The tasks will not run again. Enter offline state as soon as tasks have been terminated.  taskcompletion - Allow currently running tasks to complete. Schedule no new tasks while waiting. Enter offline state when all tasks have completed.   The default value is requeue. |  [optional] |



## Enum: NodeDisableSchedulingOptionEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| TASK_COMPLETION | &quot;taskCompletion&quot; |




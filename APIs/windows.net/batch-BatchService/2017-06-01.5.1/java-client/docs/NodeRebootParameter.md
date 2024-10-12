

# NodeRebootParameter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeRebootOption** | [**NodeRebootOptionEnum**](#NodeRebootOptionEnum) | Values are:   requeue - Terminate running task processes and requeue the tasks. The tasks will run again when a node is available. Restart the node as soon as tasks have been terminated.  terminate - Terminate running tasks. The tasks will not run again. Restart the node as soon as tasks have been terminated.  taskcompletion - Allow currently running tasks to complete. Schedule no new tasks while waiting. Restart the node when all tasks have completed.  retaineddata - Allow currently running tasks to complete, then wait for all task data retention periods to expire. Schedule no new tasks while waiting. Restart the node when all task retention periods have expired.   The default value is requeue. |  [optional] |



## Enum: NodeRebootOptionEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| TASK_COMPLETION | &quot;taskCompletion&quot; |
| RETAINED_DATA | &quot;retainedData&quot; |




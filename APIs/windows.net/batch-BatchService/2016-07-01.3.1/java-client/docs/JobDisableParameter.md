

# JobDisableParameter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableTasks** | [**DisableTasksEnum**](#DisableTasksEnum) | Possible values are: requeue – Terminate running tasks and requeue them. The tasks will run again when the job is enabled. terminate – Terminate running tasks. The tasks will not run again. wait – Allow currently running tasks to complete. |  |



## Enum: DisableTasksEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| WAIT | &quot;wait&quot; |




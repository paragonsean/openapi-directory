

# JobDisableParameter

Parameters for a CloudJobOperations.Disable request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableTasks** | [**DisableTasksEnum**](#DisableTasksEnum) | What to do with active tasks associated with the job. |  |



## Enum: DisableTasksEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| WAIT | &quot;wait&quot; |




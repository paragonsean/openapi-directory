

# NodeRebootParameter

Parameters for a ComputeNodeOperations.Reboot request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeRebootOption** | [**NodeRebootOptionEnum**](#NodeRebootOptionEnum) | When to reboot the compute node and what to do with currently running tasks. The default value is requeue. |  [optional] |



## Enum: NodeRebootOptionEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| TASKCOMPLETION | &quot;taskcompletion&quot; |
| RETAINEDDATA | &quot;retaineddata&quot; |




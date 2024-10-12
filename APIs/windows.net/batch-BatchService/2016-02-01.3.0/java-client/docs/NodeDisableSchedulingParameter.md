

# NodeDisableSchedulingParameter

Parameters for a ComputeNodeOperations.DisableScheduling request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeDisableSchedulingOption** | [**NodeDisableSchedulingOptionEnum**](#NodeDisableSchedulingOptionEnum) | What to do with currently running tasks when disable task scheduling on the compute node. The default value is requeue. |  [optional] |



## Enum: NodeDisableSchedulingOptionEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| TASKCOMPLETION | &quot;taskcompletion&quot; |




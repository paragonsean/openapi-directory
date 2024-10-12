

# NodeReimageParameter

Parameters for a ComputeNodeOperations.Reimage request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeReimageOption** | [**NodeReimageOptionEnum**](#NodeReimageOptionEnum) | When to reimage the compute node and what to do with currently running tasks. The default value is requeue. |  [optional] |



## Enum: NodeReimageOptionEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| TASKCOMPLETION | &quot;taskcompletion&quot; |
| RETAINEDDATA | &quot;retaineddata&quot; |




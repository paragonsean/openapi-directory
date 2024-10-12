

# NodeRemoveParameter

Parameters for a ComputeNodeOperations.Remove request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeDeallocationOption** | [**NodeDeallocationOptionEnum**](#NodeDeallocationOptionEnum) | Sets when compute nodes may be removed from the pool. |  [optional] |
|**nodeList** | **List&lt;String&gt;** | Sets a list containing the id of the compute nodes to be removed from the specified pool. |  |
|**resizeTimeout** | **String** | Sets the timeout for removal of compute nodes to the pool. The default value is 10 minutes. |  [optional] |



## Enum: NodeDeallocationOptionEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| TASKCOMPLETION | &quot;taskcompletion&quot; |
| RETAINEDDATA | &quot;retaineddata&quot; |




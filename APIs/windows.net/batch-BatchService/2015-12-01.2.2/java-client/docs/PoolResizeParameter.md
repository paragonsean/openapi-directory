

# PoolResizeParameter

Parameters for a CloudPoolOperations.Resize request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeDeallocationOption** | [**NodeDeallocationOptionEnum**](#NodeDeallocationOptionEnum) | Sets when nodes may be removed from the pool, if the pool size is decreasing. |  [optional] |
|**resizeTimeout** | **String** | Sets the timeout for allocation of compute nodes to the pool or removal of compute nodes from the pool. The default value is 10 minutes. |  [optional] |
|**targetDedicated** | **Integer** | Sets the desired number of compute nodes in the pool. |  |



## Enum: NodeDeallocationOptionEnum

| Name | Value |
|---- | -----|
| REQUEUE | &quot;requeue&quot; |
| TERMINATE | &quot;terminate&quot; |
| TASKCOMPLETION | &quot;taskcompletion&quot; |
| RETAINEDDATA | &quot;retaineddata&quot; |




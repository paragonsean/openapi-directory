# BatchService.PoolResizeParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodeDeallocationOption** | **String** | When nodes may be removed from the pool, if the pool size is decreasing. | [optional] 
**resizeTimeout** | **String** | The timeout for allocation of compute nodes to the pool or removal of compute nodes from the pool. The default value is 10 minutes. | [optional] 
**targetDedicated** | **Number** | The desired number of compute nodes in the pool. | 



## Enum: NodeDeallocationOptionEnum


* `requeue` (value: `"requeue"`)

* `terminate` (value: `"terminate"`)

* `taskcompletion` (value: `"taskcompletion"`)

* `retaineddata` (value: `"retaineddata"`)





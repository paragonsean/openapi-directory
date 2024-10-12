# BatchService.NodeRemoveParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodeDeallocationOption** | **String** | Sets when compute nodes may be removed from the pool. | [optional] 
**nodeList** | **[String]** | Sets a list containing the id of the compute nodes to be removed from the specified pool. | 
**resizeTimeout** | **String** | Sets the timeout for removal of compute nodes to the pool. The default value is 10 minutes. | [optional] 



## Enum: NodeDeallocationOptionEnum


* `requeue` (value: `"requeue"`)

* `terminate` (value: `"terminate"`)

* `taskcompletion` (value: `"taskcompletion"`)

* `retaineddata` (value: `"retaineddata"`)





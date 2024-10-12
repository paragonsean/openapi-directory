# BatchService.NodeReimageParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodeReimageOption** | **String** | Values are:   requeue - Terminate running task processes and requeue the tasks. The tasks will run again when a node is available. Reimage the node as soon as tasks have been terminated.  terminate - Terminate running tasks. The tasks will not run again. Reimage the node as soon as tasks have been terminated.  taskcompletion - Allow currently running tasks to complete. Schedule no new tasks while waiting. Reimage the node when all tasks have completed.  retaineddata - Allow currently running tasks to complete, then wait for all task data retention periods to expire. Schedule no new tasks while waiting. Reimage the node when all task retention periods have expired.   The default value is requeue. | [optional] 



## Enum: NodeReimageOptionEnum


* `requeue` (value: `"requeue"`)

* `terminate` (value: `"terminate"`)

* `taskCompletion` (value: `"taskCompletion"`)

* `retainedData` (value: `"retainedData"`)





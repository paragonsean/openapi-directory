# BatchService.TaskConstraints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxTaskRetryCount** | **Number** | Note that this value specifically controls the number of retries for the task executable due to a nonzero exit code. The Batch service will try the task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries the task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry the task after the first attempt. If the maximum retry count is -1, the Batch service retries the task without limit. Resource files and application packages are only downloaded again if the task is retried on a new compute node. | [optional] 
**maxWallClockTime** | **String** | If this is not specified, there is no time limit on how long the task may run. | [optional] 
**retentionTime** | **String** | The default is infinite, i.e. the task directory will be retained until the compute node is removed or reimaged. | [optional] 



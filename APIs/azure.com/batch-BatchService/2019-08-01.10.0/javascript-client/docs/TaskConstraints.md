# BatchService.TaskConstraints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxTaskRetryCount** | **Number** | Note that this value specifically controls the number of retries for the Task executable due to a nonzero exit code. The Batch service will try the Task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries the Task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry the Task after the first attempt. If the maximum retry count is -1, the Batch service retries the Task without limit. | [optional] 
**maxWallClockTime** | **String** | If this is not specified, there is no time limit on how long the Task may run. | [optional] 
**retentionTime** | **String** | The default is 7 days, i.e. the Task directory will be retained for 7 days unless the Compute Node is removed or the Job is deleted. | [optional] 



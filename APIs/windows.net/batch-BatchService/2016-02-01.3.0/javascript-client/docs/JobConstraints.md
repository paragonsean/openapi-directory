# BatchService.JobConstraints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxTaskRetryCount** | **Number** | The maximum number of times each task may be retried. The Batch service retries a task if its exit code is nonzero. | [optional] 
**maxWallClockTime** | **String** | The maximum elapsed time that the job may run, measured from the time the job starts. If the job does not complete within the time limit, the Batch service terminates it and any tasks that are still running. | [optional] 



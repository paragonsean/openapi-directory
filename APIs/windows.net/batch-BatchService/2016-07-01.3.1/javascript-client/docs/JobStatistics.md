# BatchService.JobStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kernelCPUTime** | **String** |  | 
**lastUpdateTime** | **Date** |  | 
**numFailedTasks** | **Number** | A task fails if it exhausts its maximum retry count without returning exit code 0. | 
**numSucceededTasks** | **Number** | A task completes successfully if it returns exit code 0. | 
**numTaskRetries** | **Number** |  | 
**readIOGiB** | **Number** |  | 
**readIOps** | **Number** |  | 
**startTime** | **Date** |  | 
**url** | **String** |  | 
**userCPUTime** | **String** |  | 
**waitTime** | **String** | The wait time for a task is defined as the elapsed time between the creation of the task and the start of task execution. (If the task is retried due to failures, the wait time is the time to the most recent task execution.) This value is only reported in the account lifetime statistics; it is not included in the job statistics. | 
**wallClockTime** | **String** |  | 
**writeIOGiB** | **Number** |  | 
**writeIOps** | **Number** |  | 





# JobStatistics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kernelCPUTime** | **String** |  |  |
|**lastUpdateTime** | **OffsetDateTime** |  |  |
|**numFailedTasks** | **Long** | A Task fails if it exhausts its maximum retry count without returning exit code 0. |  |
|**numSucceededTasks** | **Long** | A Task completes successfully if it returns exit code 0. |  |
|**numTaskRetries** | **Long** |  |  |
|**readIOGiB** | **Double** |  |  |
|**readIOps** | **Long** |  |  |
|**startTime** | **OffsetDateTime** |  |  |
|**url** | **String** |  |  |
|**userCPUTime** | **String** |  |  |
|**waitTime** | **String** | The wait time for a Task is defined as the elapsed time between the creation of the Task and the start of Task execution. (If the Task is retried due to failures, the wait time is the time to the most recent Task execution.) This value is only reported in the Account lifetime statistics; it is not included in the Job statistics. |  |
|**wallClockTime** | **String** |  The wall clock time is the elapsed time from when the Task started running on a Compute Node to when it finished (or to the last time the statistics were updated, if the Task had not finished by then). If a Task was retried, this includes the wall clock time of all the Task retries. |  |
|**writeIOGiB** | **Double** |  |  |
|**writeIOps** | **Long** |  |  |




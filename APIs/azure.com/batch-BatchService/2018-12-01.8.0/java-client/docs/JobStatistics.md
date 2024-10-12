

# JobStatistics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kernelCPUTime** | **String** |  |  |
|**lastUpdateTime** | **OffsetDateTime** |  |  |
|**numFailedTasks** | **Long** | A task fails if it exhausts its maximum retry count without returning exit code 0. |  |
|**numSucceededTasks** | **Long** | A task completes successfully if it returns exit code 0. |  |
|**numTaskRetries** | **Long** |  |  |
|**readIOGiB** | **Double** |  |  |
|**readIOps** | **Long** |  |  |
|**startTime** | **OffsetDateTime** |  |  |
|**url** | **String** |  |  |
|**userCPUTime** | **String** |  |  |
|**waitTime** | **String** | The wait time for a task is defined as the elapsed time between the creation of the task and the start of task execution. (If the task is retried due to failures, the wait time is the time to the most recent task execution.) This value is only reported in the account lifetime statistics; it is not included in the job statistics. |  |
|**wallClockTime** | **String** |  The wall clock time is the elapsed time from when the task started running on a compute node to when it finished (or to the last time the statistics were updated, if the task had not finished by then). If a task was retried, this includes the wall clock time of all the task retries. |  |
|**writeIOGiB** | **Double** |  |  |
|**writeIOps** | **Long** |  |  |




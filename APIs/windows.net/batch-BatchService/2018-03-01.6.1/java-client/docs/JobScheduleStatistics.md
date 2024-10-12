

# JobScheduleStatistics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kernelCPUTime** | **String** |  |  |
|**lastUpdateTime** | **OffsetDateTime** |  |  |
|**numFailedTasks** | **Long** |  |  |
|**numSucceededTasks** | **Long** |  |  |
|**numTaskRetries** | **Long** |  |  |
|**readIOGiB** | **Double** |  |  |
|**readIOps** | **Long** |  |  |
|**startTime** | **OffsetDateTime** |  |  |
|**url** | **String** |  |  |
|**userCPUTime** | **String** |  |  |
|**waitTime** | **String** | This value is only reported in the account lifetime statistics; it is not included in the job statistics. |  |
|**wallClockTime** | **String** | The wall clock time is the elapsed time from when the task started running on a compute node to when it finished (or to the last time the statistics were updated, if the task had not finished by then). If a task was retried, this includes the wall clock time of all the task retries. |  |
|**writeIOGiB** | **Double** |  |  |
|**writeIOps** | **Long** |  |  |




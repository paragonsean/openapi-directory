

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
|**waitTime** | **String** | This value is only reported in the Account lifetime statistics; it is not included in the Job statistics. |  |
|**wallClockTime** | **String** | The wall clock time is the elapsed time from when the Task started running on a Compute Node to when it finished (or to the last time the statistics were updated, if the Task had not finished by then). If a Task was retried, this includes the wall clock time of all the Task retries. |  |
|**writeIOGiB** | **Double** |  |  |
|**writeIOps** | **Long** |  |  |




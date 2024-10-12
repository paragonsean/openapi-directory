

# JobStatistics

Resource usage statistics for a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kernelCPUTime** | **String** | The total kernel mode CPU time (summed across all cores and all compute nodes) consumed by all tasks in the job. |  |
|**lastUpdateTime** | **OffsetDateTime** | The time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. |  |
|**numFailedTasks** | **Long** | The total number of tasks in the job that failed during the given time range. |  |
|**numSucceededTasks** | **Long** | The total number of tasks successfully completed in the job during the given time range. |  |
|**numTaskRetries** | **Long** | The total number of retries on all the tasks in the job during the given time range. |  |
|**readIOGiB** | **Double** | The total gibibytes read from disk by all tasks in the job. |  |
|**readIOps** | **Long** | The total number of disk read operations made by all tasks in the job. |  |
|**startTime** | **OffsetDateTime** | The start time of the time range covered by the statistics. |  |
|**url** | **String** | The URL of the statistics. |  |
|**userCPUTime** | **String** | The total user mode CPU time (summed across all cores and all compute nodes) consumed by all tasks in the job. |  |
|**waitTime** | **String** | The total wait time of all tasks in the job. The wait time for a task is defined as the elapsed time between the creation of the task and the start of task execution. (If the task is retried due to failures, the wait time is the time to the most recent task execution.) |  |
|**wallClockTime** | **String** | The total wall clock time of all tasks in the job. |  |
|**writeIOGiB** | **Double** | The total gibibytes written to disk by all tasks in the job. |  |
|**writeIOps** | **Long** | The total number of disk write operations made by all tasks in the job. |  |




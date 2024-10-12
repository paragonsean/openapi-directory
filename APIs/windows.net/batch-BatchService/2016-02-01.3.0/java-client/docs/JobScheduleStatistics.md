

# JobScheduleStatistics

Resource usage statistics for a job schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kernelCPUTime** | **String** | The total kernel mode CPU time (summed across all cores and all compute nodes) consumed by all tasks in all jobs created under the schedule. |  |
|**lastUpdateTime** | **OffsetDateTime** | The time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. |  |
|**numFailedTasks** | **Long** | The total number of tasks that failed during the given time range in jobs created under the schedule. A task fails if it exhausts its maximum retry count without returning exit code 0. |  |
|**numSucceededTasks** | **Long** | The total number of tasks successfully completed during the given time range in jobs created under the schedule. A task completes successfully if it returns exit code 0. |  |
|**numTaskRetries** | **Long** | The total number of retries during the given time range on all tasks in all jobs created under the schedule. |  |
|**readIOGiB** | **Double** | The total gibibytes read from disk by all tasks in all jobs created under the schedule. |  |
|**readIOps** | **Long** | The total number of disk read operations made by all tasks in all jobs created under the schedule. |  |
|**startTime** | **OffsetDateTime** | The start time of the time range covered by the statistics. |  |
|**url** | **String** | The URL of the statistics. |  |
|**userCPUTime** | **String** | The total user mode CPU time (summed across all cores and all compute nodes) consumed by all tasks in all jobs created under the schedule. |  |
|**waitTime** | **String** | The total wait time of all tasks in all jobs created under the schedule. The wait time for a task is defined as the elapsed time between the creation of the task and the start of task execution. (If the task is retried due to failures, the wait time is the time to the most recent task execution.) |  |
|**wallClockTime** | **String** | The total wall clock time of all the tasks in all the jobs created under the schedule. |  |
|**writeIOGiB** | **Double** | The total gibibytes written to disk by all tasks in all jobs created under the schedule. |  |
|**writeIOps** | **Long** | The total number of disk write operations made by all tasks in all jobs created under the schedule. |  |




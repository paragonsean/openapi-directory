# BatchService.TaskStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kernelCPUTime** | **String** | The total kernel mode CPU time (summed across all cores and all compute nodes) consumed by the task. | 
**lastUpdateTime** | **Date** | The time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. | 
**readIOGiB** | **Number** | The total gibibytes read from disk by the task. | 
**readIOps** | **Number** | The total number of disk read operations made by the task. | 
**startTime** | **Date** | The start time of the time range covered by the statistics. | 
**url** | **String** | The URL of the statistics. | 
**userCPUTime** | **String** | The total user mode CPU time (summed across all cores and all compute nodes) consumed by the task. | 
**waitTime** | **String** | The total wait time of the task. The wait time for a task is defined as the elapsed time between the creation of the task and the start of task execution. (If the task is retried due to failures, the wait time is the time to the most recent task execution.) | 
**wallClockTime** | **String** | The total wall clock time of the task. | 
**writeIOGiB** | **Number** | The total gibibytes written to disk by the task. | 
**writeIOps** | **Number** | The total number of disk write operations made by the task. | 



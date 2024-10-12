# BatchService.TaskStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kernelCPUTime** | **String** | Gets or sets the total kernel mode CPU time (summed across all cores and all compute nodes) consumed by the task. | 
**lastUpdateTime** | **Date** | Gets or sets the time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. | 
**readIOGiB** | **Number** | Gets or sets the total amount of data in GiB of I/O read by the task. | 
**readIOps** | **Number** | Gets or sets the total number of I/O read operations performed by the task. | 
**startTime** | **Date** | Gets or sets the start time of the time range covered by the statistics. | 
**url** | **String** | Gets or sets the URL for the statistics. | 
**userCPUTime** | **String** | Gets or sets the total user mode CPU time (summed across all cores and all compute nodes) consumed by the task. | 
**waitTime** | **String** | Gets or sets the elapsed time between the creation of the task and the start of task execution. | 
**wallClockTime** | **String** | Gets or sets the total wall clock time of the task. | 
**writeIOGiB** | **Number** | Gets or sets the total amount of data in GiB of I/O written by the task. | 
**writeIOps** | **Number** | Gets or sets the total number of I/O write operations performed by the task. | 



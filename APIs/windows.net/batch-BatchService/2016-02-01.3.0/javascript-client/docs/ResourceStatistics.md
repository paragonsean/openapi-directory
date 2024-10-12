# BatchService.ResourceStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgCPUPercentage** | **Number** | The average CPU usage across all nodes in the pool (percentage per node). | 
**avgDiskGiB** | **Number** | The average used disk space in GiB across all nodes in the pool. | 
**avgMemoryGiB** | **Number** | The average memory usage in GiB across all nodes in the pool. | 
**diskReadGiB** | **Number** | The total amount of data in GiB of disk reads across all nodes in the pool. | 
**diskReadIOps** | **Number** | The total number of disk read operations across all nodes in the pool. | 
**diskWriteGiB** | **Number** | The total amount of data in GiB of disk writes across all nodes in the pool. | 
**diskWriteIOps** | **Number** | The total number of disk write operations across all nodes in the pool. | 
**lastUpdateTime** | **Date** | The time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. | 
**networkReadGiB** | **Number** | The total amount of data in GiB of network reads across all nodes in the pool. | 
**networkWriteGiB** | **Number** | The total amount of data in GiB of network writes across all nodes in the pool. | 
**peakDiskGiB** | **Number** | The peak used disk space in GiB across all nodes in the pool. | 
**peakMemoryGiB** | **Number** | The peak memory usage in GiB across all nodes in the pool. | 
**startTime** | **Date** | The start time of the time range covered by the statistics. | 



# BatchService.ResourceStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgCPUPercentage** | **Number** | Gets or sets the average CPU usage across all nodes in the pool (percentage per node). | 
**avgDiskGiB** | **Number** | Gets or sets the average used disk space in GiB across all nodes in the pool. | 
**avgMemoryGiB** | **Number** | Gets or sets the average memory usage in GiB across all nodes in the pool. | 
**diskReadGiB** | **Number** | Gets or sets the total amount of data in GiB of disk reads across all nodes in the pool. | 
**diskReadIOps** | **Number** | Gets or sets the total number of disk read operations across all nodes in the pool. | 
**diskWriteGiB** | **Number** | Gets or sets the total amount of data in GiB of disk writes across all nodes in the pool. | 
**diskWriteIOps** | **Number** | Gets or sets the total number of disk write operations across all nodes in the pool. | 
**lastUpdateTime** | **Date** | Gets or sets the time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. | 
**networkReadGiB** | **Number** | Gets or sets the total amount of data in GiB of network reads across all nodes in the pool. | 
**networkWriteGiB** | **Number** | Gets or sets the total amount of data in GiB of network writes across all nodes in the pool. | 
**peakDiskGiB** | **Number** | Gets or sets the peak used disk space in GiB across all nodes in the pool. | 
**peakMemoryGiB** | **Number** | Gets or sets the peak memory usage in GiB across all nodes in the pool. | 
**startTime** | **Date** | Gets or sets the start time of the time range covered by the statistics. | 



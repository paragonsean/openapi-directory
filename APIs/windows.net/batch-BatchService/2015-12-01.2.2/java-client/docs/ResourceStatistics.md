

# ResourceStatistics

Statistics related to resource consumption by compute nodes in a pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avgCPUPercentage** | **Double** | Gets or sets the average CPU usage across all nodes in the pool (percentage per node). |  |
|**avgDiskGiB** | **Double** | Gets or sets the average used disk space in GiB across all nodes in the pool. |  |
|**avgMemoryGiB** | **Double** | Gets or sets the average memory usage in GiB across all nodes in the pool. |  |
|**diskReadGiB** | **Double** | Gets or sets the total amount of data in GiB of disk reads across all nodes in the pool. |  |
|**diskReadIOps** | **Long** | Gets or sets the total number of disk read operations across all nodes in the pool. |  |
|**diskWriteGiB** | **Double** | Gets or sets the total amount of data in GiB of disk writes across all nodes in the pool. |  |
|**diskWriteIOps** | **Long** | Gets or sets the total number of disk write operations across all nodes in the pool. |  |
|**lastUpdateTime** | **OffsetDateTime** | Gets or sets the time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. |  |
|**networkReadGiB** | **Double** | Gets or sets the total amount of data in GiB of network reads across all nodes in the pool. |  |
|**networkWriteGiB** | **Double** | Gets or sets the total amount of data in GiB of network writes across all nodes in the pool. |  |
|**peakDiskGiB** | **Double** | Gets or sets the peak used disk space in GiB across all nodes in the pool. |  |
|**peakMemoryGiB** | **Double** | Gets or sets the peak memory usage in GiB across all nodes in the pool. |  |
|**startTime** | **OffsetDateTime** | Gets or sets the start time of the time range covered by the statistics. |  |




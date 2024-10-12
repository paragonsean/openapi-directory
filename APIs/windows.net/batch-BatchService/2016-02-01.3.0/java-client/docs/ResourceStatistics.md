

# ResourceStatistics

Statistics related to resource consumption by compute nodes in a pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avgCPUPercentage** | **Double** | The average CPU usage across all nodes in the pool (percentage per node). |  |
|**avgDiskGiB** | **Double** | The average used disk space in GiB across all nodes in the pool. |  |
|**avgMemoryGiB** | **Double** | The average memory usage in GiB across all nodes in the pool. |  |
|**diskReadGiB** | **Double** | The total amount of data in GiB of disk reads across all nodes in the pool. |  |
|**diskReadIOps** | **Long** | The total number of disk read operations across all nodes in the pool. |  |
|**diskWriteGiB** | **Double** | The total amount of data in GiB of disk writes across all nodes in the pool. |  |
|**diskWriteIOps** | **Long** | The total number of disk write operations across all nodes in the pool. |  |
|**lastUpdateTime** | **OffsetDateTime** | The time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. |  |
|**networkReadGiB** | **Double** | The total amount of data in GiB of network reads across all nodes in the pool. |  |
|**networkWriteGiB** | **Double** | The total amount of data in GiB of network writes across all nodes in the pool. |  |
|**peakDiskGiB** | **Double** | The peak used disk space in GiB across all nodes in the pool. |  |
|**peakMemoryGiB** | **Double** | The peak memory usage in GiB across all nodes in the pool. |  |
|**startTime** | **OffsetDateTime** | The start time of the time range covered by the statistics. |  |




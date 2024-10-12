# SharedImageGalleryServiceClient.ReplicationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregatedState** | **String** | This is the aggregated replication status based on all the regional replication status flags. | [optional] [readonly] 
**summary** | [**[RegionalReplicationStatus]**](RegionalReplicationStatus.md) | This is a summary of replication status for each region. | [optional] [readonly] 



## Enum: AggregatedStateEnum


* `Unknown` (value: `"Unknown"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)





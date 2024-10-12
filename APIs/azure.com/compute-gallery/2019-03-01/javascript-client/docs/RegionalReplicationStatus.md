# SharedImageGalleryServiceClient.RegionalReplicationStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **String** | The details of the replication status. | [optional] [readonly] 
**progress** | **Number** | It indicates progress of the replication job. | [optional] [readonly] 
**region** | **String** | The region to which the gallery Image Version is being replicated to. | [optional] [readonly] 
**state** | **String** | This is the regional replication state. | [optional] [readonly] 



## Enum: StateEnum


* `Unknown` (value: `"Unknown"`)

* `Replicating` (value: `"Replicating"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)




